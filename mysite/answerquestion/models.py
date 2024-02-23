from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=200)  # 题目文本
    pub_date = models.DateTimeField('date published')  # 发布日期

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # 关联题目
    choice_text = models.CharField(max_length=200)  # 选项文本
    is_correct = models.BooleanField(default=False)  # 是否为正确答案
