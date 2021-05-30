from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from .models import Souscripteur, Assuré, Paiement, Police, Sinistre, Paiement
from .forms import SouscripteurForm, AssuréForm, PaiementForm, PoliceForm, PoliceForm, SinistreForm
from datetime import date
from django.contrib.auth.decorators import login_required
from .forms import UserRegistration, UserEditForm

def relance (request):
    PO_list = {'Police_list': Police.objects.all()}
    return render (request, 'pages/relance_list.html', PO_list)
    # prendre tous les objets Police
    # pour chaque objets voir la date de fin est inférieur à 14 jours
    # si oui recupérer le numero de police dans une liste
    # afficher la liste dans un template
    ##


def template(request):
    return render(request,'pages/index.html')


    # CRUD Souscripteur
def Souscripteur_list(request):
    S_list = {'Souscripteur_list': Souscripteur.objects.all()}
    return render (request, 'pages/Souscripteur_list.html', S_list)


def Souscripteur_upload (request):
    souscripteur = SouscripteurForm()
    if request.method == "POST":
        souscripteur = SouscripteurForm(request.POST, request.FILES)
        if souscripteur.is_valid():
            souscripteur.save()
            return redirect('Souscripteur_list')
        else :
            return HttpResponse("""votre formulaire est invalide, veuillez le corriger s'il vous plait <a href = "../Souscripteur_insert">formulaire</a>""")
    else :
        return render(request, 'pages/Souscripteur_form.html', {'souscripteur_form': souscripteur})



def Souscripteur_update (request, id):
    try:
        souscripteur_selected = Souscripteur.objects.get(pk = id)
    except Souscripteur.DoesNotExist:
        return redirect('Souscripteur_list')
    souscripteur_form = SouscripteurForm(request.POST or None, instance= souscripteur_selected)
    if souscripteur_form.is_valid():
        souscripteur_form.save()
        return redirect('Souscripteur_list')
    return render (request, 'pages/Souscripteur_form.html', {'souscripteur_form': souscripteur_form})


def Souscripteur_delete (request, id):
    souscripteur = Souscripteur.objects.get(pk = id)
    souscripteur.delete()
    return redirect('Souscripteur_list')

# CRUD Assuré
def Assuré_list(request):
    A_list = {'Assuré_list': Assuré.objects.all()}
    return render (request, 'pages/Assuré_list.html', A_list)


def Assuré_upload (request):
    assuré = AssuréForm()
    if request.method == "POST":
        assuré = AssuréForm(request.POST, request.FILES)
        if assuré.is_valid():
            assuré.save()
            return redirect('Assuré_list')
        else :
            return HttpResponse("""votre formulaire est invalide, veuillez le corriger s'il vous plait <a href = "../Assuré_insert">formulaire</a>""")
    else :
        return render(request, 'pages/Assuré_form.html', {'assuré_form': assuré})



def Assuré_update (request, A):
    try:
        assuré_selected = Assuré.objects.get(pk = A)
    except Assuré.DoesNotExist:
        return redirect('Assuré_list')
    assuré_form = AssuréForm(request.POST or None, instance= assuré_selected)
    if assuré_form.is_valid():
        assuré_form.save()
        return redirect('Assuré_list')
    return render (request, 'pages/Assuré_form.html', {'assuré_form': assuré_form})


def Assuré_delete (request, A):
    assuré = Assuré.objects.get(pk = A)
    assuré.delete()
    return redirect('Assuré_list')


# CRUD Paiement
def Paiement_list(request):
    P_list = {'Paiement_list': Paiement.objects.all()}
    return render (request,'pages/Paiement_list.html',P_list)


def Paiement_upload (request):
    paiement = PaiementForm()
    if request.method == "POST":
        paiement = PaiementForm(request.POST, request.FILES)
        if paiement.is_valid():
            paiement.save()
            return redirect('Paiement_list')
        else :
            return HttpResponse("""votre formulaire est invalide, veuillez le corriger s'il vous plait <a href = "../Paiement_insert">formulaire</a>""")
    else :
        return render(request, 'pages/Paiement_form.html', {'paiement_form': paiement})



def Paiement_update (request, P):
    id = int(P)
    try:
        paiement_selected = Paiement.objects.get(pk = id)
    except Paiement.DoesNotExist:
        return redirect('Paiement_list')
    paiement_form = PaiementForm(request.POST or None, instance= paiement_selected)
    if paiement_form.is_valid():
        paiement_form.save()
        return redirect('Paiement_list')
    return render (request, 'pages/Paiement_form.html', {'paiement_form': paiement_form})


def Paiement_delete (request, P):
    paiement = Paiement.objects.get(pk = P)
    paiement.delete()
    return redirect('Paiement_list')



# CRUD Police
def Police_list(request):
    Po_list = {'Police_list': Police.objects.all()}
    return render (request, 'pages/Police_list.html', Po_list)


def Police_upload (request):
    police = PoliceForm()
    if request.method == "POST":
        police = PoliceForm(request.POST, request.FILES)
        if police.is_valid():
            police.save()
            return redirect('Police_list')
        else :
            return HttpResponse("""votre formulaire est invalide, veuillez le corriger s'il vous plait <a href = "../Police_insert"> formulaire </a>""")
    else :
        return render(request, 'pages/Police_form.html', {'police_form': police})



def Police_update (request, Po):
    try:
        police_selected = Police.objects.get(pk = Po)
    except Police.DoesNotExist:
        return redirect('Police_list')
    police_form = PoliceForm(request.POST or None, instance= police_selected)
    if police_form.is_valid():
        police_form.save()
        return redirect('Police_list')
    return render (request, 'pages/Police_form.html', {'police_form': police_form})


def Police_delete (request, Po):
    police = Police.objects.get(pk = Po)
    police.delete()
    return redirect('Police_list')



# CRUD Sinistre
def Sinistre_list(request):
    Si_list = {'Sinistre_list': Sinistre.objects.all()}
    return render (request, 'pages/Sinistre_list.html', Si_list)


def Sinistre_upload (request):
    sinistre = SinistreForm()
    if request.method == "POST":
        sinistre = SinistreForm(request.POST, request.FILES)
        if sinistre.is_valid():
            sinistre.save()
            return redirect('Sinistre_list')
        else :
            return HttpResponse("""votre formulaire est invalide, veuillez le corriger s'il vous plait <a href = "../Sinistre_insert">formulaire</a>""")
    else :
        return render(request, 'pages/Sinistre_form.html', {'sinistre_form': sinistre})



def Sinistre_update (request, Si):
    try:
        sinistre_selected = Sinistre.objects.get(pk = Si)
    except Sinistre.DoesNotExist:
        return redirect('Sinistre_list')
    sinistre_form = SinistreForm(request.POST or None, instance= sinistre_selected)
    if sinistre_form.is_valid():
        sinistre_form.save()
        return redirect('Sinistre_list')
    return render (request, 'pages/Sinistre_form.html', {'sinistre_form': sinistre_form})


def Sinistre_delete (request, Si):
    sinistre = Sinistre.objects.get(pk = Si)
    sinistre.delete()
    return redirect('Sinistre_list')


