from django import template
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

register = template.Library()
# 这是定义模板标签要用到的

@register.simple_tag(takes_context=True)
def paginate(context, object_list, page_count):
    context['count'] = object_list.count
    paginator = Paginator(object_list, page_count)
    page = context['request'].GET.get('page')

    try:
        object_list = paginator.page(page)
        context['current_page'] = int(page)

    except PageNotAnInteger:
        object_list = paginator.page(1)
        context['current_page'] = 1
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)
        context['current_page'] = paginator.num_pages

    context['article_list'] = object_list
    context['last_page'] = paginator.num_pages
    context['first_page'] = 1
    return ''  # 必须加这个，否则首页会显示个None

