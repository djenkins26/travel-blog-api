from django.urls import path
from .views.blog_post_views import Blog, BlogDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
  	# Restful routing
    path('blog_posts/', Blog.as_view(), name='blog_posts'),
    path('blog_posts/<int:pk>/', BlogDetail.as_view(), name='blog_post_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
