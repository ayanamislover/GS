from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'answerquestion/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'answerquestion/detail.html', {'question': question})

#处理AJAX请求，判断用户的答案是否正确，并返回得分更新的结果
def submit_answer(request, question_id):
    if request.method == 'POST' and request.is_ajax():
        selected_choice_id = request.POST.get('choice')
        selected_choice = Choice.objects.get(id=selected_choice_id)
        is_correct = selected_choice.is_correct
        # 更新得分逻辑（根据你的具体需求实现）
        score_update = 10 if is_correct else 0
        return JsonResponse({'is_correct': is_correct, 'score_update': score_update})
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)