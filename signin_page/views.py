
from django.shortcuts import redirect, render
from django.http import HttpResponse
from requests import session
from signup_page.models import signup_detail

# Create your views here.

def signin(request):

    if request.method=="POST":
        username=request.POST['uname']
        password=request.POST['pass1'] 
        if signup_detail.objects.filter(uname=username,pass1=password).exists():
            user_data=signup_detail.objects.get(uname=username)

           
            request.session['uname']=user_data.uname
            
           
            
            
            return redirect('/we/welcome')

        else:
            return render(request,'signin/signin_page.html',{'message':'Incorrect Username Or Password'})


    return render(request,'signin/signin_page.html')
