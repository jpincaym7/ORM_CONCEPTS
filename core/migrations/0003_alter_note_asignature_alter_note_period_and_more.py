# Generated by Django 4.2 on 2024-06-14 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_detailnote_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='asignature',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asignature_note', to='core.asignature'),
        ),
        migrations.AlterField(
            model_name='note',
            name='period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='period_note', to='core.period'),
        ),
        migrations.AlterField(
            model_name='note',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_note', to='core.teacher'),
        ),
    ]
