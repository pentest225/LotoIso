from django.http import JsonResponse
import json
from requests import get
from bs4 import BeautifulSoup
from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from  django.contrib.auth import  authenticate ,login ,logout
from django.shortcuts import get_object_or_404,render
from .models import *
from  django.utils import timezone
import datetime
# Create your views here.

def index(request):
    AllInfo=Sport.objects.all()
    data={
        'all_info':AllInfo,
    }
    return render(request,'MyApp/index.html',data)
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
@login_required(login_url='/login')
def parie(request,math_id):
    mathInfo = get_object_or_404(Math, pk=math_id)

    return render(request, 'MyApp/parie.html', {'mathInfo': mathInfo})


def scrap(request):
    url = 'https://www.matchendirect.fr/'
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    table = html_soup.find('div', attrs={'id': 'livescore'})
    compt = 1

    mydata = []

    for row in table.findAll('div', attrs={'class': 'panel panel-info'}):
        a_desc = row.find('h3', attrs={'class': 'panel-title'}).get_text()

        try:
            if Sport.objects.filter(nom=a_desc).exists():
                print()
                # print('ok dans la boite ')
            else:
                sprt=Sport(nom=a_desc)
                sprt.save()
                # print('enregistrement en Base de Donne de ',a_desc)
        except Exception as e:
            print('Dans l\'exception sport \nValleur =>{}'.format(e))


        for el in row.findAll('tr'):
            resultat = {}
            heure = el.find('td', attrs={'class': 'lm1'}).get_text()
            eqA = el.find('span', attrs={'class': 'lm3_eq1'}).get_text()
            eqB = el.find('span', attrs={'class': 'lm3_eq2'}).get_text()

            scors = el.find('span', attrs={'class': 'lm3_score'}).get_text()

            resultat['heure'] = heure
            resultat['eqa'] = eqA
            resultat['eqb'] = eqB
            resultat['scors'] = scors

            if '&nbsp' in heure :
                heure='-- : --'

            myScor1=scors[:2]
            myScor2=scors[3:]
            # if len(scors.strip()) != 0:
            #     print("Section :", a_desc)
            #     print("Equipe1:{}\nEquipe2:{}".format(eqA,eqB))
            #     print("Heure du Math ",heure)
            #     print("Scort",scors)
            #     print("Score1",myScor1)
            #     print("Score2", myScor2)
            #     print('Type Scodre ',type(myScor1))
            #     print('En int ',int(myScor1))
            #Enregistrement d'une equipe
            try:

                mySport=Sport.objects.get(nom=a_desc)
                # print("Dans la base de Bonne ",mySport)
                # print(mySport)
                if Equipe.objects.filter(nom=eqA).exists():
                    pass
                else:
                    Equipe1=Equipe(nom=eqA,)
                    Equipe1.idSport=mySport
                    Equipe1.save()
                if Equipe.objects.filter(nom=eqB).exists():
                    pass
                else:
                    Equipe2=Equipe(nom=eqB)
                    Equipe2.idSport=mySport
                    Equipe2.save()

            except Exception as e:
                print()
                print('Execpte Equipe \nValleur Exection:{}'.format(e))

            #Enregistrement d'un math

            try:
                idEq1 = Equipe.objects.get(nom=eqA)
                idEq2 = Equipe.objects.get(nom=eqB)
                if Math.objects.filter(idEquipe1=idEq1,idEquipe2=idEq2,heure_debut=heure).exists():
                    #OK LE MATH EXISTE PENSSON A LA MISE A JOURS DU SCORE
                    dbMath=Math.objects.get(idEquipe1=idEq1,idEquipe2=idEq2,heure_debut=heure)
                    if (dbMath.scoreEq1 != myScor1):
                        dbMath.scoreEq1=myScor1
                        dbMath.save()

                    if (dbMath.scoreEq2 != myScor2):
                        dbMath.scoreEq2=myScor2
                        dbMath.save()

                    # print("Score dase de donnee :\n{}=>{}\n{}=>{}".format(dbMath.idEquipe1,dbMath.scoreEq1,dbMath.idEquipe2,dbMath.scoreEq2))
                else:
                    myTypeSport = Sport.objects.get(nom=a_desc)
                    myMath = Math(heure_debut=heure)
                    myMath.typeSport=myTypeSport
                    myMath.idEquipe1 = idEq1
                    myMath.idEquipe2 = idEq2
                    myMath.scoreEq1=myScor1
                    myMath.scoreEq2 =myScor2
                    myMath.save()



            except Exception as e:
                print()

                print('Math Exception \nValleur :{}'.format(e))


            #Enregistrement d'un mathe

            mydata.append(resultat)
        #verification dans la table sport





    data = mydata
    return JsonResponse(data, safe=False)  # retourn du json
    #return render(request, 'myapp/parie.html', {'result': data})








