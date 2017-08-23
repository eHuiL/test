# _*_ encoding:utf-8 _*_
from django.db import models

from users.models import TeacherInfo


# 学院教材征订表
class BookOrder(models.Model):
    Number = models.CharField(primary_key=True, max_length=30, null=False, verbose_name=u"编号")
    CourseID = models.CharField(max_length=10, verbose_name=u"课程号", null=False)
    Amount = models.IntegerField(verbose_name=u"数量", null=False)
    Term = models.CharField(max_length=30, verbose_name=u"学期")
    Major = models.CharField(max_length=30, verbose_name=u"专业", null=False)

    class Meta:
        verbose_name = u"学院教材征订表"
        verbose_name_plural = verbose_name
        db_table = "colodform"

    def __str__(self):
        return self.Number


# # 课程信息表
# # ForeignKey中的to_field制定关联的字段，默认关联对象的主键
# class CourseForm(models.Model):
#     CourseID = models.ForeignKey(BookOrder, to_field=BookOrder.CourseID, primary_key=True, null=False,
#                                  verbose_name=u"课程号")
#     TeacherID = models.ForeignKey(TeacherInfo, to_field=TeacherInfo.TeacherID, max_length=10, null=False,
#                                   verbose_name=u"教师id")
#     Cname = models.CharField(max_length=30, verbose_name=u"课程名")
#
#     class Meta:
#         verbose_name = u"课程信息表"
#         verbose_name_plural = verbose_name
#         db_table = "courseform"
#
#     def __str__(self):
#         return self.Cname
#
#
# # 学院信息表
# class CollegeInfor(models.Model):
#     Collname = models.CharField(max_length=10, null=False, verbose_name=u"学院名")
#     Major = models.ForeignKey(max_length=10, primary_key=True, null=False, verbose_name=u"专业")
#
#     class Meta:
#         verbose_name = u"学院信息表"
#         verbose_name_plural = verbose_name
#         db_table = "colinfor"
#
#     def __str__(self):
#         return self.Collname
#
#
# 书籍信息表
class BookInfo(models.Model):
    Number = models.ForeignKey(BookOrder, primary_key=True, max_length=30, null=False, verbose_name=u"编号")
    Bookname = models.CharField(max_length=30, null=False, verbose_name=u"书名")
    Press = models.CharField(max_length=30, verbose_name=u"出版社")
    Author = models.CharField(max_length=30, verbose_name=u"作者")
    Edition = models.CharField(max_length=10, null=False, verbose_name=u"版次")
    Price = models.FloatField(max_length=30, null=False, verbose_name=u"单价")

    class Meta:
        verbose_name = u"书籍信息表"
        verbose_name_plural = verbose_name
        db_table = "bookinfo"

    def __str__(self):
        return self.Bookname
