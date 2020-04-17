# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect

# Create your views here.

list = [
    {"item_name":"snap","finished": True}
]

def home(request):
    if request.method == "POST":
        if request.POST.get("item_name") != "":
            item_name = request.POST.get("item_name")
            list.append({'item_name':item_name, 'finished':False})
            return render(request, "home.html", {"content":list})
        else:
            return render(request, "home.html", {"content":list,"warning":"please don't submit empty strings."})
    else:
        return render(request, "home.html",{"content":list})

def about(request):
    return render(request, "about.html")

def edit(request, id):
    if request.method == "GET":
        content = {"item_name": list[int(id) - 1]['item_name']}
        return render(request, "edit.html", content)
    elif request.method == "POST":
        if request.POST["item_name_changed"] == "":
            return render(request, "edit.html", {"warning":"please don't submit empty strings."})
        else:
            list[int(id) - 1]['item_name'] = request.POST["item_name_changed"]
            return redirect("/")

def delete(request, id):
    list.pop(int(id)-1)
    return redirect("/")

def finished(request, id):
    if (list[int(id)-1]['finished']):
        list[int(id)-1]['finished']=False
    else:
        list[int(id) - 1]['finished']=True
    return redirect("/")