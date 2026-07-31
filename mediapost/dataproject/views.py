from django.shortcuts import render
from myapp.models import MyPost

# Create your views here.

def home(request):
    post = MyPost.objects.order_by('-created_at')[:3]  #Only latest 3
    return render(request, 'website/home.html', {'posts_': post})