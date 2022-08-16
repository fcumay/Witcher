from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import *

menu = [{'title': "About", 'url_name': 'about'},
        {'title': "Add article", 'url_name': 'add_page'},
        {'title': "Contact", 'url_name': 'contact'},
        {'title': "Enter", 'url_name': 'login'}
        ]



class MonstersHome(ListView):
    model = Monsters
    template_name = 'witcherr/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'WBestiary'
        context['cat_selected'] = 0
        return context

# def index(request):
#     posts = Monsters.objects.all()
#     cats = Category.objects.all()
#
#     context = {
#         'posts': posts,
#         'cats': cats,
#         'menu': menu,
#         'title': "WBestiary",
#         'cat_selected':0,
#     }
#     return render(request, 'witcherr/index.html', context=context)

def about(request):
    return render(request, 'witcherr/about.html', {'menu': menu, 'title': 'About'})

def addpage(request):
    return HttpResponse("Soon")

def contact(request):
    return HttpResponse("Soon")

def login(request):
    return HttpResponse("Soon")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')

# def show_post(request, post_id):
#     post = get_object_or_404(Monsters, pk=post_id)
#
#     context = {
#         'post': post,
#         'manu':menu,
#         'title':post.title,
#         'cat_selected': post.cat_id,
#     }
#
#     return render(request, 'witcherr/post.html', context=context)

class ShowPost(DetailView):
    model = Monsters
    template_name = 'witcherr/post.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        return context


class WitcherrCategory(ListView):
    model = Monsters
    template_name = 'witcherr/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Monsters.objects.filter(cat__id=self.kwargs['cat_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'WCat - ' + str(context['posts'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].cat_id
        return context



# def show_category(request, cat_id):
#     posts = Monsters.objects.filter(cat_id=cat_id)
#     cats = Category.objects.all()
#
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {
#         'posts':posts,
#         'cats':cats,
#         'menu':menu,
#         'title':'WCAtegories',
#         'cat_selected': cat_id,
#     }
#
#     return render(request, 'witcherr/index.html', context=context)

