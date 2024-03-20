from django.shortcuts import render
from django.shortcuts import render
from .models import Product
from django.http import JsonResponse
import random
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from .models import Product
from django.contrib import messages
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from usersinformation.models import PlayerProfile
from decorate import login_requiredforuser
@login_requiredforuser
def shop(request, nickname):
    # Pass the nickname and score to the template
    context = {
        'nickname': nickname,

    }
    return render(request, 'index1.html', context=context)

@login_requiredforuser
def search_results(request):
    query = request.GET.get('q', '')  # 获取搜索词
    if query:
        products = Product.objects.filter(name__icontains=query)  # 过滤物品名称
    else:
        products = Product.objects.none()  # 无搜索词时返回空查询

    return render(request, 'search_results.html', {'products': products})


# Create your views here.

@login_requiredforuser
def lottery_draw(request):
    # 如果是GET请求，显示抽奖页面
    return render(request, 'lottery.html')

@login_requiredforuser
def buy_product(request, name, nickname):
    # 获取请求的商品
    product = Product.objects.get(name=name)

    # 获取用户的积分情况
    user_profile = PlayerProfile.objects.get(nickname=nickname)

    # 检查用户是否有足够的积分购买商品
    if user_profile.score >= product.price:
        # 减去相应的积分
        user_profile.score -= product.price
        user_profile.save()

        # 增加商品销量，如果你跟踪的话
        # product.sales += 1
        # product.save()

        # 记录购买...

        # 显示购买成功消息
        #messages.success(request, "Purchase successful!")
        # 或者返回JSON响应
        return JsonResponse({'status':'success'})
    else:
        # 积分不足
        #messages.error(request, "You do not have enough points.")
        # 或者返回JSON响应
        return JsonResponse({'status':'fail'})


@login_requiredforuser
def product_detail(request, name, nickname):
    product = Product.objects.get(name=name)
    return render(request, 'product_detail.html', {'product': product, 'nickname':nickname })

