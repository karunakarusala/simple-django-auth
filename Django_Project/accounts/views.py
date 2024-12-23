from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == 'POST' :
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']

        if password == confirm_password:   
            if User.objects.filter(username=username).exists():
               messages.info(request,"user name already taken")
               return render(request,'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exits")
                return render(request,'register.html')
            else:
                user  = User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save();          
                return render(request,'login.html')
        else:
            
            messages.info(request, "password didnt match")
            return render(request,'register.html')
        return redirect('/')
    else:
        
        return render(request,'register.html')

def login (request):

    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']
       user = auth.authenticate(username=username,password=password)
       if not password:
            messages.info(request, "Password field cannot be empty")
            return render(request, 'login.html')
       if user is not None : 
             
                print(user,"usernae")          
                auth.login(request,user)
                return redirect('/')           
       else:
           messages.info(request,"username and password didnt match")
           return render(request,'login.html')
 
    else :
        return render(request,'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')   