from django.urls import path
from clock.views import NoticeListAPI

urlpatterns = [
    path('api/notice/', NoticeListAPI.as_view()),
]
