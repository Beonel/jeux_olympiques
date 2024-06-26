# Generated by Django 5.0.6 on 2024-06-21 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='Les groupes auxquels cet utilisateur appartient. Un utilisateur aura toutes les autorisationsaccordés à chacun de leurs groupes.', related_name='customuser_set', related_query_name='user', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Autorisations spécifiques pour cet utilisateur.', related_name='customuser_set', related_query_name='user', to='auth.permission'),
        ),
    ]
