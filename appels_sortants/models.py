
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.


class Adresse(models.Model):
 
    rue = models.CharField(max_length=30)
    ville = models.CharField(max_length=30)
    pays = models.CharField(max_length=30)
    codezip = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.rue


class Contact(models.Model):
    
    nom = models.CharField(max_length=30,blank=False,null=False)
    prenom = models.CharField(max_length=30,blank=False,null=False)
    #adresse_postal = models.ForeignKey('Adresse',on_delete=models.CASCADE,blank=True, null=True)
    adresse = models.TextField(blank=True, null=True)
    mobile = models.CharField(max_length=30, blank=False,null=False)
    dernier_appel_date = models.DateTimeField(blank=True, null=True)
    prochain_appel_date = models.DateTimeField(blank=True, null=True)
    statut = models.IntegerField(default=00, blank=True, null=True)
     
    def __str__(self):
        return self.nom


class Historique(models.Model):	

    contact  = models.ForeignKey(Contact, on_delete=models.CASCADE, blank=False, null=False)
    id_action = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    operateur = models.ForeignKey(User, null=True,on_delete=models.CASCADE)
    
    #override creation
    def save(self, request, *args, **kwargs):
        self.operateur = request.user
        super().save(*args, **kwargs)  # Call the "real" save() method.


    def __str__(self):
        return (str(self.id_action))




# Create your models here.
class UserProfileInfo(models.Model):
      user = models.OneToOneField(User,on_delete=models.CASCADE)
      site_personnel = models.URLField(blank=True)
      profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
      
      def __str__(self):
         return self.user.username
