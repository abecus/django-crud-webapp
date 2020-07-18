from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django import forms 
# from django.views.generic import CreateView


class InputForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("task", )

def home(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("crud-home")

    tasks = Post.objects.all()
    form = InputForm()
    return render(request, "crud/home.html", context={'tasks':tasks, "form":form})

def update(request, pk):
    task = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = InputForm(request.POST, instance=task)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect("crud-home")
    else:
        form = InputForm(instance=task)
    return render(request, 'crud/update.html', {'form': form})

def delete(request, pk):
    Post.objects.get(pk=pk).delete()
    return redirect("crud-home")