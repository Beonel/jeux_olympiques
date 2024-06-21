from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class CustomUser(AbstractUser):
    key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    groups = models.ManyToManyField(
        'auth.Group', related_name='customuser_set', #Nom unique pour la relation inversée
        blank=True,
        help_text=('Les groupes auxquels cet utilisateur appartient. Un utilisateur aura toutes les autorisations' 'accordés à chacun de leurs groupes.'),
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set', #Nom unique pour la relation inversée
        blank=True,
        help_text='Autorisations spécifiques pour cet utilisateur.',
        related_query_name='user'
    )
        

