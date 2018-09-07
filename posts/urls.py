from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url

from posts.views import posts_home
from posts.views import posts_detail
from posts.views import posts_list
from posts.views import posts_update
from posts.views import posts_delete
from posts.views import posts_create

from posts import views


app_name = 'posts'

urlpatterns = [
    path('', posts_list,name='list'),
    path('create/', posts_create),
    path('<int:id>/', posts_detail, name= 'detail'), 
    path('<int:id>/edit', posts_update, name= 'update'),
    path('<int:id>/delete', posts_delete),
]