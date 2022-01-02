from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home_page'),
    path('about/', views.about, name='about_page'),
    path('login/', views.login, name='login'),
    path('search/', views.search, name='search_results'),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),
    path('category/<slug:category_slug>/', views.ShowCategory.as_view(), name='category'),
    path('writer/<int:writer_id>/', views.show_writer, name='writer'),
    path('add_page/', views.AddPage.as_view(), name='add_page'),
]
