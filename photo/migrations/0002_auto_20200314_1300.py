# Generated by Django 3.0.4 on 2020-03-14 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photolog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=100, verbose_name='One Line Description')),
                ('content', models.TextField(blank=True, verbose_name='Photolog')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('modify_dt', models.DateTimeField(auto_now=True, verbose_name='Modify Date')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.RemoveField(
            model_name='photo',
            name='album',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.AddField(
            model_name='photo',
            name='photolog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='photo.Photolog'),
        ),
    ]
