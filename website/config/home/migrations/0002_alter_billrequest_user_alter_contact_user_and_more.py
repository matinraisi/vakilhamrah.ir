# Generated by Django 4.2.17 on 2024-12-30 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0001_initial'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billrequest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.profile'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.profile'),
        ),
        migrations.AlterField(
            model_name='lawyer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.profile'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
