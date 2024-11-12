
from django.shortcuts import render

from django.contrib.auth.decorators import login_required

def public_page(request):
    return render(request, 'public_page.html')



@login_required
def home(request):
    return render(request, 'home.html')