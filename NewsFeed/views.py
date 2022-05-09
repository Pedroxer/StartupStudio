import math

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from NewsFeed.models import NewsArticle, Comment
from UserSystem.models import CustomUser


class IndexView(generic.ListView):
    template_name = 'NewsFeed/index.html'
    context_object_name = 'latest_article_list'

    def get_queryset(self):
        """Return the last ten published articles."""
        return NewsArticle.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


# Create your views here.


class DetailView(generic.DetailView):
    model = NewsArticle
    template_name = 'NewsFeed/detail.html'

    def get_queryset(self):
        """
        Excludes any articles that aren't published yet.
        """
        return NewsArticle.objects.filter(pub_date__lte=timezone.now())


def send_comment(request, article_id):
    article = get_object_or_404(NewsArticle, pk=article_id)
    user = get_object_or_404(CustomUser, pk=request.POST['user_id'])
    q = Comment(article=article, user_id=user, pub_datetime=timezone.now(), comment_text=request.POST['comment_text'])
    q.save()
    return HttpResponseRedirect(reverse('NewsFeed:detail', args=(article_id,)))


def index_using_culling(request, page_num='1'): #Возможно, это можно переделать через ListView c Пейджингом
    all_articles = NewsArticle.objects.filter(pub_date__lte=timezone.now())
    articles_count = all_articles.count()
    latest_article_list = all_articles[(int(page_num) - 1) * 5:int(page_num) * 5]

    for item in latest_article_list:
        item.news_text = item.news_text[:item.news_main_text_culling]
    context = {'latest_article_list': latest_article_list}

    total_pages = int(math.ceil(articles_count / 5))
    page_numbers = [x for x in range(1, total_pages + 1)][:7] #manual pagination
    if total_pages > 8:                                       #TODO: fix pagination for 10 pages and mode (Maybe use auto pagination as well?)
        page_numbers.append(total_pages)
    context['page_numbers'] = page_numbers

    return render(request, 'NewsFeed/index.html', context)

# add the reference to the last page
    # Код надо наверное отрефакторить?

def tag_filtered(request, tag_name, page_num='1'):
    all_articles = NewsArticle.objects.filter(tags__tag_name=tag_name).filter(pub_date__lte=timezone.now())
    articles_count = all_articles.count()
    latest_article_list = all_articles[(int(page_num) - 1) * 5:int(page_num) * 5]
    for item in latest_article_list:
        item.news_text = item.news_text[:item.news_main_text_culling]
    context = {'latest_article_list': latest_article_list}

    total_pages = int(math.ceil(articles_count / 5))
    page_numbers = [x for x in range(1, total_pages + 1)][:7]
    if total_pages > 8:
        page_numbers.append(total_pages)  # add the reference to the last page
    context['page_numbers'] = page_numbers #Код надо наверное отрефакторить?

    return render(request, 'NewsFeed/index.html', context)
