from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField

# 临时笔记
# auto_now_add : 创建时间戳，不会被覆盖
# auto_now : 自动将当前时间覆盖之前时间
# python3 用 __str__ python2 用 __unicode__

# Create your models here.


# 测试表
class Test(models.Model):
    name = models.CharField(max_length=20)


# 文章
class Article(models.Model):
    title = models.CharField(u'博客标题', max_length=100)
    category = models.ForeignKey('Category', verbose_name=u'文章类型', on_delete=models.CASCADE)
    pub_date = models.DateTimeField(u'发布日期', auto_now_add=True, null=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)
    #content = models.TextField(u'正文内容', blank=True, null=True)
    content = RichTextUploadingField(u'博客内容', null=True, blank=True)
    abstract = models.CharField(u'文章摘要', max_length=100, null=True, help_text='可选项, 若为空格则摘取正文前100个字符')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'作者', on_delete=models.CASCADE)
    view = models.BigIntegerField(u'阅读数', default=0)
    comment = models.BigIntegerField(u'评论数', default=0)
    picture = models.ImageField(u'标题图片地址', upload_to='uploadImages')
    tag = models.ManyToManyField('Tag', verbose_name='标签集合')

    def __str__(self):
        return self.title

    # 增加阅读数
    def add_view(self):
        self.view += 1
        self.save(update_fields=['view'])

    class Meta:    # 按时间下降排序
        ordering = ['-pub_date']
        verbose_name = u'文章'
        verbose_name_plural = u'文章'


# 文章分类
class Category(models.Model):
    name = models.CharField(u'文章分类', max_length=30)
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    last_mod_time = models.DateTimeField(u'修改时间', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = u'文章类型'
        verbose_name_plural = verbose_name


# 标签云
class Tag(models.Model):
    tag_name = models.CharField(u'标签名', max_length=30)

    def __str__(self):
        return self.tag_name



