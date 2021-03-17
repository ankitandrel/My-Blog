from django.urls import path
from . import views
urlpatterns = [
  path('', views.posts, name = 'posts' ),
  path('post/<int:id>', views.post_details, name='post_details'),
  path('create_post/',views.create_post, name = 'create_post'),
  path('update_post/<int:id>', views.update_post, name='update_post'),
  path('delete_post/<int:id>/', views.delete_post, name='delete_post'),
  path('search/', views.search, name='search'),

] 

