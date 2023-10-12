from django.urls import path
from django.contrib.auth.decorators import login_required
from posts.views import (CreatPostView,CreatePostGenericView,PostListGenericView,PostDetailGenericView
        ,PostDetailGenericView,UpdatePostGenericView,DeletePostGenericView)


urlpatterns = [

    path('creat',CreatPostView.as_view(), name='posts.create'),
    path('create/generic',CreatePostGenericView.as_view(), name='posts.create' ),
    path('', PostListGenericView.as_view(), name='posts.index'),
    path('<int:pk>', PostDetailGenericView.as_view(), name='posts.show'),
    path('<int:pk>/edit',login_required(login_required(UpdatePostGenericView.as_view())), name='posts.edit'),
    path('<int:pk>/delete', login_required(DeletePostGenericView.as_view()), name='posts.delete'),


]

