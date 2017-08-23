# _*_ encoding:utf-8 _*_
from django.db import models


# 用户表
class UserInfo(models.Model):
    # 定义主键，废除默认的id自增列
    username = models.CharField(primary_key=True, null=False, blank=False, max_length=30, unique=True, verbose_name=u"用户名")
    password = models.CharField(max_length=30, verbose_name=u"密码", null=False)

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name
        db_table = "userform"

    def __str__(self):
        return self.username


# 管理员信息表
class AdminInfo(models.Model):
    AdminID = models.ForeignKey(UserInfo, verbose_name=u"管理员id", primary_key=True, null=False)
    Aname = models.CharField(max_length=30, verbose_name=u"姓名", null=False)
    Asex = models.CharField(max_length=6, verbose_name=u"性别")
    Aage = models.CharField(max_length=4, verbose_name=u"年龄")
    Aphone = models.CharField(max_length=20, verbose_name=u"联系方式")

    class Meta:
        verbose_name = u"管理员信息"
        verbose_name_plural = verbose_name
        db_table = "managerform"

    def __str__(self):
        return self.AdminID


# 学院负责人信息表
class ColRspPsInfo(models.Model):
    SecreID = models.ForeignKey(UserInfo, verbose_name=u"学院负责人id", null=False, primary_key=True)
    Sename = models.CharField(max_length=30, verbose_name=u"姓名", null=False)
    Sesex = models.CharField(max_length=5, verbose_name=u"性别")
    Seage = models.CharField(max_length=4, verbose_name=u"年龄")
    Sephone = models.CharField(max_length=20, verbose_name=u"联系方式")
    Semajor = models.CharField(max_length=30, verbose_name=u"专业", null=False)

    class Meta:
        verbose_name = u"学院负责人信息表"
        verbose_name_plural = verbose_name
        db_table = "colrepform"

    def __str__(self):
        return self.SecreID


# 学生信息表
class StudentInfo(models.Model):
    StudentID = models.ForeignKey(UserInfo, verbose_name=u"学生id", null=False, primary_key=True)
    Sname = models.CharField(max_length=30, verbose_name=u"姓名", null=False)
    Ssex = models.CharField(max_length=5, verbose_name=u"性别")
    Sage = models.CharField(max_length=4, verbose_name=u"年龄")
    Sphone = models.CharField(max_length=20, verbose_name=u"联系方式")
    Smajor = models.CharField(max_length=30, verbose_name=u"专业", null=False)

    class Meta:
        verbose_name = u"学生信息表"
        verbose_name_plural = verbose_name
        db_table = "stuform"

    def __str__(self):
        return self.StudentID


# 教师信息表
class TeacherInfo(models.Model):
    TeacherID = models.ForeignKey(UserInfo, verbose_name=u"教师id", primary_key=True, null=False)
    Tname = models.CharField(max_length=30, verbose_name=u"姓名")
    Tsex = models.CharField(max_length=5, verbose_name=u"性别")
    Tage = models.CharField(max_length=4, verbose_name=u"年龄")
    Tphone = models.CharField(max_length=20, verbose_name=u"联系方式")
    Tmajor = models.CharField(max_length=30, verbose_name=u"专业", null=False)

    class Meta:
        verbose_name = u"教师信息表"
        verbose_name_plural = verbose_name
        db_table = "tchform"

    def __str__(self):
        return self.TeacherID
