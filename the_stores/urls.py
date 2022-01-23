#from django.conf.urls import include,url
from django.contrib import admin
from racks import views
from django.urls import include, re_path

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', views.index, name='index'),
    re_path(r'^item/(?P<id>\d+)/', views.item_detail, name='item_detail'),
    #url(r'^admin/', include(admin.site.urls)),
]

