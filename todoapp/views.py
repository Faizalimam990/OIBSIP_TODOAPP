from django.shortcuts import render,redirect
from .models import*


def index(request):
    usermo=usertasks.objects.all()
    if request.method=="POST":
        
        udes=request.POST['u_des']
        obj=usertasks(description=udes)
        print("data recieved")
        obj.save()

    return render(request,'index.html',{'usermo':usermo})

def deleteid(request,id):
    data=usertasks.objects.filter(id=id)
    data.delete()
    return redirect('/index')