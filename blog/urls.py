from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('about/', views.about, name='about_page'),
    path('login/', views.login, name='login'),
    path('search/', views.search, name='search_results'),
    path('post/<slug:post_slug>/', views.show_post, name='post'),
    path('category/<int:category_id>/', views.show_category, name='category'),
    path('writer/<int:writer_id>/', views.show_writer, name='writer'),
    path('add_page/', views.add_page, name='add_page'),
]
