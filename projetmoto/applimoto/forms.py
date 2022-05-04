from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class EcurieForm(ModelForm):
    class Meta:
        model = models.Ecurie

        fields = {'nom', "marque", "team_manager", 'sponsor', 'date_creation',}
        labels = {
            'nom': _('Nom'),
            'marque': _('Marque'),
            'team_manager': _('Team-manager'),
            'sponsor': _('Sponsor officel'),
            'date_creation': _('Date de creation'),
        }

class PiloteForm(ModelForm):
    class Meta:
        model = models.Pilote

        fields = {'nom_pilote', 'prenom', 'age',}
        labels = {
            'nom_pilote': _('Nom'),
            'prenom': _('Prenom'),
            'age': _('Age'),
        }