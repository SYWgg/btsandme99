from django.views.generic import ListView, DetailView
from django.views.generic import ArchiveIndexView, YearArchiveView, MonthArchiveView 
from django.views.generic import DayArchiveView, TodayArchiveView

from news.models import Post
from django.views.generic import FormView
from news.forms import PostSearchForm
from django.db.models import Q
from django.shortcuts import render

# Create your views here.

#--- ListView 
class PostLV(ListView): 
    model = Post 
    template_name = 'news/post_all.html' 
    context_object_name = 'posts' 
    paginate_by = 2
    
#--- DetailView 
class PostDV(DetailView): 
    model = Post
    
#--- ArchiveView 
class PostAV(ArchiveIndexView): 
    model = Post 
    date_field = 'modify_dt'
    
class PostYAV(YearArchiveView): 
    model = Post 
    date_field = 'modify_dt' 
    make_object_list = True
    
class PostMAV(MonthArchiveView): 
    model = Post 
    date_field = 'modify_dt'
    
class PostDAV(DayArchiveView): 
    model = Post 
    date_field = 'modify_dt'
    
class PostTAV(TodayArchiveView): 
    model = Post 
    date_field = 'modify_dt'
    
class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'news/post_search.html'
    
    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        post_list = Post.objects.filter(Q(title__icontains=searchWord) | Q(description__icontains=searchWord) | Q(content__icontains=searchWord)).distinct()
        
        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list
        
        return render(self.request, self.template_name, context) 
