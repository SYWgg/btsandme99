from django.shortcuts import render
from django.views.generic import ListView, DetailView
from sns.models import SNS

class SNSLV(ListView):
    model = SNS
class SNSDV(DetailView):
    model = SNS