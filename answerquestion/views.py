from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render,redirect,reverse
from .models import Choice, UserAnswer, Question,Series
from .forms import QuizForm
from usersinformation.models import PlayerProfile
from urllib.parse import urlencode
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from achievement.models import Achievement
from usersinformation.models import AchievementAndUser
# Define an unlogged interface without a primary key
from django.db.models import Q

def index_none(request):
    # render the response using the Render function, specifying the template file and context data (if any)
    return render(request, 'usersinformation/player_profile_none.html')

# Answer main page
def index(request, nickname):
    series_list = Series.objects.all()
    user_profile = get_object_or_404(PlayerProfile, nickname=nickname)

    # Suppose PlayerProfile has a method or property to get the completed series
    completed_series_ids = user_profile.completed_series.values_list('id', flat=True)

   # Adds completion status to the series list
    series_with_status = []
    for series in series_list:
        series_with_status.append({
            'series': series,
            'is_completed': series.id in completed_series_ids,
        })

    return render(request, 'answerquestion/index.html', {
        'series_with_status': series_with_status,
        'user_nickname': user_profile.nickname,

    })

#lcoal
def series_detail(request, series_id, nickname):
    print("进入这个url了么")
    series = get_object_or_404(Series, pk=series_id)
    questions = series.questions.all()
    player_profile = get_object_or_404(PlayerProfile, nickname=nickname)  # Gets the user instance based on the incoming user pk
    # 获取用户昵称
    user_nickname = player_profile.nickname  # Assume that the PlayerProfile model has a nickname field

    if request.method == 'POST':
        form = QuizForm(request.POST, questions=questions)
        if form.is_valid():
            total_score = calculate_score(form.cleaned_data, questions)
             #Update the score in the user's PlayerProfile
            try:
               #  这里给用户加分了，于此同时判断一下是否达成了新成就，如果达成新成就要添加一条新记录
               player_profile = PlayerProfile.objects.get(nickname=nickname)

               oldscore = player_profile.score
               player_profile.score += total_score  # Increase score
               newscore = player_profile.score
               player_profile.save()
               print("现在开始判断该用户的积分足够达到新成就了么：", oldscore, newscore)
               # 大于旧分数，小于等于新分数的成就
               achievement_detail = Achievement.objects.filter(Q(unlock_score__gt=oldscore) & Q(unlock_score__lte=newscore))
               for achievement in achievement_detail:
                   print("找到了新成就：", achievement.name)
                   # 添加一条新的成就记录
                   achievement_and_user = AchievementAndUser()
                   achievement_and_user.user = player_profile
                   achievement_and_user.achievement = achievement
                   achievement_and_user.save()

            except PlayerProfile.DoesNotExist:
            # Handle situations where the user does not have a PlayerProfile
             pass

           # Build urls with query strings
            results_url = reverse('ans:results_page', kwargs={'nickname': nickname,'series_id':series_id}) + f'?score={total_score}'
            return redirect(results_url)
    else:
        form = QuizForm(questions=questions)

    return render(request, 'answerquestion/detail.html', {'form': form, 'series': series, 'user_nickname': user_nickname})

#@csrf_exempt
def results_page(request, nickname,series_id):
    # Get the score from the query string
    additional_score = int(request.GET.get('score', 0))
    # Get a PlayerProfile instance
    player_profile = get_object_or_404(PlayerProfile, nickname=nickname)
    # Suppose you pass the ID of the series through the query string

    series_completed = False  # is used to mark if the series is complete

    if series_id:
        series = get_object_or_404(Series, pk=series_id)
       # Add series to completed_series if it's not already there
        if series not in player_profile.completed_series.all():
            player_profile.completed_series.add(series)
            series_completed = True # series completion is marked True
    # Prepares the context data to be passed to the template

    context = {
        'series_id': series_id,
           'nickname': player_profile.nickname,
          'total_score': player_profile.score,
         'additional_score': additional_score,
       'series_completed': series_completed,  # Indicates whether the column is complete

     }
    if series_id % 2 == 1:
    # If series_id is odd, use results_page.html
        return render(request, 'answerquestion/results_page.html', {
        'series_id': series_id, 'nickname': nickname, 'additional_score': additional_score
    })
    else:
    # If series_id is even, use results_page1.html
        return render(request, 'answerquestion/results_page1.html', {
        'series_id': series_id, 'nickname': nickname, 'additional_score': additional_score
    })




def calculate_score(cleaned_data, questions):
   # Calculate the total score based on cleaned data and correct answers
    total_score = 0
    for question in questions:
        correct_answer = question.choices.get(is_correct=True).id
        given_answer = int(cleaned_data.get('question_%s' % question.id))
        if correct_answer == given_answer:
            total_score += 1 # Assume 1 point for each question
    return total_score


#@csrf_exempt # You can temporarily disable CSRF protection if you do not process CSRF tokens
def submit_answers(request):
    if request.method == 'POST':
        total_score = 0
        correct_answers = 0
       # Suppose each question is scored 1 point
        score_per_question = 1
        user_answers = request.POST
        for key, value in user_answers.items():
            if key.startswith('question_'):
                question_id = key.split('_')[1]
                selected_choice = value
                correct_choice = Choice.objects.filter(question_id=question_id, is_correct=True).first()

                if correct_choice and str(correct_choice.id) == selected_choice:
                    total_score += score_per_question
                    correct_answers += 1

        # Save results to session or database (as needed)
# For example: request.session['total_score'] = total_score

        # Redirect to the results page
        return redirect('results_page', total_score=total_score, correct_answers=correct_answers)
    else:
      # If not POST request, redirect back to home page or other page
        return redirect('index')
