from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls import url


# SET THE NAMESPACE!
app_name = 'appels_sortants'


urlpatterns = [
    
    #path('', views.post_list, name='post_list'),
    #path('brr/', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('', views.contacts_list, name='contacts_list'),
    path('contact/<int:pk>/', views.contact_detail, name='contact_detail'),
    path('contact/<int:pk>/edit/', views.contact_edit, name='contact_edit'),
    path('contact/new/', views.contact_new, name='contact_new'),
    path('contacts_table/', views.contact_table, name='contact_table'),
    path('historique_table/', views.historique_table, name='historique_table'),
    path('user_table/', views.user_table, name='user_table'),
    path('historique_table/contact/<int:pk>/', views.contact_detail_from_history, name='contact_detail2'),
    path('delete/<int:pk>/', views.ContactDelete.as_view(), name='contact_delete'),
    path('delete2/<int:pk>/', views.ContactDelete2.as_view(), name='contact_delete2'),
    path('delete_history/', views.HistoriqueDelete, name='historique_delete'),
    #path('contact/<int:pk>+1/', views.contact_next, name='contact_next'),
    path('contact/next/<int:pk>/', views.contact_next, name='contact_next'),
  
    #path('user/<int:pk>/', views.user_detail, name='user_detail'),
    
    path('appel_started/', views.appel_started, name='appel_started'),
    path('appel_answered/', views.appel_answered, name='appel_answered'),
    path('appel_non_answered/', views.appel_non_answered, name='appel_non_answered'),

    path('contact/<int:pk>/date_edit/', views.date_edit, name='date_edit'),

    ## La partie de la gestions des utilisateurs

    url(r'^nouvel_operateur/$',views.register, name='user_new'),
    path('delete_user/<int:pk>/', views.UserDelete.as_view(), name='user_delete'),
    path('user/<int:pk>/', views.user_detail, name='user_detail'),
    path('user/<int:pk>/edit/', views.user_edit, name='user_edit'),
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'index',views.index,name='index'),

    url(r'okok',views.okok,name='okok'),

    path('logout/', views.user_logout, name='logout'),
    #path(r'^special/',views.special,name='special'),
    path('contacts_upload/', views.contacts_upload, name='contacts_upload'),
    path('contacts_upload2/', views.contacts_upload2, name='contacts_upload2'),



]


