from django.shortcuts import render
from .models import Deal

# Create your views here.


def index(request):
    deals = Deal.objects.all()
    return render(request, 'deals/home-page-1.html', {'deals': deals})