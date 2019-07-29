from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from  django.contrib.auth import  authenticate ,login ,logout
# Create your views here.

def index(request):
    return render(request,'MyApp/index.html')
def register(request):
    return  render(request,'MyApp/register.html')
def myRegister(request):
    Fname=request.POST.get('Fname',False)
    Lname=request.POST.get('Lname',False)
    Email=request.POST.get('Email',False)
    Pass=request.POST.get('Pass',False)
    PassConf=request.POST.get('PassConf',False)
    Phone=request.POST.get('num',False)
    #verifion si le deux mot de pass son bon
    print("PASS ={}\nPassConf={}".format(Pass,PassConf))
    if Pass == PassConf :
        try:
            user=User(username=Fname,last_name=Lname,email=Email)
            user.save()
            user.password=Pass
            user.profile.numero=Phone
            user.set_password(user.password)
            user.save()
        except Exception as e:
            print(str(e))
            data={
                'error':str(e),
                'Fname':Fname,
                'Lname':Lname,
                'Email':Email,
                'Phone':Phone,
            }
            return render(request,'MyApp/register.html',data)
        data={
            'message':'Filicitation {} votre compte a ee cree '.format(Fname)
        }
        print('Inscription OK')
        return render(request,'MyApp/login.html',data)
    else:
        print('Error password')
        data={
            'error':'password is not equals ',
        }
        return redirect('register/')


def connexion(request):
        return render(request,'MyApp/login.html')

def myLogin(request):
    userneme=request.POST.get('Login', False)
    Pass=request.POST.get('Pass', False)
    print('UserName={}\nPass={}'.format(userneme,Pass))

    user=authenticate(username=userneme,password=Pass)
    if user is not None:
        login(request,user)
        return redirect('index')
    else:
        data={
            'error':'Login ou password incorecte ',
            'Login':userneme,
        }
        return render(request, 'MyApp/login.html',data)

