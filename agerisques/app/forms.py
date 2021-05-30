from django.contrib.auth.models import User
from django import forms
from .models import Souscripteur, Assuré, Paiement, Police, Type_contrat, Compagnie, Sinistre 


class SouscripteurForm (forms.ModelForm):
    class Meta :
        model = Souscripteur
        fields = ('nom_souscripteur','prenom_souscripteur', 'contact_souscripteur', 'mail_souscripteur','numCNI_souscripteur')


class AssuréForm (forms.ModelForm):
    class Meta :
        model = Assuré
        fields = ('nom_assure','prenom_assure', 'contact_assure', 'mail_assure','numCNI_assure')


class PaiementForm (forms.ModelForm):
    class Meta :
        model = Paiement
        fields = ('somme_verse','date_paiement','police', 'souscripteur')
    

class PoliceForm (forms.ModelForm):
    class Meta :
        model = Police
        fields = ('prime_ttc_A','prime_ttc_B', 'numero_police','numero_attestation','numero_CEDEAO','date_signature','date_debut','date_fin','prime_net_A','prime_net_B','accessoire_A','accessoire_B','taxe_A','taxe_B','CEDEAO', 'type_contrat', 'compagnie', 'assurés')


class Type_contratForm (forms.ModelForm):
    class Meta :
        model = Type_contrat
        fields = ('libelle_contrat',)

class CompagnieForm (forms.ModelForm):
    class Meta :
        model = Compagnie
        fields = ('nom_compagnie',)


class SinistreForm (forms.ModelForm):
    class Meta :
        model = Sinistre
        fields = ('libelle_sinistre','responsable_sinistre','numero_sinistre','designation_victime','designation_adversaire','designation_beneficiaire','date_survenance','date_declaration','evaluation','code_compagnie','indemnisation','date_indemnisation', 'police')      


class UserRegistration(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Passwords don\'t match.')
            return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')