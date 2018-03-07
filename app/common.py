from .models import Category, Article, Tag


def sidebar(request):
    category_list = Category.objects.all()  # 所有类型

    article_rank = Article.objects.all().order_by('-view')[0:5]  # 文章排行

    rank_num = range(1,6)  # 排名

    tag_list = Tag.objects.all()  # 标签

    return {
        'category_list': category_list,
        'article_rank': article_rank,
        'rank_num': rank_num,
        'tag_list': tag_list,
    }

if __name__ == '__main__':
    pass