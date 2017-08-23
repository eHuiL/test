from django.conf.urls import url
from users import views
from django.views.generic import TemplateView

urlpatterns = [
    # 首页
    url(r'^$', TemplateView.as_view(template_name='firstpage.html'), name="firstpage"),
    # url(r'^$', views.login, name='login'),
    # 登录
    url(r'^users/login/$', views.login, name='login'),
    # 注册
    url(r'^users/register/$', views.regist, name='regist'),
    # 菜单页
    url(r'^users/index/$', views.index, name='index'),
    # 退出登录
    url(r'^users/logout/$', views.logout, name='logout'),
    # 个人信息
    url(r'^users/psinfo/$', views.pvshow, name='pvinfo'),
    # 提交留言信息
    url(r'^users/leavemessage/$', views.leavemessage, name='leavemessage')
]
