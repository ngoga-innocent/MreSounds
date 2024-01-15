from django.shortcuts import get_object_or_404,render,redirect
from django.contrib.auth import get_user_model,authenticate,login
from django.contrib import messages
# Create your views here.
User=get_user_model()
def Home(request):
    return render(request,'Accounts/SignIn.html')
def Signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        phone=request.POST['phone']
        password=request.POST['password']
        password1=request.POST['password1']

        if password==password1:
            user=User.objects.filter(username=username).exists()
            if not user:
                email_check=User.objects.filter(email=email).exists()
                if not email_check:
                    # User.username=username
                    # User.email=email
                    # User.phone=phone
                    # User.password=password

                    
                    saveuser=User.objects.create_user(username=username,email=email,password=password)
                    saveuser.phone=phone
                    saveuser.save()
                    if saveuser:
                        return redirect('login')
                    
                    else:
                        return render(request,'Accounts/Signup.html',{'message':'failed to create your account please try again!!!'})
                return render(request,'Accounts/signup.html',{'message':'Email already used try another email!'})
            return render(request,'Accounts/Signup.html',{'message':'username taken!'})
        return render (request, 'Accounts/Signup.html',{'message':'passwords does not match,please try again'})
    else:
        return render (request, 'Accounts/Signup.html')
    

def Login(request):
    if request.method == 'POST':
        username_or_email = request.POST['username']
        password = request.POST['password']

        if '@' in username_or_email:
            authenticated_user = authenticate(request, email=username_or_email, password=password)
        else:
            authenticated_user = authenticate(request, username=username_or_email, password=password)

        if authenticated_user is not None:
            login(request, authenticated_user)
            return redirect('home')
        else:
            messages.error(request, 'Failed to login. Please check your credentials.')

    return render(request, 'Accounts/Signin.html')