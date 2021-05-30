from django.db import models
from django.conf import settings

class Souscripteur(models.Model):
    nom_souscripteur = models.CharField(max_length=50)
    prenom_souscripteur = models.CharField(max_length=200)
    contact_souscripteur = models.CharField(max_length=20)
    mail_souscripteur = models.EmailField(max_length=50)
    numCNI_souscripteur = models.CharField(max_length=20)
    lib_1 = models.CharField(max_length=20)
    lib_2 = models.CharField(max_length=20)
    lib_3 = models.CharField(max_length=20)
    lib_4 = models.CharField(max_length=20)
    lib_5 = models.CharField(max_length=20)
    lib_6 = models.CharField(max_length=20)
    lib_7 = models.CharField(max_length=20)
    lib_8 = models.CharField(max_length=20)
    lib_9 = models.CharField(max_length=20)
    lib_10 = models.CharField(max_length=20)
    def __str__(self):
        return self.nom_souscripteur


class Assuré(models.Model):
    nom_assure = models.CharField(max_length=50)
    prenom_assure = models.CharField(max_length=200)
    contact_assure = models.CharField(max_length=20)
    mail_assure= models.EmailField(max_length=50)
    numCNI_assure = models.CharField(max_length=20)
    lib_1 = models.CharField(max_length=20)
    lib_2 = models.CharField(max_length=20)
    lib_3 = models.CharField(max_length=20)
    lib_4 = models.CharField(max_length=20)
    lib_5 = models.CharField(max_length=20)
    lib_6 = models.CharField(max_length=20)
    lib_7 = models.CharField(max_length=20)
    lib_8 = models.CharField(max_length=20)
    lib_9 = models.CharField(max_length=20)
    lib_10 = models.CharField(max_length=20)
    def __str__(self):
        return self.nom_assure


class Paiement(models.Model):
    souscripteur = models.ForeignKey ('Souscripteur', on_delete = models.CASCADE, null= True, blank = True)
    police = models.ForeignKey('Police', on_delete = models.CASCADE,null= True, blank = True)
    somme_verse = models.DecimalField(max_digits=10, decimal_places=2)
    date_paiement = models.DateField()
    lib_1 = models.CharField(max_length=20)
    lib_2 = models.CharField(max_length=20)
    lib_3 = models.CharField(max_length=20)
    lib_4 = models.CharField(max_length=20)
    lib_5 = models.CharField(max_length=20)
    lib_6 = models.CharField(max_length=20)
    lib_7 = models.CharField(max_length=20)
    lib_8 = models.CharField(max_length=20)
    lib_9 = models.CharField(max_length=20)
    lib_10 = models.CharField(max_length=20)
    def __str__(self):
        return self.somme_verse


class Police(models.Model):
    type_contrat = models.ForeignKey('Type_contrat', on_delete = models.CASCADE, null= True, blank = True)
    compagnie = models.ForeignKey('Compagnie', on_delete = models.CASCADE, null= True, blank = True)
    assurés = models.ManyToManyField('Assuré', blank = True)
    prime_ttc_A = models.DecimalField(max_digits=10, decimal_places=2)  
    prime_ttc_B = models.DecimalField(max_digits=10, decimal_places=2)
    numero_police = models.CharField(max_length=20)
    numero_attestation = models.CharField(max_length=20)
    numero_CEDEAO = models.CharField(max_length=20)
    date_signature = models.DateField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    prime_net_A = models.DecimalField(max_digits=10, decimal_places=2)
    prime_net_B = models.DecimalField(max_digits=10, decimal_places=2)
    accessoire_A = models.DecimalField(max_digits=8, decimal_places=2)
    accessoire_B = models.DecimalField(max_digits=8, decimal_places=2)
    taxe_A = models.DecimalField(max_digits=8, decimal_places=2)
    taxe_B = models.DecimalField(max_digits=8, decimal_places=2)
    CEDEAO = models.DecimalField(max_digits=8, decimal_places=2)
    lib_1 = models.CharField(max_length=20)
    lib_2 = models.CharField(max_length=20)
    lib_3 = models.CharField(max_length=20)
    lib_4 = models.CharField(max_length=20)
    lib_5 = models.CharField(max_length=20)
    lib_6 = models.CharField(max_length=20)
    lib_7 = models.CharField(max_length=20)
    lib_8 = models.CharField(max_length=20)
    lib_9 = models.CharField(max_length=20)
    lib_10 = models.CharField(max_length=20)
    def __str__(self):
        return self.numero_police




class Type_contrat(models.Model):
    libelle_contrat = models.CharField(max_length=500)
    lib_1 = models.CharField(max_length=20)
    lib_2 = models.CharField(max_length=20)
    lib_3 = models.CharField(max_length=20)
    lib_4 = models.CharField(max_length=20)
    lib_5 = models.CharField(max_length=20)
    lib_6 = models.CharField(max_length=20)
    lib_7 = models.CharField(max_length=20)
    lib_8 = models.CharField(max_length=20)
    lib_9 = models.CharField(max_length=20)
    lib_10 = models.CharField(max_length=20)
    def __str__(self):
        return self.libelle_contrat


class Compagnie(models.Model):
    nom_compagnie = models.CharField(max_length=100)
    lib_1 = models.CharField(max_length=20)
    lib_2 = models.CharField(max_length=20)
    lib_3 = models.CharField(max_length=20)
    lib_4 = models.CharField(max_length=20)
    lib_5 = models.CharField(max_length=20)
    lib_6 = models.CharField(max_length=20)
    lib_7 = models.CharField(max_length=20)
    lib_8 = models.CharField(max_length=20)
    lib_9 = models.CharField(max_length=20)
    lib_10 = models.CharField(max_length=20)
    def __str__(self):
        return self.nom_compagnie


class Sinistre(models.Model):
    police = models.ForeignKey('Police', on_delete = models.CASCADE, null= True, blank = True)
    libelle_sinistre = models.CharField(max_length=500)
    responsable_sinistre = models.CharField(max_length=100)
    numero_sinistre = models.CharField(max_length=10)
    designation_victime = models.CharField(max_length=100)
    designation_adversaire = models.CharField(max_length=100)
    designation_beneficiaire = models.CharField(max_length=100)
    date_survenance = models.DateField()
    date_declaration = models.DateField()
    evaluation = models.CharField(max_length=500)
    code_compagnie = models.CharField(max_length=10)
    indemnisation = models.DecimalField(max_digits=10, decimal_places=2)
    date_indemnisation = models.DateField()
    lib_1 = models.CharField(max_length=20)
    lib_2 = models.CharField(max_length=20)
    lib_3 = models.CharField(max_length=20)
    lib_4 = models.CharField(max_length=20)
    lib_5 = models.CharField(max_length=20)
    lib_6 = models.CharField(max_length=20)
    lib_7 = models.CharField(max_length=20)
    lib_8 = models.CharField(max_length=20)
    lib_9 = models.CharField(max_length=20)
    lib_10 = models.CharField(max_length=20)
    def __str__(self):
        return self.libelle_sinistre



class UserRegistrationModel(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)