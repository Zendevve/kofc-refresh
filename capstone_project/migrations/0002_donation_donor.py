# Generated migration for adding donor field to Donation model

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('capstone_project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='donor',
            field=models.ForeignKey(blank=True, help_text='The logged-in user who made this donation', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='donations', to=settings.AUTH_USER_MODEL),
        ),
    ]
