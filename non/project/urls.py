from django.urls import path
from .import views

urlpatterns =[

    path('',views.home, name='home'),
    path('about',views.about, name='about'),
    path('shop',views.shop, name='shop'),
    path('blog',views.blog, name='blog'),
    path('gallery',views.gallery, name='gallery')
]