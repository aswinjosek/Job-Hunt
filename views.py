from django.shortcuts import render,redirect
from django.http import HttpResponse, request,JsonResponse
from .models import Admindb
from django.contrib.auth.models import User,auth


# Create your views here.


def index(request):
    return render(request,'index.htm')

def admin1(request):
    return render(request,'admin1.htm')

def adminreg(request):
    data=dict()
    if request.method=='POST':
        adminobj=Admindb()
        adminobj.firstname=request.POST.get('firstname')
        adminobj.lastname=request.POST.get('lastname')
        adminobj.username=request.POST.get('username')
        adminobj.email=request.POST.get('email')
        adminobj.password=request.POST.get('password')
        adminobj.confirmpassword=request.POST.get('confirmpassword')
        if adminobj.password == adminobj.confirmpassword:
            if Admindb.objects.filter(username=adminobj.username).exists():
                print("user name taken")
            elif Admindb.objects.filter(email=adminobj.email).exists():
                print("email taken")
            else:
                adminobj.save()
                data['message']="Registred succesfully"
                data['error']=1
                print('user created')
                return JsonResponse(data)
        else:
            data['message']="password not matching"
            data['error']=1
            print('user not created')
            #return JsonResponse(data)
            
            
            

def admintable(request):
    datas=Admindb.objects.all()
    return render(request,'admintable.htm',{'datas':datas})
   

def userdelete(request,dataid):
    #data=dict()
    #if request.method=='POST':
        Admindb.objects.filter(id=dataid).delete()
        return redirect('admintable')
    #data['message']="Deleted succesfully"
    #data['error']=1
    #return JsonResponse(data)
     
    

def adminupdate(request,dataid):
    datas=Admindb.objects.filter(id=dataid)
    return render(request,'adminupdate.htm',{'datas':datas })
    
    
    
def updating(request,dataid):
    #data=dict()
    #if request.method=='POST':
        "dataid=request.POST.get()"
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        user=Admindb.objects.filter(id=dataid).update(firstname=firstname,lastname=lastname,username=username,email=email,password=password,confirmpassword=confirmpassword)
    #data['message']="Updated succesfully"
    #data['error']=1
    #return JsonResponse(data)
        return redirect('admintable')
    

def candidatetable(request):
    return render(request,'candidatetable.htm')

def login(request):
    adminobj=Admindb()
    if request.method=='POST':
        adminobj.username=request.POST.get('username')
        adminobj.password=request.POST.get('password')
        adminobj.user=auth.authenticate(username = adminobj.username,password = adminobj.password)
        if adminobj.user is not None:
            auth.login(request,adminobj.user)
            return redirect('index')
        else:
            return redirect('login')
        
    else:
        return render(request,'login.htm')


    