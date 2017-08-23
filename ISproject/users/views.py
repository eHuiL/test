# _*_ encoding:utf-8 _*_
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.views.decorators.csrf import csrf_exempt
from users.models import UserInfo, StudentInfo, ColRspPsInfo, TeacherInfo, AdminInfo


# 表单
@csrf_exempt
class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())


# 注册
@csrf_exempt
def regist(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            # 获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 添加到数据库
            UserInfo.objects.create(username=username, password=password)
            # 更改一下跳转，可以完善
            return HttpResponse('regist success!!')
    else:
        uf = UserForm()
    return render_to_response('register.html', {'uf': uf}, )


# 登陆
@csrf_exempt
def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            # 获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 获取的表单数据与数据库进行比较
            user = UserInfo.objects.filter(username__exact=username, password__exact=password)
            if user:
                # 比较成功，跳转index
                response = HttpResponseRedirect('/users/index/')
                # 将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username', username, 3600)
                return response
            else:
                # 比较失败，还在login
                return HttpResponseRedirect('/users/login/')
    else:
        uf = UserForm()
    return render_to_response('logincopy.html', {'uf': uf}, )


# 登陆成功
@csrf_exempt
def index(req):
    username = req.COOKIES.get('username', '')
    if username == 'teacher':
        return render_to_response('index.html', {'username': username})
    elif username == '2014213382':
        return render_to_response('stuindex.html', {'username': username})
    elif username == 'admin':
        return render_to_response('admindex.html', {'username': username})
    elif username == 'colrsp':
        return render_to_response('colrspindex.html', {'username': username})
    else:
        # 更改一下跳转，可以完善
        return HttpResponse("log error!")


# 退出
@csrf_exempt
def logout(req):
    response = HttpResponse('logout !!')
    # 清理cookie里保存username
    response.delete_cookie('username')
    # return HttpResponse
    return HttpResponseRedirect('/')


# 个人信息
def pvshow(request):
    tchinfo_list = TeacherInfo.objects.all()
    stuinfo_list = StudentInfo.objects.all()
    colrspinfo_list = ColRspPsInfo.objects.all()
    adminfo_list = AdminInfo.objects.all()
    username = request.COOKIES.get('username', '')
    if username == 'teacher':
        return render(request, 'tchpvinfo.html', {'tchinfo_list': tchinfo_list})
    elif username == '2014213382':
        return render(request, 'stupvinfo.html', {'stuinfo_list': stuinfo_list})
    elif username == 'admin':
        return render(request, 'admpvinfo.html', {'adminfo_list': adminfo_list})
    elif username == 'colrsp':
        return render(request, 'colrspvinfo.html', {'colrspinfo_list': colrspinfo_list})
    else:
        # 更改一下跳转，可以完善
        return HttpResponse("error!")

@csrf_exempt
def leavemessage(request):
    return HttpResponse("提交成功!")
