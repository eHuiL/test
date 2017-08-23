# -*- coding: utf-8 -*-
#  把models创建的表，添加到xadmin后台中
import xadmin

from .models import UserInfo, StudentInfo, TeacherInfo, ColRspPsInfo, AdminInfo
from xadmin import views


class BaseSetting(object):
    # 设置后台管理主题
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "教材征订后台管理系统"
    site_footer = "合肥工业大学"
    menu_style = "accordion"


class UserInfoAdmin(object):
    # 在列表页中显示字段
    list_display = ['username', 'password']
    # 在列表页添加搜索功能
    search_fields = ['username', 'password']
    # 在列表页配置过滤器
    list_filter = ['username', 'password']


class StudentInfoAdmin(object):
    list_display = ['StudentID', 'Sname', 'Ssex', 'Sage', 'Sphone', 'Smajor']
    search_fields = ['StudentID', 'Sname', 'Ssex', 'Sage', 'Sphone', 'Smajor']
    list_filter = ['StudentID', 'Sname', 'Ssex', 'Sage', 'Sphone', 'Smajor']


class TeacherInfoAdmin(object):
    list_display = ['TeacherID', 'Tname', 'Tsex', 'Tage', 'Tphone', 'Tmajor']
    search_fields = ['TeacherID', 'Tname', 'Tsex', 'Tage', 'Tphone', 'Tmajor']
    list_filter = ['TeacherID', 'Tname', 'Tsex', 'Tage', 'Tphone', 'Tmajor']


class ColRspInfoAdmin(object):
    list_display = ['SecreID', 'Sename', 'Sesex', 'Seage', 'Sephone', 'Semajor']
    search_fields = ['SecreID', 'Sename', 'Sesex', 'Seage', 'Sephone', 'Semajor']
    list_filter = ['SecreID', 'Sename', 'Sesex', 'Seage', 'Sephone', 'Semajor']


class AdminInfoAdmin(object):
    list_display = ['AdminID', 'Aname', 'Asex', 'Aage', 'Aphone']
    search_fields = ['AdminID', 'Aname', 'Asex', 'Aage', 'Aphone']
    list_filter = ['AdminID', 'Aname', 'Asex', 'Aage', 'Aphone']


xadmin.site.register(UserInfo, UserInfoAdmin)
xadmin.site.register(StudentInfo, StudentInfoAdmin)
xadmin.site.register(TeacherInfo, TeacherInfoAdmin)
xadmin.site.register(ColRspPsInfo, ColRspInfoAdmin)
xadmin.site.register(AdminInfo, AdminInfoAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
