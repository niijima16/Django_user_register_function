from typing import List

from django.shortcuts import render, HttpResponse, redirect
from app01.models import UserInfo, Department

import requests


# Create your views here.

def index(request):
    return HttpResponse("hello, thankyou. thankyou very much.")


def tpl(request):
    name = "SkadiP"
    roles = ["manager", "CEO", "Security"]
    user_info = {"name": "Skadi", "salary": 100000, "role": "CTO"}
    data_list = [{"name": "Skadi", "salary": 100000, "role": "CTO"},
                 {"name": "Mikazuki", "salary": 100000, "role": "CTO"},
                 {"name": "aho", "salary": 100000, "role": "CTO"}
                 ]
    return render(request, "tpl.html",
                  {"n1": name, "n2": roles, "n3": data_list})


def news(request):
    return render(request, 'news.html')


def somethings(req):
    print(req.method)
    print(req.GET)
    print(req.POST)
    # return HttpResponse("aaa")
    # return render(req, 'somethings.html', {"aaa": "coming"})
    return redirect("https://www.google.com")


def login(req):
    if req.method == "GET":
        return render(req, "login.html")

    username = req.POST.get("user")
    passwd = req.POST.get("pwd")

    if username == 'root' and passwd == 'qwe123':
        return redirect(
            'https://www.bilibili.com/video/BV1rT4y1v7uQ?p=41&vd_source=47cb68c4da424242be48edd4673d5d81')

    return render(req, "login.html",
                  {"error_msg": "ユーザーが存在しないもしくわパスワードが間違えている"})


def orm(req):
    # Department.objects.create(title="セールス部門")
    # Department.objects.create(title="OA部門")
    # Department.objects.create(title="HR部門")
    #
    # UserInfo.objects.create(name="Skadi",passwd='asdqwe',age=18)
    # UserInfo.objects.filter(id=2).delete()
    # Department.objects.all().delete()
    # data_list = UserInfo.objects.all()
    # for obj in data_list:
    #     print(obj.id, obj.name, obj.passwd, obj.age)
    UserInfo.objects.filter(id=4).update(age=22)
    return HttpResponse("成功")


# ###############################################
# 　ユーザー管理機能

# 1.データ表示ページ
def user_admin(req):
    data_list = UserInfo.objects.all()

    print(data_list)

    return render(req, "user_admin.html", {"data_list": data_list})


# 2.ユーザー追加ページ
def user_add(req):
    if req.method == "GET":
        return render(req, "user_add.html")
    user = req.POST.get("user")
    passwd = req.POST.get("passwd")
    age = req.POST.get("age")

    UserInfo.objects.create(name=user, passwd=passwd, age=age)

    return redirect("/user/admin/")


# 3.ユーザー削除機能
def user_delete(req):
    nid = req.GET.get('nid')
    UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/admin/")
