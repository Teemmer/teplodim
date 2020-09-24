from django.urls import path

from .views import HomeView, AboutView, ContactView, ArticleDetailView, add_article_view

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('articles/<int:article_id>/', ArticleDetailView.as_view(), name='article_detail'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('edit_panel/', add_article_view, name='panel'),
    path('', HomeView.as_view(), name='home'),
]
