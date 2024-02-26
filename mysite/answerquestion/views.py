from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render,redirect,reverse
from .models import Choice, UserAnswer, Question,Series
from .forms import QuizForm
from usersinformation.models import PlayerProfile
from urllib.parse import urlencode
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


#定义未有主键的未登录界面
def index_none(request):
    # 使用render函数渲染响应，指定模板文件和上下文数据（如果有）
    return render(request, 'usersinformation/player_profile_none.html')

#答题主页面
def index(request, nickname):
    series_list = Series.objects.all()
    user_profile = get_object_or_404(PlayerProfile, nickname=nickname)

    # 假设 PlayerProfile 有一个方法或属性来获取已完成的系列
    completed_series_ids = user_profile.completed_series.values_list('id', flat=True)

    # 为系列列表添加完成状态
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

#本地
def series_detail(request, series_id, nickname):
    series = get_object_or_404(Series, pk=series_id)
    questions = series.questions.all()
    player_profile = get_object_or_404(PlayerProfile, nickname=nickname)  # 根据传入的用户pk获取用户实例
    # 获取用户昵称
    user_nickname = player_profile.nickname  # 假设PlayerProfile模型有一个nickname字段

    if request.method == 'POST':
        form = QuizForm(request.POST, questions=questions)
        if form.is_valid():
            total_score = calculate_score(form.cleaned_data, questions)
             #更新用户的PlayerProfile中的score
            try:
               player_profile = PlayerProfile.objects.get(nickname=nickname)
               player_profile.score += total_score  # 增加得分
               player_profile.save()
            except PlayerProfile.DoesNotExist:
            #处理用户没有PlayerProfile的情况
             pass

            # 构建带有查询字符串的URL
            results_url = reverse('results_page', kwargs={'nickname': nickname}) + f'?score={total_score}'
            return redirect(results_url)
    else:
        form = QuizForm(questions=questions)

    return render(request, 'answerquestion/detail.html', {'form': form, 'series': series, 'user_nickname': user_nickname})


def results_page(request, nickname):
    # 从查询字符串中获取得分
    additional_score = int(request.GET.get('score', 0))
    # 获取PlayerProfile实例
    player_profile = get_object_or_404(PlayerProfile, nickname=nickname)
    # 假设通过查询字符串传递系列的ID
    series_id = request.GET.get('series_id')

    series_completed = False  # 用于标记系列是否完成

    if series_id:
        series = get_object_or_404(Series, pk=series_id)
        # 添加系列到completed_series，如果它还不在那里
        if series not in player_profile.completed_series.all():
            player_profile.completed_series.add(series)
            series_completed = True  # 系列完成标记为True
    # 准备传递给模板的上下文数据

    context = {
           'nickname': player_profile.nickname,
          'total_score': player_profile.score,
         'additional_score': additional_score,
       'series_completed': series_completed,  # 标记系列是否完成

     }
    return render(request, 'answerquestion/results_page.html', context)




#梓涵
def series_detail1(request, series_id, nickname):
    series = get_object_or_404(Series, pk=series_id)
    questions = series.questions.all()
    player_profile = get_object_or_404(PlayerProfile, nickname=nickname)  # 根据传入的用户pk获取用户实例
    # 获取用户昵称
    user_nickname = player_profile.nickname  # 假设PlayerProfile模型有一个nickname字段

    if request.method == 'POST':
        form = QuizForm(request.POST, questions=questions)
        if form.is_valid():
            total_score = calculate_score(form.cleaned_data, questions)
             #更新用户的PlayerProfile中的score
            try:
               player_profile = PlayerProfile.objects.get(nickname=nickname)
               player_profile.score += total_score  # 增加得分
               player_profile.save()
            except PlayerProfile.DoesNotExist:
            #处理用户没有PlayerProfile的情况
             pass

            # 构建带有查询字符串的URL
            results_url = reverse('results_page', kwargs={'nickname': nickname}) + f'?score={total_score}'
            return redirect(results_url)
    else:
        form = QuizForm(questions=questions)

    return render(request, 'answerquestion/detail.html', {'form': form, 'series': series, 'user_nickname': user_nickname})

