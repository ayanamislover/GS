from django.http import HttpResponseRedirect
from functools import wraps  # 导入wraps


def login_requiredforuser(f):
    @wraps(f)  # 使用wraps装饰内部函数
    def wrap(request, *args, **kwargs):
        if not request.session.get('is_logged_in'):
            # 使用绝对路径重定向到web app中的登录页面
            return HttpResponseRedirect('/login/')
        return f(request, *args, **kwargs)
    return wrap