from django.urls import path

from .views import *

urlpatterns = [
    path('', MonstersHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<int:post_id>/', ShowPost.as_view(), name='post'),
    path('category/<int:cat_id>/', WitcherrCategory.as_view(), name='category'),
]