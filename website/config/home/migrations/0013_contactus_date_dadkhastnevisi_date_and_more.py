# Generated by Django 4.2.17 on 2025-01-03 17:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0001_initial'),
        ('home', '0012_dadkhastcaregory_dadkhastnevisi_delete_billrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dadkhastnevisi',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dadkhastnevisi',
            name='file',
            field=models.FileField(default=1, upload_to='dadkhast_request'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dadkhastnevisi',
            name='subject',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lawyer',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='SabtMoshavere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Authentication.profile')),
            ],
        ),
    ]
