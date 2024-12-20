# Routers provide an easy way of automatically determining the URL conf.

# from django.urls import include, path
# from api2.views import CommentViewSet, PostViewSet, UserViewSet
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'post', PostViewSet)
# router.register(r'comment', CommentViewSet)

# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.

# urlpatterns = [
#     path('', include(router.urls)),
# ]
from django.urls import path
from api2 import views

urlpatterns = [
    # path('post/', views.PostListAPIView.as_view(),name='post-list'),
    # path('post/<int:pk>/', views.PostRetrieveAPIView.as_view(),name='post-detail'),
    # path('comment/', views.CommentCreateAPIView.as_view(),name='comment-create'),
    # path('post/<int:pk>/like/', views.PostLikeAPIView.as_view(),name='post-like'),
    # path('catetag/', views.CateTagAPIView.as_view(), name='catetag'),

    path('post/', views.PostViewSet.as_view(actions = {
        'get': 'list',
    }),name='post-list'),
    path('post/<int:pk>/', views.PostViewSet.as_view(actions = {
        'get': 'retrieve',
    }),name='post-detail'),
    path('post/<int:pk>/like/', views.PostViewSet.as_view(actions = {
        'get': 'like',
    }),name='post-like'),
    
    path('comment/', views.CommentViewSet.as_view(actions = {
        'post': 'create',
    }),name='comment-list'),

    path('catetag/', views.CateTagAPIView.as_view(), name='catetag'),

]
