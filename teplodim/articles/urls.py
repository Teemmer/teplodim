from django.conf.urls import url
from django.urls import path
from django.views.generic import RedirectView

from .views import (
    HomeView,
    AboutView,
    ContactView,
    ArticleDetailView,
    add_article_view,
    ServicesView,
    ContactsView
)

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('articles/<int:article_id>/', ArticleDetailView.as_view(), name='article_detail'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('services/', ServicesView.as_view(), name='services'),
    path('about/', AboutView.as_view(), name='about'),
    path('edit_panel/', add_article_view, name='panel'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico'), name='favicon'),
    path('', HomeView.as_view(), name='home'),
]
