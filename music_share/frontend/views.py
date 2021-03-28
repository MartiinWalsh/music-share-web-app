from django.shortcuts import render

# Create your views here.
# Return the html and template
def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html')