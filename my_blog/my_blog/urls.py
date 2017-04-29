"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from article import views as article_views
from article.views import RSSFeed
from account import views as account_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', article_views.home, name='home'),
    url(r'^(?P<id>\d+)/$', article_views.detail, name='detail'),
    url(r'^archives/$', article_views.archives, name = 'archives'),
    url(r'^aboutme/$', article_views.about_me, name = 'about_me'),
    url(r'^tag(?P<tag>\w+)/$', article_views.search_tag, name = 'search_tag'),
    url(r'^search/$', article_views.blog_search, name = 'search'),
    url(r'^feed/$', RSSFeed(), name = "RSS"),
    url(r'^uploadfile/$', article_views.upload_file, name = "upload_file"),
    url(r'^register/$', account_views.register, name = 'register'),
    url(r'^login/', account_views.login_site, name='login'),
    url(r'^logout/', account_views.logout_site, name='logout'),
]
