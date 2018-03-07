from django.contrib import admin
from app.models import Article, Category, Tag

# Register your models here.

admin.site.register([Article, Category, Tag])

