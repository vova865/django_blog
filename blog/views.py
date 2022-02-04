from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import AddPostForm, RegisterUserForm, LoginUserForm
from .models import Article, Category


class HomePage(ListView):
    """Главная страница сайта."""
    model = Article
    template_name = 'blog/home_page.html'

    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['popular_post'] = Article.objects.get(pk=1)
        context['cats'] = Category.objects.all()
        return context


class ShowArticles(ListView):
    """Показывает список статей по категориям."""
    paginate_by = 3
    model = Article
    template_name = 'blog/list_articles.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].category)
        return context

    def get_queryset(self):
        return Article.objects.filter(category__slug=self.kwargs['category_slug'])


class ShowPost(DetailView):
    """Показывает пост."""
    model = Article
    template_name = 'blog/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'content'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Пост'
        return context


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница, которую вы ищите, не найдена!</h1>')


def about(request):
    context = {
        'title': 'О проекте',
    }
    return render(request, 'blog/about.html', context=context)


class AddPage(LoginRequiredMixin, CreateView):
    """Добавление новой записи."""
    form_class = AddPostForm
    template_name = 'blog/add_page.html'
    success_url = reverse_lazy('home_page')
    login_url = reverse_lazy('login')

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        return context


class RegisterUser(CreateView):
    """Регистрация пользователя."""
    form_class = RegisterUserForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('home_page')

    def get_context_data(self, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home_page')


class LoginUser(LoginView):
    """Вход пользователя."""
    form_class = LoginUserForm
    template_name = 'blog/login.html'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context

    def get_success_url(self):
        return reverse_lazy('home_page')


def logout_user(request):
    logout(request)
    return redirect('home_page')


def search(request):
    return HttpResponse('<h1>Страница поиска</h1>')


def show_writer(request, writer_id):
    return HttpResponse(f"Отображение писателя с id = {writer_id}")
