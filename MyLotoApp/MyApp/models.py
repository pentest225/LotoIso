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
    idEquipe1=models.ForeignKey(Equipe,on_delete=models.CASCADE,null=True,related_name='Equipe1' )
    idEquipe2=models.ForeignKey(Equipe,on_delete=models.CASCADE,null=True,verbose_name="Equipe2")
    date_debut=models.DateTimeField()
    date_fin=models.DateTimeField()
    scoreEq1=models.IntegerField(null=True)
    scoreEq2=models.IntegerField(null=True)



class Parier(models.Model):
    idUser=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,related_name='User_parie')
    idMath=models.ForeignKey(Math,on_delete=models.CASCADE,null=True,related_name='Math_parie')
    mise=models.IntegerField()
    date_parie=models.DateTimeField(auto_now_add=True)
    date_up=models.DateTimeField(auto_now=True)