from django.urls import path

from . import views

urlpatterns = [
    path("", views.TopPageView.as_view(), name="top"),
    path("mypage/", views.MyPageView.as_view(), name="mypage"),
]
