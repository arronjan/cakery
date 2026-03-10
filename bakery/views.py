from django.shortcuts import render

# If this says 'def index', then the urls.py must say 'views.index'
def index(request):
    return render(request, 'bakery/index.html')