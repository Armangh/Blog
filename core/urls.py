from django.urls import path

from .views import (CreatePost, DetailPost, DeletePost,
                    CreateComment, CreateTag, DetailTag,
                    DeleteTag)

urlpatterns = [
    # /post/create/ create_post
    path('post/create/',
        CreatePost.as_view(),
        name='create_post'),

    # /post/1/ detail_post
    path('post/<int:pk>/',
        DetailPost.as_view(),
        name='detail_post'),

    # /post/delete/1
    path('post/<int:pk>/delete/',
        DeletePost.as_view(),
        name='delete_post'),

    # /post/1/comment/
    path('post/<int:pk>/comment/',
        CreateComment.as_view(),
        name='create_comment'),

    # /tag/create/
    path('tag/create/',
        CreateTag.as_view(),
        name='create_tag'),

    # /tag/1/
    path('tag/<int:pk>/',
        DetailTag.as_view(),
        name='detail_tag'),

    # /tag/1/delete
    path('tag/<int:pk>/delete',
        DeleteTag.as_view(),
        name='delete_tag'),
]
