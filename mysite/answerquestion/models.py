from django.db import models
from django.contrib.auth.models import User

class Series(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.name

class Question(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE, related_name='questions', null=True)
    text = models.CharField(max_length=200)
    score = models.IntegerField(default=1)  # 假设每个问题默认得分为1
    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)  # 设置为True如果选择的choice是正确的
