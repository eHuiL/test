from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.shortcuts import render_to_response
from operations import models
from django.views.decorators.csrf import csrf_exempt
from operations.models import BookOrder


class BookForm(forms.Form):
    number = forms.CharField(label='编号', max_length=30)
    CourseID = forms.CharField(label='课程号', max_length=30)
    amount = forms.CharField(label='数量', max_length=30)
    term = forms.CharField(label='学期', max_length=30)
    major = forms.CharField(label='专业', max_length=30)

@csrf_exempt
def show(request):
    global book_list
    book_list = models.BookOrder.objects.all()
    global bi
    if request.method == "POST":
        bi = request.POST['id']
    username = request.COOKIES.get('username', '')
    if username == 'teacher':
        return render(request, 'tchshow.html', {'book_list': book_list})
    elif username == '2014213382':
        return render(request, 'stushow.html', {'book_list': book_list})
    elif username == 'colrsp':
        return render(request, 'colrspshow.html', {'book_list': book_list})
    elif username == 'admin':
        return render(request, 'copy.html', {'book_list': book_list})
    else:
        return HttpResponse("error!")



@csrf_exempt
def add(request):
    if request.method == 'POST':
        bf = BookForm(request.POST)
        if bf.is_valid():
            number = bf.cleaned_data['number']
            courseID = bf.cleaned_data['CourseID']
            amount = bf.cleaned_data['amount']
            term = bf.cleaned_data['term']
            major = bf.cleaned_data['major']
            models.BookOrder.objects.create(Number=number, CourseID=courseID,
                                            Amount=amount, Term=term, Major=major)
            # return HttpResponse("success")
            response = HttpResponseRedirect('/operations/bookinfo/')
            response.set_cookie('number', number, 3600)
            return response
    else:
        bf = BookForm()
    return render_to_response('add.html', {'bf': bf}, )

#修改
@csrf_exempt
def update(req):
    if req.method == 'POST':
        id = bi
        bookid = req.POST['bookid']
        courseid = req.POST['courseid']
        booknumber = req.POST['booknumber']
        term = req.POST['term']
        major = req.POST['major']
        book = BookOrder()
        book.Number = id
        book.Number = bookid
        book.CourseID = courseid
        book.Amount = booknumber
        book.Term = term
        book.Major = major
        book.save()
        return HttpResponse()
    return render_to_response('update.html',{'bi':bi})


# @csrf_exempt
# def update(request):
#     if request.method == 'POST':
#         bf = BookForm(request.POST)
#         if bf.is_valid():
#             number = bf.cleaned_data['number']
#             courseID = bf.cleaned_data['CourseID']
#             amount = bf.cleaned_data['amount']
#             term = bf.cleaned_data['term']
#             major = bf.cleaned_data['major']
#             models.BookOrder.objects.filter(Number=number).update()
#             # return HttpResponse("success")
#             response = HttpResponseRedirect('/operations/bookinfo/')
#             response.set_cookie('number', number, 3600)
#             return response
#     else:
#         bf = BookForm()
#     return render_to_response('update.html', {'bf': bf}, )
#     # if request.method == 'POST':
#     #     number = request.POST['up_Number']
#     #     courseID = request.POST['up_CourseID']
#     #     amount = request.POST['up_Amount']
#     #     term = request.POST['up_Term']
#     #     major = request.POST['up_Major']
#     #     book_list = models.BookOrder.objects.filter(Number=number).update(Number=number,
#     #                                                                       CourseID=courseID, Amount=amount, Term=term,
#     #                                                                       Major=major)
#     #     return render(request, 'update.html', {'book_list': book_list})


# @csrf_exempt
# def delete(request):
#     if request.method == 'POST':
#         bf = BookForm(request.POST)
#         if bf.is_valid():
#             number = bf.cleaned_data['number']
#             courseID = bf.cleaned_data['CourseID']
#             amount = bf.cleaned_data['amount']
#             term = bf.cleaned_data['term']
#             major = bf.cleaned_data['major']
#             models.BookOrder.objects.all().delete()
#             models.BookOrder.objects.filter(Number=number, CourseID=courseID,
#                                             Amount=amount, Term=term, Major=major).delete()
#             # return HttpResponse("success")
#             response = HttpResponseRedirect('/operations/bookinfo/')
#             response.set_cookie('number', number, 3600)
#             return response
#     else:
#         bf = BookForm()
#     return render_to_response('delete.html', {'bf': bf}, )


@csrf_exempt
def delete(request):
    if request.method == 'POST':
        bookid = request.POST['id']
        book = BookOrder()
        book.Number = bookid
        book.delete()
        print(bookid)
        bf = BookForm(request.POST)
        # models.BookOrder.objects.filter(Numcber=bookid).delete()
        print(bookid)
        # return HttpResponse("success")
        response = HttpResponseRedirect('/operations/bookinfo/')
        response.set_cookie('number', bookid, 3600)
        return response
    return render_to_response('copy.html', {'book_list': book_list}, )


def showbooks(request):
    books_list = models.BookInfo.objects.all()
    return render(request, 'showbooks.html', {'books_list': books_list})
