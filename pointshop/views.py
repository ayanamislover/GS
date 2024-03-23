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
    query = request.GET.get('q', '')  # Get search terms
    if query:
        products = Product.objects.filter(name__icontains=query)  # filter item name
    else:
        products = Product.objects.none()  # Returns an empty query when there are no search terms

    return render(request, 'search_results.html', {'products': products})


# Create your views here.

@login_requiredforuser
def lottery_draw(request):
    # If it is a GET request, the sweepstakes page is displayed
    return render(request, 'lottery.html')

@login_requiredforuser
def buy_product(request, name, nickname):
    # get the required items
    product = Product.objects.get(name=name)

    # get the points situation from users
    user_profile = PlayerProfile.objects.get(nickname=nickname)

    # check whether the user has the 
    if user_profile.score >= product.price:
        # decrease the points
        user_profile.score -= product.price
        user_profile.save()

        # increase the number of products
        # product.sales += 1
        # product.save()

        # record the purchased items

        # appear the purchase information
        #messages.success(request, "Purchase successful!")
        # back to JSON response
        return JsonResponse({'status':'success'})
    else:
        # inadequate points
        #messages.error(request, "You do not have enough points.")
        # or back to the JASONRESPONSE
        return JsonResponse({'status':'fail'})


@login_requiredforuser
def product_detail(request, name, nickname):
    product = Product.objects.get(name=name)
    return render(request, 'product_detail.html', {'product': product, 'nickname':nickname })

