from django.db import models


class Ecurie(models.Model):
    nom = models.CharField(max_length=50)
    marque = models.CharField(max_length=20)
    team_manager = models.CharField(max_length=50)
    sponsor = models.CharField(max_length=20)
    date_creation = models.DateField(blank=True, null=True)

    def __str__(self):
        texte = f"{self.nom}"
        return texte

    def dico(self):
        return {'nom': self.nom, 'marque': self.marque, 'team_manager': self.team_manager, 'sponsor': self.sponsor,
                'date_creation': self.date_creation}


class Pilote(models.Model):
    ecurie = models.ForeignKey("Ecurie", on_delete=models.CASCADE, default=None)
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    age = models.IntegerField(blank=False)


    #ecurie = models.ForeignKey(Ecurie, default=None)

    def __str__(self):
        textepilote = f"{self.prenom} {self.nom}"
        return textepilote

    def dico(self):
        return {'nom': self.nom, 'prenom': self.prenom, 'age': self.age, 'ecurie': self.ecurie.nom}
