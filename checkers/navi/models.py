from django.db import models

class Checker(models.Model):
    # 编号，使用Django的自动增长主键字段
    id = models.AutoField(primary_key=True)
    # 经度，使用DecimalField以存储精确的小数，并指定最大位数和小数位
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    # 纬度，同样使用DecimalField
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    # 地点名称，使用CharField并指定最大长度
    location_name = models.CharField(max_length=255)

class player_profile(models.Model):
    last_game_start = models.DateTimeField(null=True, blank=True)
    verified_locations_count = models.IntegerField(default=0)

    def __str__(self):
        return self.location_name
