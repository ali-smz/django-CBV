from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView , CreateView  , UpdateView , DeleteView 
from .models import Link , Profile
from django.urls import reverse_lazy
# Create your views here.
class LinkListView(ListView):
    model = Link
    # link = Link.objects.all()
    # context = {'link' : link}
    # return render( request , link_list.html , context)
    # it look for a link_list.html


class LinkCreateView(CreateView):
    model = Link
    fields = '__all__'
    success_url = reverse_lazy('link-list')
    # it look for a link_form.html


class LinkUpdateView(UpdateView):
    model = Link 
    fields = ['text' , 'url']
    success_url = reverse_lazy('link-list')
    # it look for a link_form.html

class LinkDeleteView(DeleteView):
    model = Link 
    success_url = reverse_lazy('link-list')
    # it look for a link_confirm_delete.html

def profile_view(request , profile_slug):
    profile = get_object_or_404(Profile , slug = profile_slug)
    links = profile.links.all()
    context = {
        'profile': profile ,
        'links' : links
    }
    return render(request , 'link_plant/profile.html' , context)