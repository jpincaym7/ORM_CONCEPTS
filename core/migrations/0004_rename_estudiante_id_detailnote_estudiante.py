# Generated by Django 4.2 on 2024-06-15 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_note_asignature_alter_note_period_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detailnote',
            old_name='estudiante_id',
            new_name='estudiante',
        ),
    ]
