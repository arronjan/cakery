from django.shortcuts import render

def home(request):  # Changed this name to match your urls.py
    return render(request, 'bakery/index.html')