#梓涵
def results_page1(request, nickname):
    # 从查询字符串中获取得分
    additional_score = int(request.GET.get('score', 0))
    # 获取PlayerProfile实例
    player_profile = get_object_or_404(PlayerProfile, nickname=nickname)
    # 假设通过查询字符串传递系列的ID
    series_id = request.GET.get('series_id')

    series_completed = False  # 用于标记系列是否完成

    if series_id:
        series = get_object_or_404(Series, pk=series_id)
        # 添加系列到completed_series，如果它还不在那里
        if series not in player_profile.completed_series.all():
            player_profile.completed_series.add(series)
            series_completed = True  # 系列完成标记为True


    # 创建查询字典
    query_dict = {
        'nickname': player_profile.nickname,
        'additional_score':additional_score,
        'series_id': series_id,  # 添加series_id到字典中
    }

    # 将查询字典转换为查询字符串
    query_string = urlencode(query_dict)

    # 生成重定向URL，附加查询字符串
    return_url = reverse('你的视图函数名字', args=[player_profile.nickname]) + '?' + query_string

    # 重定向到目标URL
    return redirect(return_url)

    # 准备传递给模板的上下文数据
#    context = {
 #       'nickname': player_profile.nickname,
  #      'total_score': player_profile.score,
   #     'additional_score': additional_score,
    #    'pk': pk,
     #   'series_completed': series_completed,  # 标记系列是否完成
        #'return_url': return_url  # 返回到其他模块的URL
    #}
    #return render(request, 'answerquestion/results_page.html', context)

def calculate_score(cleaned_data, questions):
    # 根据cleaned_data和正确的答案计算总分
    total_score = 0
    for question in questions:
        correct_answer = question.choices.get(is_correct=True).id
        given_answer = int(cleaned_data.get('question_%s' % question.id))
        if correct_answer == given_answer:
            total_score += 1  # 假设每个问题1分
    return total_score


#@csrf_exempt  # 如果你不处理CSRF令牌，可以暂时禁用CSRF保护
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

        # 保存结果到session或数据库（根据需要）
        # 例如: request.session['total_score'] = total_score

        # 重定向到结果页面
        return redirect('results_page', total_score=total_score, correct_answers=correct_answers)
    else:
        # 如果不是POST请求，则重定向回首页或其他页面
        return redirect('index')

#lcy
def series_detail2(request, series_id, nickname):
        series2 = get_object_or_404(Series, pk=series_id)
        questions2 = series2.questions.all()
        player_profile2 = get_object_or_404(PlayerProfile, nickname=nickname)  # 根据传入的用户pk获取用户实例
        # 获取用户昵称
        user_nickname2 = player_profile2.nickname  # 假设PlayerProfile模型有一个nickname字段

        if request.method == 'POST':
            form = QuizForm(request.POST, questions=questions2)
            if form.is_valid():
                total_score = calculate_score(form.cleaned_data, questions2)
                # 更新用户的PlayerProfile中的score
                try:
                    player_profile2 = PlayerProfile.objects.get(nickname=nickname)
                    player_profile2.score += total_score  # 增加得分
                    player_profile2.save()
                except PlayerProfile.DoesNotExist:
                    # 处理用户没有PlayerProfile的情况
                    pass

                # 构建带有查询字符串的URL
                results_url = reverse('results_page', kwargs={'nickname': nickname}) + f'?score={total_score}'
                return redirect(results_url)
        else:
            form = QuizForm(questions=questions2)

        return render(request, 'answerquestion/detail.html',
                      {'form': form, 'series': series2, 'user_nickname': user_nickname2})

#lcy
def results_page2(request, nickname):
        # 从查询字符串中获取得分
        additional_score = int(request.GET.get('score', 0))
        # 获取PlayerProfile实例
        player_profile = get_object_or_404(PlayerProfile, nickname=nickname)
        # 假设通过查询字符串传递系列的ID
        series_id = request.GET.get('series_id')

        series_completed = False  # 用于标记系列是否完成

        if series_id:
            series = get_object_or_404(Series, pk=series_id)
            # 添加系列到completed_series，如果它还不在那里
            if series not in player_profile.completed_series.all():
                player_profile.completed_series.add(series)
                series_completed = True  # 系列完成标记为True

        # 创建查询字典
        query_dict = {
            #'nickname': player_profile.nickname,
            'additional_score': additional_score,
            #'series_id': series_id,  # 添加series_id到字典中
        }

        # 将查询字典转换为查询字符串
        query_string = urlencode(query_dict)

        # 生成重定向URL，附加查询字符串
        return_url = reverse('你的视图函数名字', args=[player_profile.nickname]) + '?' + query_string

        # 重定向到目标URL
        return redirect(return_url)