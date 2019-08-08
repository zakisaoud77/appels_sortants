import django_tables2 as tables
from django_tables2 import TemplateColumn
from .models import *
from django_tables2.utils import A  # alias for Accessor
from django.contrib.auth.models import User



class ContactTable(tables.Table):

     
    class Meta:

        model = Contact
     
        fields = ['nom','prenom', 'mobile','statut','dernier_appel_date','prochain_appel_date','adresse']
        attrs = {'class': 'table table-sm'}
        template_name = 'django_tables2/bootstrap.html'

    nom = tables.LinkColumn('appels_sortants:contact_detail', args=[A('pk')], orderable=False)
    delete = TemplateColumn(template_name='appels_sortants/delete_button.html')
    edit = TemplateColumn(template_name='appels_sortants/edit_button.html')    
    selected = tables.CheckBoxColumn(accessor='pk', orderable=False) 
    


class HistoriqueTable(tables.Table):

     
    class Meta:
    
        model = Historique

        fields = ['contact', 'id_action', 'comment', 'created_date','operateur' ]
        attrs = {'class': 'table table-sm'}
        template_name = 'django_tables2/bootstrap.html'

    contact = tables.LinkColumn('appels_sortants:contact_detail2', args=[A('pk')], orderable=False)
    #operateur = tables.LinkColumn('appels_sortants:contact_detail2', args=[A('pk')], orderable=False)

    #delete = TemplateColumn(template_name='appels_sortants/delete_button.html')
    #edit = TemplateColumn(template_name='appels_sortants/edit_button.html')    
  

class UserTable(tables.Table):

     
    class Meta:
        
        model = User

        fields = ['username', 'email', 'first_name', 'last_name','last_login','date_joined','is_superuser' ]
        attrs = {'class': 'table table-sm'}
        template_name = 'django_tables2/bootstrap.html'
    


    #username = tables.LinkColumn('appels_sortants:user_detail', args=[A('pk')], orderable=False)
    delete = tables.TemplateColumn(template_name='appels_sortants/delete_button_user.html')
    edit = TemplateColumn(template_name='appels_sortants/edit_button_user.html')  
    
 
