from django.urls import path
from sns.views import SNSLV, SNSDV

app_name = 'sns'
urlpatterns = [
    path('', SNSLV.as_view(), name='index'),
    path('<int:pk>/', SNSDV.as_view(), name='detail'),
]