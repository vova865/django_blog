from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from .forms import AddPostForm
from .models import Article, Category


def home_page(request):
    popular_post = Article.objects.get(pk=1)
    context = {
        'popular_post': popular_post,
        'title': 'Главная страница',
        'posts': Article.objects.all(),
        'cats': Category.objects.all()
    }
    return render(request, 'blog/home_page.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница, которую вы ищите, не найдена!</h1>')


def about(request):
    context = {
        'title': 'О проекте',
    }
    return render(request, 'blog/about.html', context=context)


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'blog/add_page.html'
    success_url = reverse_lazy('home_page')

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        return context


def login(request):
    return HttpResponse('<h1>Авторизация</h1>')


def search(request):
    return HttpResponse('<h1>Страница поиска</h1>')


def show_post(request, post_slug):
    context = {
        'title': 'Пост',
        'post_slug': post_slug,
        'post': get_object_or_404(Article, slug=post_slug),
        'content': Article.objects.get(slug=post_slug),
    }
    return render(request, 'blog/post.html', context=context)


def show_category(request, category_id):
    context = {
        'title': 'Категория',
        'category_id': category_id,
        'cats': Article.objects.all(),
        'posts': Article.objects.filter(category_id=category_id)
    }
    return render(request, 'blog/list_categories.html', context=context)


def show_writer(request, writer_id):
    return HttpResponse(f"Отображение писателя с id = {writer_id}")
