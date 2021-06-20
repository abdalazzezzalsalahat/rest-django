from django.urls import path
from .views import SkyList, SkyDetail

urlpatterns = [
    path('', SkyList.as_view(), name='sky_list'),
    path('<int:pk>/', SkyDetail.as_view(), name='sky_detail'),
]



