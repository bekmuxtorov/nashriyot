from django.shortcuts import render
from django.db.models import Q
from pages.models import Articles
from .const import Const
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView, CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.
def MainPagesView(request):
    categories = dict(Const.categories)
    context = {'categories': categories}
    return render(request, 'main.html', context)
    
def AllPagesView(request):
    if request.method == "POST":
        title = request.POST.get('title')
        image = request.POST.get('image')
        category_id = request.POST.get('category')
        body = request.POST.get('body')
        category = dict(Const.categories)[category_id]
        Articles(title=title, image=image, category=category_id, body=body).save()

    all_articles = list(Articles.objects.all()[::-1])
    article_0 = all_articles[0]
    article_1 = all_articles[1]
    article_2 = all_articles[2]
    article_3 = all_articles[3]

    articles_mahalliy = Articles.objects.filter(category='1')[::-1]
    articles_dunyo = Articles.objects.filter(category='2')[::-1]
    articles_dunyo_0 = articles_dunyo[0]

    articles_moliya = Articles.objects.filter(category='3')[::-1]
    articles_moliya_0 = articles_moliya[0]

    articles_sport = Articles.objects.filter(category='4')[::-1]
    articles_fan = Articles.objects.filter(category='5')[::-1]
    articles_fan_0 = articles_fan[0]

    

    categories = dict(Const.categories)
    context = {'categories': categories,
                'articles': all_articles,
                'article_0': article_0,
                'article_1': article_1,
                'article_2': article_2,
                'article_3': article_3,
                'articles_mahalliy': articles_mahalliy,
                'articles_dunyo': articles_dunyo,
                'articles_dunyo_0': articles_dunyo_0,
                'articles_moliya': articles_moliya,
                'articles_moliya_0': articles_moliya_0,
                'articles_sport': articles_sport,
                'articles_fan': articles_fan,
                'articles_fan_0': articles_fan_0,
              }
    return render(request, 'all.html', context)

def ArticleDetailView(request, pk):
    categories = dict(Const.categories)
    object = Articles.objects.get(pk=pk)
    articles_ = Articles.objects.all()

    blog_object=Articles.objects.get(id=pk)
    blog_object.blog_view=blog_object.blog_view+1
    blog_object.save()

    context = {'object': object,
                'articles_': articles_  ,
                'categories': categories,
              }

    return render(request, 'article_detail.html', context)


class ArticleCreateView(CreateView, LoginRequiredMixin):
    model = Articles
    template_name = 'article_new.html'
    fields = ['title', 'body','image','category' ]
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = dict(Const.categories)
        context['categories'] = categories
        
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(). form_valid(form)  

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user  

def ArticleCategoryListView(request, pk):
    categories = dict(Const.categories)
    category = dict(Const.categories)[pk]
    object_list = list(Articles.objects.filter(category=pk)[::-1])
    if len(object_list) > 4:
        object_list_0 = object_list[0]
        object_list_1 = object_list[1]
        object_list_2 = object_list[2]
        object_list_3 = object_list[3]

        context = {
            "object_list": list(object_list),
            "category": category,
            'categories': categories,
            'object_list_0': object_list_0,
            'object_list_1': object_list_1,
            'object_list_2': object_list_2,
            'object_list_3': object_list_3
        }

    else:
        context = {
            "object_list": list(object_list),
            "category": category,
            'categories': categories,
        }


    return render(request, "category_filter.html", context)

# delete, update
class ArticleDeleteView(DeleteView):
    model = Articles
    template_name = 'article_delete.html'
    success_url = reverse_lazy('all')

class ArticleUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Articles
    fields = ['title', 'body','image','category' ]
    template_name = 'article_update.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = dict(Const.categories)
        context["categories"] = categories
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(). form_valid(form)

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user 

# QIDIRUV QISMI UCHUN
class SearchResultsListView(ListView):
    model = Articles
    context_object_name = 'object_list'
    template_name = 'search_results.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Articles.objects.filter(
            Q(title__icontains=query) | Q(title__icontains=query)
        )
    
    