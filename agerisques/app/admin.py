


# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class SouscripteurAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom_souscripteur',
        'prenom_souscripteur',
        'contact_souscripteur',
        'mail_souscripteur',
        'numCNI_souscripteur',
        'lib_1',
        'lib_2',
        'lib_3',
        'lib_4',
        'lib_5',
        'lib_6',
        'lib_7',
        'lib_8',
        'lib_9',
        'lib_10',
    )
    list_filter = (
        'id',
        'nom_souscripteur',
        'prenom_souscripteur',
        'contact_souscripteur',
        'mail_souscripteur',
        'numCNI_souscripteur',
        'lib_1',
        'lib_2',
        'lib_3',
        'lib_4',
        'lib_5',
        'lib_6',
        'lib_7',
        'lib_8',
        'lib_9',
        'lib_10',
    )


class AssuréAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom_assure',
        'prenom_assure',
        'contact_assure',
        'mail_assure',
        'numCNI_assure',
        'lib_1',
        'lib_2',
        'lib_3',
        'lib_4',
        'lib_5',
        'lib_6',
        'lib_7',
        'lib_8',
        'lib_9',
        'lib_10',
    )
    list_filter = (
        'id',
        'nom_assure',
        'prenom_assure',
        'contact_assure',
        'mail_assure',
        'numCNI_assure',
        'lib_1',
        'lib_2',
        'lib_3',
        'lib_4',
        'lib_5',
        'lib_6',
        'lib_7',
        'lib_8',
        'lib_9',
        'lib_10',
    )


class PaiementAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'souscripteur',
        'police',
        'somme_verse',
        'date_paiement',
        'lib_1',
        'lib_2',
        'lib_3',
        'lib_4',
        'lib_5',
        'lib_6',
        'lib_7',
        'lib_8',
        'lib_9',
        'lib_10',
    )
    list_filter = (
        'souscripteur',
        'police',
        'date_paiement',
        'id',
        'souscripteur',
        'police',
        'somme_verse',
        'date_paiement',
        'lib_1',
        'lib_2',
        'lib_3',
        'lib_4',
        'lib_5',
        'lib_6',
        'lib_7',
        'lib_8',
        'lib_9',
        'lib_10',
    )


class PoliceAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'type_contrat',
        'compagnie',
        'prime_ttc_A',
        'prime_ttc_B',
        'numero_police',
        'numero_attestation',
        'numero_CEDEAO',
        'date_signature',
        'date_debut',
        'date_fin',
        'prime_net_A',
        'prime_net_B',
        'accessoire_A',
        'accessoire_B',
        'taxe_A',
        'taxe_B',
        'CEDEAO',
        'lib_1',
        'lib_2',
        'lib_3',
        'lib_4',
        'lib_5',
        'lib_6',
        'lib_7',
        'lib_8',
        'lib_9',
        'lib_10',
    )
    list_filter = (
        'type_contrat',
        'compagnie',
        'date_signature',
        'date_debut',
        'date_fin',
        'id',
        'type_contrat',
        'compagnie',
        'prime_ttc_A',
        'prime_ttc_B',
        'numero_police',
        'numero_attestation',
        'numero_CEDEAO',
        'date_signature',
        'date_debut',
        'date_fin',
        'prime_net_A',
        'prime_net_B',
        'accessoire_A',
        'accessoire_B',
        'taxe_A',
        'taxe_B',
        'CEDEAO',
        'lib_1',
        'lib_2',
        'lib_3',
        'lib_4',
        'lib_5',
        'lib_6',
        'lib_7',
        'lib_8',
        'lib_9',
        'lib_10',
    )
    raw_id_fields = ('assurés',)


class Type_contratAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'libelle_contrat',
        'lib_1',
        'lib_2',
        'lib_3',
        'lib_4',
        'lib_5',
        'lib_6',
        'lib_7',
        'lib_8',
        'lib_9',
        'lib_10',
    )
    list_filter = (
        'id',
        'libelle_contrat',
        'lib_1',
        'lib_2',
        'lib_3',
        'lib_4',
        'lib_5',
        'lib_6',
        'lib_7',
        'lib_8',
        'lib_9',
        'lib_10',
    )


class CompagnieAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom_compagnie',
        'lib_1',
        'lib_2',
        'lib_3',
        'lib_4',
        'lib_5',
        'lib_6',
        'lib_7',
        'lib_8',
        'lib_9',
        'lib_10',
    )
    list_filter = (
        'id',
        'nom_compagnie',
        'lib_1',
        'lib_2',
        'lib_3',
        'lib_4',
        'lib_5',
        'lib_6',
        'lib_7',
        'lib_8',
        'lib_9',
        'lib_10',
    )


class SinistreAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'police',
        'libelle_sinistre',
        'responsable_sinistre',
        'numero_sinistre',
        'designation_victime',
        'designation_adversaire',
        'designation_beneficiaire',
        'date_survenance',
        'date_declaration',
        'evaluation',
        'code_compagnie',
        'indemnisation',
        'date_indemnisation',
        'lib_1',
        'lib_2',
        'lib_3',
        'lib_4',
        'lib_5',
        'lib_6',
        'lib_7',
        'lib_8',
        'lib_9',
        'lib_10',
    )
    list_filter = (
        'police',
        'date_survenance',
        'date_declaration',
        'date_indemnisation',
        'id',
        'police',
        'libelle_sinistre',
        'responsable_sinistre',
        'numero_sinistre',
        'designation_victime',
        'designation_adversaire',
        'designation_beneficiaire',
        'date_survenance',
        'date_declaration',
        'evaluation',
        'code_compagnie',
        'indemnisation',
        'date_indemnisation',
        'lib_1',
        'lib_2',
        'lib_3',
        'lib_4',
        'lib_5',
        'lib_6',
        'lib_7',
        'lib_8',
        'lib_9',
        'lib_10',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Souscripteur, SouscripteurAdmin)
_register(models.Assuré, AssuréAdmin)
_register(models.Paiement, PaiementAdmin)
_register(models.Police, PoliceAdmin)
_register(models.Type_contrat, Type_contratAdmin)
_register(models.Compagnie, CompagnieAdmin)
_register(models.Sinistre, SinistreAdmin)
