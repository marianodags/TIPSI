from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

def index(request):

    return render(request, 'pythontutorials/index.html')


def main(request):

    return render(request, 'pythontutorials/main.html')

def about(request):

    return render(request, 'pythontutorials/about.html')


def terms(request):
    return render(request, 'pythontutorials/terms.html')

def services(request):
    return render(request, 'pythontutorials/services.html')

def privacypolicy(request):
    return render(request, 'pythontutorials/privacypolicy.html')





def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'pythontutorials/blog.html', context)
class PostListView(ListView):
    model = Post
    template_name = 'pythontutorials/blog.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
