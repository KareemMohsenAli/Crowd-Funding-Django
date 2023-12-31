# Generated by Django 4.1.7 on 2023-03-15 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_reportcomment_boolean_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportcomment',
            name='comment',
        ),
        migrations.AddField(
            model_name='reportcomment',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commentrr', to='projects.project'),
        ),
        migrations.AlterField(
            model_name='reportcomment',
            name='user_id',
            field=models.TextField(null=True),
        ),
    ]
