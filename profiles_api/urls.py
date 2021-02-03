from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
# base_name는 restframework 최신버전에서 basename으로 바뀌었다


urlpatterns =[
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls)), # views.HelloViewSet로 연결한다
]
