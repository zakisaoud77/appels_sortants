from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django_tables2 import RequestConfig
from django.core.exceptions import PermissionDenied
from django.views.generic import DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import *
from .tables import *
from next_prev import next_in_order, prev_in_order
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from datetime import timedelta
from django.template.loader import render_to_string
from django.contrib import messages
from django.db.models import Q
import csv, io




# just for try 
def home(request):

    return HttpResponse('<html><body>toto</body></html>') 

'''
def bla(request,pk):


    contacte = get_object_or_404(Contact, pk=pk)
    #print(contacte)
    
    historique = Historique(contact=contacte, id_action=1, comment="accepted")
    historique.save(force_insert=True)
    #print(historique)
    return redirect('appels_sortants:contact_detail',pk=pk)
'''

def appel_started(request):

        if request.method == 'GET':
               pk = request.GET['contact_id']
               contacte = get_object_or_404(Contact, pk=pk)
               historique = Historique(contact=contacte, id_action=0, comment="Appel lancé")
               historique.save(request,force_insert=True)

               return HttpResponse("Success!!!") # Sending an success response
        else:
               return HttpResponse("Request method is not a GET")



def appel_answered(request):

        if request.method == 'GET':
               pk = request.GET['contact_id']
               contacte = get_object_or_404(Contact, pk=pk)
               contacte.statut = -1
               contacte.save() 

               answer = request.GET['button_type']

               historique = Historique(contact=contacte, id_action=1, comment="Appel accepté")
               historique.save(request,force_insert=True)

               if (answer=="interested") : 
                  historique = Historique(contact=contacte, id_action=3, comment="Client intéressé")
                  historique.save(request,force_insert=True)

               elif (answer == "non_interested") :
                  historique = Historique(contact=contacte, id_action=4, comment="Client non intéressé")
                  historique.save(request,force_insert=True)


               return HttpResponse("Success!!!") # Sending an success response
        else:
               return HttpResponse("Request method is not a GET")


def appel_non_answered(request):

        if request.method == 'GET':
               pk = request.GET['contact_id']
               contacte = get_object_or_404(Contact, pk=pk)
               historique = Historique(contact=contacte, id_action=2, comment="Appel refusé")
               historique.save(request,force_insert=True)

               return HttpResponse("Success!!!") # Sending an success response
        else:
               return HttpResponse("Request method is not a GET")




######################################################
######################################################



def contacts_list(request):

    #contacts = Contact.objects.filter().order_by('id')
    #qs = User.objects.filter(Q(first_name__startswith='R')|Q(last_name__startswith='D'))
    
    CurrentDate = datetime.datetime.now()
    now = timezone.now()

    #contacts = Contact.objects.filter(prochain_appel_date__lte = now).order_by('id')
    contacts = Contact.objects.filter((Q(prochain_appel_date__lte = now) & ~Q(statut = -1)) |(Q(prochain_appel_date = None) & ~Q(statut = -1))).order_by('id')
    print(contacts)
    if contacts:

     first_contact = contacts[0]
     nb_contacts = len(contacts)

     if (nb_contacts==1) :
        vide = True

     elif  (nb_contacts>1):
          vide = False

     elif  (nb_contacts==0):
    	#return HttpResponse('<html><body>toto</body></html>') 
        return render(request, 'appels_sortants/empty_data.html')
    
     ## Instructions to show date formulaire
     if request.method == "POST":

        form = ProchainappelForm(request.POST, instance=first_contact)
        if form.is_valid():
            first_contact = form.save(commit=False)
            first_contact.save()
            return redirect('appels_sortants:contact_detail', pk=first_contact.pk)
     else:

        form = ProchainappelForm(instance=first_contact)

     return render(request, 'appels_sortants/contact_detail.html', {'form':form, 'vide':vide, 'contact': first_contact})
    
    else:
    
     #return render(request, 'appels_sortants/empty_data.html')
     return redirect('appels_sortants:contacts_upload')



