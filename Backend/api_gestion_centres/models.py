from django.db import models
from Backend.api_auth.models import User

class Centre(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='centre_logos/', null=True, blank=True)
    numeros_telephone = models.CharField(max_length=200)
    emails = models.EmailField()
    numero_compte = models.CharField(max_length=100)
    no_ifu = models.CharField(max_length=100)
    isActif = models.BooleanField(default=True)
    heure_douverture = models.CharField(max_length=200)     #par exemple "9h00 - 18h00" ou "8:30 AM - 5:00 PM"
    services_offerts = models.TextField()

    # Relation pour les abonnements
    abonnements = models.ManyToManyField('Abonnement', related_name='centres', null=True, blank=True)

    def __str__(self):
        return self.nom
class Abonnement(models.Model):
    centre = models.ForeignKey(Centre, on_delete=models.CASCADE)
    date_abonnement = models.DateTimeField(auto_now_add=True)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    isValide = models.BooleanField(default=False)

    def __str__(self):
        return f"Abonnement for {self.centre}"

class Profil(models.Model):
    SUPER_ADMIN = 'superAdmin'
    ADMIN_LOCAL = 'adminLocal'
    PERSONNEL_ADMIN = 'personnelAdmin'
    PERSONNEL = 'personnel'
    USER = 'user'

    PROFIL_CHOICES = [
        (SUPER_ADMIN, 'Super Admin'),
        (ADMIN_LOCAL, 'Admin Local'),
        (PERSONNEL_ADMIN, 'Personnel Admin'),
        (PERSONNEL, 'Personnel'),
        (USER, 'User'),
    ]

    profil_type = models.CharField(
        max_length=20,
        choices=PROFIL_CHOICES,
        default=USER,
    )
    
    def __str__(self):
        # Utilisez un dictionnaire pour mapper le profil_type aux noms de profil
        profil_names = {
            self.SUPER_ADMIN: 'Super Admin',
            self.ADMIN_LOCAL: 'Admin Local',
            self.PERSONNEL_ADMIN: 'Personnel Admin',
            self.PERSONNEL: 'Personnel',
            self.USER: 'User',
        }
        return profil_names.get(self.profil_type, 'Unknown')  

class Profil_Affectation(models.Model):
    date_affectation = models.DateField(auto_now_add=True)
    isValide = models.BooleanField(default=True)
    centre = models.ForeignKey('api_gestion_centres.Centre', on_delete=models.CASCADE)
    user = models.ForeignKey('api_auth.User', on_delete=models.CASCADE)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)

    def __str__(self):
        return f"Affectation du centre {self.centre}"


    # Explications :

    # Nous avons ajouté la fonction create_groups_for_profiles, qui récupère tous les types de profil 
    # disponibles dans le modèle Profil et crée les groupes correspondants pour chaque type de profil à 
    # l'aide de la classe Group de Django.

    # Dans la fonction create_groups_for_profiles, nous utilisons get_or_create pour obtenir le groupe avec 
    # le nom correspondant. S'il n'existe pas encore, il sera créé automatiquement.

    # Nous avons également utilisé le signal post_migrate pour appeler la fonction create_groups au moment d
    # es migrations. Cela garantit que les groupes seront créés automatiquement chaque fois que les migrations
    #  sont appliquées.



    @property
    def nom(self):
        return self.contenu
