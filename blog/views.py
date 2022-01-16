from django.shortcuts import render
import blog.views


# Create your views here.
def index(request):
    return render(request, "blog/index.html")