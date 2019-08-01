from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    compte_client=models.IntegerField(null=True)
    numero = models.IntegerField(null=True)



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
class Sport(models.Model):
    nom=models.CharField(max_length=100)
    logo=models.CharField(max_length=500,null=True)
    date_add=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nom

class Equipe(models.Model):
    idSport=models.ForeignKey(Sport,on_delete=models.CASCADE,null=True,related_name='Sport')

    nom = models.CharField(max_length=100)
    logo=models.CharField(max_length=500,null=True)
    cote=models.IntegerField(null=True)
    def __str__(self):
        return self.nom

# Create your models here.




class Math(models.Model):
    typeSport=models.ForeignKey(Sport,on_delete=models.CASCADE,null=True,related_name='typeMath')
    idEquipe1=models.ForeignKey(Equipe,on_delete=models.CASCADE,null=True,related_name='Equipe1' )
    idEquipe2=models.ForeignKey(Equipe,on_delete=models.CASCADE,null=True,verbose_name="Equipe2")
    date_math=models.DateField(auto_now=True, null=True)
    heure_debut=models.CharField(max_length=10,null=True)
    heure_fin=models.CharField(max_length=10,null=True)
    scoreEq1= models.CharField(default=0 ,max_length=10)
    scoreEq2=models.CharField(default=0,max_length=10)

class Parier(models.Model):
    idUser=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,related_name='User_parie')
    idMath=models.ForeignKey(Math,on_delete=models.CASCADE,null=True,related_name='Math_parie')
    mise=models.IntegerField(null=True)
    date_parie=models.DateTimeField(auto_now_add=True)
    date_up=models.DateTimeField(auto_now=True)