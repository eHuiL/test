# -*- coding: utf-8 -*-
#  把models创建的表，添加到xadmin后台中
import xadmin

from .models import BookOrder, BookInfo


class BookOrderAdmin(object):
    # 在列表页中显示字段
    list_display = ['Number', 'CourseID', 'Amount', 'Term', 'Major']
    # 在列表页添加搜索功能
    search_fields = ['Number', 'CourseID', 'Amount', 'Term', 'Major']
    # 在列表页配置过滤器
    list_filter = ['Number', 'CourseID', 'Amount', 'Term', 'Major']


class BookInfoAdmin(object):
    list_display = ['Number', 'Bookname', 'Press', 'Author', 'Edition', 'Price']
    search_fields = ['Number', 'Bookname', 'Press', 'Author', 'Edition', 'Price']
    list_filter = ['Number', 'Bookname', 'Press', 'Author', 'Edition', 'Price']


xadmin.site.register(BookOrder, BookOrderAdmin)
xadmin.site.register(BookInfo, BookInfoAdmin)
