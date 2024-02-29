from django.shortcuts import render

#from GS.mysite.usersinformation.models import PlayerProfile
from .models import Gift
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



def gift_list(request):
    sort_method = request.GET.get('sort')
    search_query = request.GET.get('q', '')
 #   nickname = PlayerProfile.nickname
    if search_query:
        gifts = Gift.objects.filter(name__icontains=search_query)
    else:
        gifts = Gift.objects.all()
#    points = PlayerProfile.nickname.score
    if sort_method == 'asc':
        gifts = gifts.order_by('points')
    elif sort_method == 'desc':
        gifts = gifts.order_by('-points')
    context = {
#        'nickname': nickname,
        'gifts': gifts,
#        'points': points
    }

    return render(request, 'rewards/gift_list.html', context)


def gift_detail(request, id):
    gift = get_object_or_404(Gift, pk=id)
    return render(request, 'rewards/gift_detail.html', {'gift': gift})

@csrf_exempt  # Disable CSRF protection temporarily. Use it with caution in actual projects
def buy_gift(request, gift_id):
    if request.method == 'POST':
        # This is where purchase logic is performed, such as deducting user credits

        # Assuming successful purchase
        return JsonResponse({'message': 'Purchase successful!'})
    else:
        return JsonResponse({'message': 'Invalid request'}, status=400)



