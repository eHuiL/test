from django.conf.urls import url
from django.views.generic import TemplateView
from operations import views

urlpatterns = [
    # 显示教材征订表数据
    url(r'^operations/bookinfo/$', views.show, name="show"),
    # 修改教材征订表数据
    url(r'^operations/update/$', views.update, name="update"),
    # 增加教材征订表数据
    url(r'^operations/add/$', views.add, name="add"),
    # 删除叫教材征订表数据
    url(r'^operations/delete/$', views.delete, name="delete"),
    # 查看书目
    url(r'^operations/books/$', views.showbooks, name="showbooks"),
    # 留言信息
    url(r'^userinfo/$', TemplateView.as_view(template_name='leavemessage.html'), name="liuyan"),
]
