from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render,redirect,reverse
from .models import Choice, UserAnswer, Question,Series
from .forms import QuizForm
from usersinformation.models import PlayerProfile
from urllib.parse import urlencode
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


#Define an unlogged-in screen without a primary key
def index_none(request):
    # Render the response using the render function, specifying the template file and context data (if any)
    return render(request, 'usersinformation/player_profile_none.html')

#Quize main page
def index(request, nickname):
    series_list = Series.objects.all()
    user_profile = get_object_or_404(PlayerProfile, nickname=nickname)

    # PlayerProfile property to get the completed series
    completed_series_ids = user_profile.completed_series.values_list('id', flat=True)

    # Adding a completion status to the series list
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

#Quize's series
def series_detail(request, series_id, nickname):
    series = get_object_or_404(Series, pk=series_id)
    questions = series.questions.all()
    player_profile = get_object_or_404(PlayerProfile, nickname=nickname)
    user_nickname = player_profile.nickname

    if request.method == 'POST':
        form = QuizForm(request.POST, questions=questions)
        if form.is_valid():
            total_score = calculate_score(form.cleaned_data, questions)
             #Updating the score in the user's PlayerProfile
            try:
               player_profile = PlayerProfile.objects.get(nickname=nickname)
               player_profile.score += total_score
            except PlayerProfile.DoesNotExist:
            #Handling cases where the user does not have a PlayerProfile
             pass
            # Constructing URLs with query strings
            results_url = reverse('ans:results_page', kwargs={'nickname': nickname,'series_id':series_id}) + f'?score={total_score}'
            return redirect(results_url)
    else:
        form = QuizForm(questions=questions)

    return render(request, 'answerquestion/detail.html', {'form': form, 'series': series, 'user_nickname': user_nickname})

#Result page, to show the result detail
def results_page(request, nickname,series_id):
    # Getting a score from a query string
    additional_score = int(request.GET.get('score', 0))
    # Get PlayerProfile instance
    player_profile = get_object_or_404(PlayerProfile, nickname=nickname)
    # Used to mark series completion
    series_completed = False

    if series_id:
        series = get_object_or_404(Series, pk=series_id)
        # Add series to completed_series
        if series not in player_profile.completed_series.all():
            player_profile.completed_series.add(series)
            series_completed = True
    #Context data passed to the template
    context = {
        'series_id': series_id,
        'nickname': player_profile.nickname,
        'total_score': player_profile.score,
        'additional_score': additional_score,
        'series_completed': series_completed,
     }
    return render(request, 'answerquestion/results_page.html',
                  {'series_id': series_id, 'nickname': nickname, 'additional_score': additional_score})


#zihan,different peer that use the Quzie series page with samm logic
def series_detail1(request, series_id, nickname):
    series = get_object_or_404(Series, pk=series_id)
    questions = series.questions.all()
    player_profile = get_object_or_404(PlayerProfile, nickname=nickname)
    user_nickname = player_profile.nickname

    if request.method == 'POST':
        form = QuizForm(request.POST, questions=questions)
        if form.is_valid():
            total_score = calculate_score(form.cleaned_data, questions)
             #Updating the score in the user's PlayerProfile
            try:
               player_profile = PlayerProfile.objects.get(nickname=nickname)
               player_profile.score += total_score
               player_profile.save()
            except PlayerProfile.DoesNotExist:
            # Handling cases where the user does not have a PlayerProfile
             pass
            # Constructing URLs with query strings
            results_url = reverse('results_page', kwargs={'nickname': nickname}) + f'?score={total_score}'
            return redirect(results_url)
    else:
        form = QuizForm(questions=questions)

    return render(request, 'answerquestion/detail.html', {'form': form, 'series': series, 'user_nickname': user_nickname})

#Same logic
def results_page1(request, nickname):
    # Get socre
    additional_score = int(request.GET.get('score', 0))
    # Get PlayerProfile instance
    player_profile = get_object_or_404(PlayerProfile, nickname=nickname)
    # Get series id
    series_id = request.GET.get('series_id')
    series_completed = False

    if series_id:
        series = get_object_or_404(Series, pk=series_id)
        if series not in player_profile.completed_series.all():
            player_profile.completed_series.add(series)
            series_completed = True
    # Create query dictionary
    query_dict = {
        'nickname': player_profile.nickname,
        'additional_score':additional_score,
        'series_id': series_id,
    }

    # change to query string
    query_string = urlencode(query_dict)
    #
    return_url = reverse('your name', args=[player_profile.nickname]) + '?' + query_string

    return redirect(return_url)


def calculate_score(cleaned_data, questions):
    # Calculate total score based on cleaned_data and correct answers
    total_score = 0
    for question in questions:
        correct_answer = question.choices.get(is_correct=True).id
        given_answer = int(cleaned_data.get('question_%s' % question.id))
        if correct_answer == given_answer:
            total_score += 1
    return total_score


#not use
def submit_answers(request):
    if request.method == 'POST':
        total_score = 0
        correct_answers = 0
        # 假设每个问题的得分是1分
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

        return redirect('results_page', total_score=total_score, correct_answers=correct_answers)
    else:

        return redirect('index')

#lcy Same logic
def series_detail2(request, series_id, nickname,useid):
        series2 = get_object_or_404(Series, pk=series_id)
        questions2 = series2.questions.all()
        player_profile2 = get_object_or_404(PlayerProfile, nickname=nickname)

        user_nickname2 = player_profile2.nickname

        if request.method == 'POST':
            form = QuizForm(request.POST, questions=questions2)
            if form.is_valid():
                total_score = calculate_score(form.cleaned_data, questions2)
                #
                try:
                    player_profile2 = PlayerProfile.objects.get(nickname=nickname)
                    player_profile2.score += total_score
                    player_profile2.save()
                except PlayerProfile.DoesNotExist:

                    pass


                results_url = reverse('results_page2', kwargs={'nickname': nickname}) + f'?score={total_score}'
                return redirect(results_url)
        else:
            form = QuizForm(questions=questions2)

        return render(request, 'answerquestion/detail.html',
                      {'form': form, 'series': series2, 'user_nickname': user_nickname2})

#lcy
def results_page2(request, nickname):
        print('1111:')

        additional_score = int(request.GET.get('score', 0))

        player_profile = get_object_or_404(PlayerProfile, nickname=nickname)

        series_id = request.GET.get('series_id')

        series_completed = False

        if series_id:
            series = get_object_or_404(Series, pk=series_id)

            if series not in player_profile.completed_series.all():
                player_profile.completed_series.add(series)
                series_completed = True

        query_dict = {
            #'nickname': player_profile.nickname,
            'additional_score': additional_score,
            #'series_id': series_id,
        }

        query_string = urlencode(query_dict)

        return_url = reverse('navi', args=[player_profile.nickname]) + '?' + query_string

        return redirect(return_url)