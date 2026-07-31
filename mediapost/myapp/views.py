from django.shortcuts import render
from django.http import HttpResponse
from . models import MyPost
from . forms import MyPostForm, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# get all the posts
def post_list(request):
    posts = MyPost.objects.all().order_by('-created_at')
    return render(request, 'post_list.html', {'posts_': posts}) 
# this post_list.html we will make afterwards

@login_required
# to make a post
def post_create(request):
    if request.method == 'POST':
        form=MyPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # commit=False means that it wil now save in the DB but only in the given variable
            post.user = request.user
            post.save() #this will save the form in the DB
            return redirect('post_list')
    else:
        form = MyPostForm()
    return render(request, 'post_form.html', {'form_': form})

@login_required
# edit post
def post_edit(request, post_id):
    post = get_object_or_404(MyPost, pk=post_id, user=request.user)
    if request.method=='POST':
        form=MyPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_list')
    else:
        form = MyPostForm(instance=post)
    return render(request, 'post_form.html', {'form_': form})
    
@login_required
# delete post
def post_delete(request, post_id):
    post = get_object_or_404(MyPost, pk=post_id, user=request.user)
    if request.method=='POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'post_delete.html', {'post_': post})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # here the password1 is the field that we put in the form, where user will put the password
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('post_list')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form_': form})
  