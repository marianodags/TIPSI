from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [

    path('', views.main, name='python-main'),
    path('index/', views.index, name='python-index'),
    path('about/', views.about, name='python-about'),
    path('terms/', views.terms, name='python-terms'),
    path('services/', views.services ,name='python-services'),
    path('privacypolicy/', views.privacypolicy ,name='python-privacypolicy'),
    path('blog/', PostListView.as_view() ,name='python-blog'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),



]
