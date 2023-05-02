from django.urls import path 
from btsprofile.views import BTSprofile_TBLLV, BTSprofile_TBLDV

app_name = 'btsprofile'
urlpatterns = [
    path('', BTSprofile_TBLLV.as_view(), name='index'), 
    path('<int:pk>/', BTSprofile_TBLDV.as_view(), name='detail'), 
]