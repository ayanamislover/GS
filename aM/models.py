from django.db import models


class Activity(models.Model):
    """
    An activity model 活动模型
    """
    title = models.CharField(max_length=120)  # 标题，字符串类型
    content = models.TextField()  # 内容，文本类型
    publish_date = models.DateTimeField(auto_now_add=True)  # 出版时间，日期时间类型，默认为当前时间
    start_date = models.DateTimeField()  # 开始时间，日期时间类型
    end_date = models.DateTimeField()  # 结束时间，日期时间类型
    location = models.CharField(max_length=255)  # 地点，字符串类型
    max_participants = models.PositiveIntegerField()  # 最大参与人数，正整数类型
    fee = models.DecimalField(max_digits=10, decimal_places=2)  # 费用，十进制类型
    status = models.CharField(max_length=20, choices=[('draft', 'Draft 草稿'), ('published', 'Published 发布'), ('ended', 'Ended 结束')], default='draft')  # 状态，选择类型，默认为草稿
    organizer = models.CharField(max_length=120)  # 组织者，字符串类型
    category = models.CharField(max_length=50)  # 类别，字符串类型
    tags = models.CharField(max_length=255, blank=True, null=True)  # 标签，字符串类型，可以为空
    series_id = models.CharField(max_length=100, unique=True)
