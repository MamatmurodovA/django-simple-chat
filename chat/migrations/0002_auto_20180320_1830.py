# Generated by Django 2.0.3 on 2018-03-20 18:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversation',
            name='room',
        ),
        migrations.AddField(
            model_name='conversation',
            name='receiver',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='conversation',
            name='sender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL),
        ),
    ]