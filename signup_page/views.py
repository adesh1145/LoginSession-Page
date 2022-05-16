
from fileinput import filename
from django.shortcuts import redirect, render
from django.http import HttpResponse
from signup_page.models import signup_detail

# Create your views here.

def signup(request):

    if request.method=="POST":
        fname=request.POST['fname']   
        lname=request.POST['lname']   
       
            
        
        uname=request.POST['uname']   
        email=request.POST['email']   
        pass1=request.POST['pass1']   
        pass2=request.POST['pass2']   
        

        if pass1==pass2:
            if not signup_detail.objects.filter(uname=uname,email_name=email).exists():
               
               
                myuser=signup_detail(fname=fname,lname=lname,uname=uname,email_name=email,pass1=pass1)
                myuser.save() 

                return redirect('/')
            else:
                return render(request,'signup/signup_page.html',{'message':'UserName Or Email Are already Exixts.'})

        else:
            
            return render(request,'signup/signup_page.html',{'message':'Password Does not Match'})







    return render(request,'signup/signup_page.html')
