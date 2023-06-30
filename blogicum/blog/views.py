import datetime
from django.shortcuts import render, get_object_or_404
from blog.models import Category, Post


def published_post(request):
    return (
        request.
        filter(
            is_published=True, category__is_published=True
        ).
        filter(pub_date__date__lte=datetime.datetime.today()))


def index(request):
    template_name = 'blog/index.html'
    post_list = Post.objects.all()
    context = {
        'post_list': published_post(post_list,)[:5]
    }
    return render(request, template_name, context)


def post_detail(request, id):
    template_name = 'blog/detail.html'
    post = Post.objects.all()
    context = {
        'post': get_object_or_404(published_post(post,), pk=id)
    }
    return render(request, template_name, context)


def category_posts(request, category_slug):
    category = get_object_or_404(Category.objects.all(), slug=category_slug,
                                 is_published=True)
    return render(request, 'blog/category.html', {
        'category': category,
        'post_list': published_post(category.posts,)},)
