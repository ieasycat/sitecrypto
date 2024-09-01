from django.urls import path
from . import views

urlpatterns = [
    path('', views.CryptoHome.as_view(), name='home'),
    path('network/<slug:net_slug>', views.CryptoNetwork.as_view(), name='network'),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),
    path('addpage/', views.AddPage.as_view(), name='add_page'),
    path('edit/<slug:slug>', views.UpdatePage.as_view(), name='edit_page'),
    path('delete/<slug:slug>', views.DeletePage.as_view(), name='delete_page'),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('contact/', views.ContactPage.as_view(), name='contact'),
    path('search/', views.SearchPost.as_view(), name='search_post'),
]
