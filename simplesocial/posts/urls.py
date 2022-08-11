from . import views
from django.urls import path

app_name = 'posts'

urlpatterns = [
    path('', views.PostList.as_view(template_name='post_list.html'), name='all'),
    path('new/', views.CreatePost.as_view(), name='create'),
    path('by/<str:username>/', views.UserPosts.as_view(), name='for_user'),
    path('by/<str:username>/<int:pk>/', views.PostDetail.as_view(), name='single'),
    path('delete/<int:pk>/', views.DeletePost.as_view(), name='delete'),
]
