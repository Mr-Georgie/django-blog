from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post, Comment
from django.urls import reverse_lazy
from django.forms import ModelForm

from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    
    
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    
class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title','author','body']
    
class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title','body']
    
class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    
    
    
# Create comment views here.
class CommentForm(ModelForm):
    
    class Meta:
        model = Comment
        fields = ('name', 'comment_text',)
        
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})