from django.shortcuts import render, redirect, get_object_or_404
from .models import Deal

def index(request):
    deals = Deal.objects.all()
    return render(request, 'deals/home-page-1.html', {'deals': deals})

def page_detail(request, pk):
    deal = get_object_or_404(Deal, id=pk)
    context = {"deal": deal}
    return render(request, 'deals/page_detail.html', context)