def contact_detail(request, pk):
    
    #contacts = Contact.objects.all().order_by('id')
    print("contact_detail")

    now = timezone.now()
    contacts = Contact.objects.filter((Q(prochain_appel_date__lte = now) & ~Q(statut = -1)) |(Q(prochain_appel_date = None) & ~Q(statut = -1))).order_by('id')
    print(contacts)
    
    if contacts:

     last_contact  = contacts.reverse()[0]
     contact = get_object_or_404(Contact, pk=pk)
     nb_contacts = len(contacts)
     first_contact = contacts[0]

     print("first",first_contact)
     print("last", last_contact)
    
     if (nb_contacts==1) :

        vide = True
     else:
        vide = False

     if (last_contact.id == contact.id) :

        statut = True
     else:
        statut = False

     print(vide,statut)
    
     ## Instructions to show date formulaire
     if request.method == "POST":
        form = ProchainappelForm(request.POST, instance=contact)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()

            #return redirect('appels_sortants:contact_detail', pk=contact.pk)
            return redirect('appels_sortants:contact_detail', pk=contact.pk)
     else:
        form = ProchainappelForm(instance=contact)


     return render(request, 'appels_sortants/contact_detail.html', {'form': form,'first':first_contact ,'vide':vide, 'islast':statut, 'contact': contact})
    
    else:
    
     #return render(request, 'appels_sortants/empty_data.html')
     return redirect('appels_sortants:contacts_upload')

# from foreign key 
def contact_detail_from_history(request, pk):
    
    contacts = Contact.objects.all().order_by('id')
    last_contact  = contacts.reverse()[0]

    historique = get_object_or_404(Historique, pk=pk)
    contact = get_object_or_404(Contact, pk=historique.contact.pk)

    nb_contacts = len(contacts)
    first_contact = contacts[0]
    
    if (nb_contacts==1) :

        vide = True
    else:
        vide = False

    if (last_contact.id == contact.id) :

        statut = True
    else:
        statut = False

    print(vide,statut)
    return render(request, 'appels_sortants/contact_detail.html', {'first':first_contact ,'vide':vide, 'islast':statut, 'contact': contact})


def contact_new(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return redirect('appels_sortants:contact_table')

    else:
        form = ContactForm()
        return render(request, 'appels_sortants/contact_new.html', {'form': form})


def contact_edit(request, pk):

    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()

            #return redirect('appels_sortants:contact_detail', pk=contact.pk)
            return redirect('appels_sortants:contact_table')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'appels_sortants/contact_edit.html', {'form': form})


def contact_table(request):

	#order_by = request.GET.get('order_by', 'defaultOrderField')

    table = ContactTable(Contact.objects.all())
    #RequestConfig(request).configure(table)
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'appels_sortants/contact_table.html', {'table': table})

def historique_table(request):
	#order_by = request.GET.get('order_by', 'defaultOrderField')

    table = HistoriqueTable(Historique.objects.all())
    #RequestConfig(request).configure(table)
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'appels_sortants/historique_table.html', {'table': table})



class ContactDelete(DeleteView):

    model = Contact
    success_url = reverse_lazy('appels_sortants:contact_table')


class ContactDelete2(DeleteView):

    model = Contact
    #template_name = 'appels_sortants/contacts_list.html'
    success_url = reverse_lazy('appels_sortants:contacts_list')


def HistoriqueDelete(request):
    
    contacts = Contact.objects.all().order_by('id').update(statut=0)
    #contacts.save()
    Historique.objects.all().delete()

    return redirect('appels_sortants:historique_table')
    

def contact_next(request, pk):
    

    #contacts = Contact.objects.all().order_by('id')
    now = timezone.now()
    contacts = Contact.objects.filter((Q(prochain_appel_date__lte = now) & ~Q(statut = -1)) |(Q(prochain_appel_date = None) & ~Q(statut = -1))).order_by('id')
    contact_actuel = get_object_or_404(Contact, pk=pk)
    contact_next = next_in_order(contact_actuel)

    if contacts: 
     # get next contact
     if contact_next not in contacts:

      while contact_next not in contacts:
        contact_next = next_in_order(contact_next)
        if contact_next == None :
           break

     print("ok",contacts)
     print("actuel, next", contact_actuel, contact_next)
    
     first_contact = contacts[0]
     nb_contacts = len(contacts)
     last_contact  = contacts.reverse()[0]
     vide = False
     statut = False

     print("first, last", first_contact,last_contact)
    
     if(contact_next != None) :
     
      if (last_contact.id == contact_next.id) :

        statut = True
      else:
        statut = False
      print(statut)

      if (nb_contacts==1) :

        vide = True
      else:
        vide = False
      print(nb_contacts)
    
     ## Instructions to show date formulaire
     if request.method == "POST":
        form = ProchainappelForm(request.POST, instance=contact_next)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()

            #return redirect('appels_sortants:contact_detail', pk=contact.pk)
            return redirect('appels_sortants:contact_detail', pk=contact_next.pk)
     else:
        form = ProchainappelForm(instance=contact_next)

     return render(request, 'appels_sortants/contact_detail.html', {'form':form, 'vide':vide, 'first':first_contact,'islast': statut,'contact': contact_next})
    
    else:

     #return render(request, 'appels_sortants/empty_data.html')
     return redirect('appels_sortants:contacts_upload')

