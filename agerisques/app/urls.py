from django.contrib import admin
from django.urls import path, include
from . import views 

app_name = 'app'
urlpatterns = [ 

    path('', views.template, name = 'template'),
    path ('relance', views.relance, name = 'relance_list'),

    path('Souscripteur_list/', views.Souscripteur_list, name = 'Souscripteur_list'),
    path('Souscripteur_insert/', views.Souscripteur_upload, name = 'Souscripteur_insert'),
    path('<int:id>/',views.Souscripteur_update, name = 'Souscripteur_update'),
    path('delete/<int:id>/',views.Souscripteur_delete, name = 'Souscripteur_delete'),

    path('Assuré_list/', views.Assuré_list, name = 'Assuré_list'),
    path('Assuré_insert/', views.Assuré_upload, name = 'Assuré_insert'),
    path('A<int:A>/',views.Assuré_update, name = 'Assuré_update'),
    path('deleteA/<int:A>/',views.Assuré_delete, name = 'Assuré_delete'),
    
    path('Paiement_list/', views.Paiement_list, name = 'Paiement_list'),
    path('Paiement_insert/', views.Paiement_upload, name = 'Paiement_insert'),
    path('P<int:P>/',views.Paiement_update, name = 'Paiement_update'),
    path('deleteP/<int:P>/',views.Paiement_delete, name = 'Paiement_delete'),
    
    
    path('Police_list/', views.Police_list, name = 'Police_list'),
    path('Police_insert/', views.Police_upload, name = 'Police_insert'),
    path('Po<int:Po>/',views.Police_update, name = 'Police_update'),
    path('deletePo/<int:Po>/',views.Police_delete, name = 'Police_delete'),
    
    path('Sinistre_list/', views.Sinistre_list, name = 'Sinistre_list'),
    path('Sinistre_insert/', views.Sinistre_upload, name = 'Sinistre_insert'),
    path('Si<int:Si>/',views.Sinistre_update, name = 'Sinistre_update'),
    path('deleteSi/<int:Si>/',views.Sinistre_delete, name = 'Sinistre_delete'),

]