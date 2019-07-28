from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    compte_client=models.IntegerField()
    numero=models.IntegerField()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Client.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
class Equipe(models.Model):
    nom = models.CharField(max_length=100)
    logo=models.CharField(max_length=500)
    cote=models.IntegerField()

# Create your models here.
class Sport(models.Model):
    ipEquipe=models.ForeignKey(Equipe,on_delete=models.CASCADE,null=True,related_name='Equipe_sport')
    Nom=models.CharField(max_length=100)
    logo=models.CharField(max_length=100)



class Math(models.Model):
    idEquipe=models.ForeignKey(Equipe,on_delete=models.CASCADE,null=True,related_name='Equipe_math' )
    date_debut=models.DateTimeField()
    date_fin=models.DateTimeField()
    id_equip1=models.IntegerField(verbose_name='Equipe 1')
    id_equip2=models.IntegerField(verbose_name='Equipe 2')
    scoreEq1=models.IntegerField()
    scoreEq2=models.IntegerField()



class Parier(models.Model):
    idUser=models.ForeignKey(Client,on_delete=models.CASCADE,null=True,related_name='User_parie')
    idMath=models.ForeignKey(Math,on_delete=models.CASCADE,null=True,related_name='Math_parie')
    mise=models.IntegerField()
    date_parie=models.DateTimeField(auto_now_add=True)
    date_up=models.DateTimeField(auto_now=True)