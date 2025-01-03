# Generated by Django 5.1.4 on 2025-01-02 14:05

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_category_legalfiles'),
    ]

    operations = [
        migrations.CreateModel(
            name='LegalCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name='Category',
            new_name='LawyerType',
        ),
        migrations.RemoveField(
            model_name='lawyer',
            name='subject_type',
        ),
        migrations.AddField(
            model_name='lawyer',
            name='lawyer_type',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='home.lawyertype'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lawyer',
            name='experience',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='qaa',
            name='subject_type',
            field=models.CharField(choices=[('fa', 'خانوادگی'), ('ju', 'قضایی'), ('ma', 'مدنی'), ('je', 'جنایی'), ('ot', 'سایر')], max_length=100),
        ),
        migrations.AlterField(
            model_name='legalfiles',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.legalcategory'),
        ),
    ]
