from django.shortcuts import render, get_object_or_404, reverse
from app.models import Article, Category

# Create your views here.


# 博客首页
def Index(request):
    article_list = Article.objects.all().order_by('-pub_date')[0:5]
    return render(request, 'blog/index.html', {'article_list' : article_list, 'source_id' : 'index'})

# 全部文章
def Blog(request, pk):
    pk = int(pk)
    if pk:
        category_object = get_object_or_404(Category, pk=pk)
        category = category_object.name
        article_list = Article.objects.filter(category_id=pk)
    else:
        # pk 为0时表示全部
        article_list = Article.objects.all()  # 获取全部文章
        category = u''
    return render(request, 'blog/article.html', {'article_list': article_list, 'categroy': category})

# 博文详情
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.add_view()
    return render(request, 'blog/detail.html', {'article': article})

# 关于
def about(request):
    return render(request, 'blog/about.html', {'world': 'hello world'})

# 标签
def tag(request, name):
    article_list = Article.objects.filter(tag__tag_name=name)
    return render(request, 'blog/tag.html', {'article_list': article_list, 'tag': name})

'''
def test(request):
    blog = Article.objects.get(id = 2)
    return render(request, 'blog/blog.html', {'blog' : blog})
'''
