from django.urls import path
from .views import (BlogListView, BlogDetailView, BlogCreateView, 
                    BlogUpdateView, BlogDeleteView, add_comment_to_post,
                    UserRegisterView)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/comment/', add_comment_to_post, name='add_comment_to_post'),
    path("registration/register", UserRegisterView.as_view(), name="register"),
    # path("password_change/", auth_views.PasswordChangeView.as_view(
    #     template_name='registration/change_password.html'), name='password_change'),
]