def date_edit(request, pk):

    contact = get_object_or_404(Contact, pk=pk)

    if request.method == "POST":
        form = ProchainappelForm(request.POST, instance=contact)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()

            #return redirect('appels_sortants:contact_detail', pk=contact.pk)
            return redirect('appels_sortants:contact_detail', pk=contact.pk)
    else:
        form = ProchainappelForm(instance=contact)

    return render(request, 'appels_sortants/date_edit.html', {'form': form})


###################################################################
###    User management *******************************************
####################################################################


def user_table(request):


    #table = UserTable(User.objects.all())
    table = UserTable(User.objects.filter(is_superuser=False))
    #RequestConfig(request).configure(table)
    RequestConfig(request, paginate={'per_page': 10}).configure(table)


    return render(request, 'appels_sortants/user_table.html', {'table': table})


def user_detail(request, pk):
    
    user = get_object_or_404(User, pk=pk)
    print(user)
    return render(request, 'appels_sortants/user_detail.html', {'user': user})


def index(request):
    return render(request,'appels_sortants/index.html')

def okok(request):
    return render(request,'appels_sortants/okok.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('appels_sortants:index'))



def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'appels_sortants/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('appels_sortants:index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'appels_sortants/login.html', {})



def user_new(request):

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)

    else:

        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        return render(request,'appels_sortants/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})



class UserDelete(DeleteView):

    model = User
    success_url = reverse_lazy('appels_sortants:user_table')



def user_edit(request, pk):

    registered = False
    user= get_object_or_404(User, pk=pk)
    if request.method == "POST":
        user_form = UserForm(data=request.POST,instance=user)
        profile_form = UserProfileInfoForm(data=request.POST,instance=user)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
            return redirect('appels_sortants:user_table')
        else:
            print(user_form.errors,profile_form.errors)

    else:

        user_form = UserForm(instance=user)
        profile_form = UserProfileInfoForm(instance=user)
        return render(request,'appels_sortants/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})


#############################
##  Upolad contacts
##############################


def contacts_upload(request):

    #template = "appels_sortants/contacts_upload.html"
    template = "appels_sortants/empty_data.html"
    print(template)
    #propmt = {'order' : 'Order of the CSV should be nom, prenom...' }

    if "GET" == request.method:
        #return render(request, template, prompt)
        return render(request, template)
    

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
           messages.error(request,'File is not CSV type')
    

    data_set = csv_file.read().decode("utf-8")  
    io_string = io.StringIO(data_set)
    next(io_string) 
    for column in csv.reader(io_string, delimiter =',', quotechar="|"):
        _, created = Contact.objects.update_or_create(
        nom = column[0],
        prenom = column[1],
        mobile = column[2],
        adresse = column[3],
        )

    #context = {}
    #return render(request, template, context)
    return redirect('appels_sortants:contact_table')



def contacts_upload2(request):

    if request.method == 'POST':
        csv_file= request.FILES['file']
        #print(csv_file.name)
        #print(csv_file.size)

    data_set = csv_file.read().decode("utf-8")  
    io_string = io.StringIO(data_set)
    next(io_string) 
    for column in csv.reader(io_string, delimiter =',', quotechar="|"):
        _, created = Contact.objects.update_or_create(
        nom = column[0],
        prenom = column[1],
        mobile = column[2],
        adresse = column[3],
        )

    return redirect('appels_sortants:contact_table')

