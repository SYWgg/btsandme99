from django.shortcuts import render
from django.views.generic import ListView, DetailView
from btsprofile.models import BTSprofile_TBL

# Create your views here.
class BTSprofile_TBLLV(ListView):
    model = BTSprofile_TBL
    
class BTSprofile_TBLDV(DetailView):
    model = BTSprofile_TBL
