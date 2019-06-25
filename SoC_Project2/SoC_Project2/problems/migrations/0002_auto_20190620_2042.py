# Generated by Django 2.2.2 on 2019-06-20 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weeklychallenges',
            name='constraints',
            field=models.TextField(default='SOME STRING'),
        ),
        migrations.AddField(
            model_name='weeklychallenges',
            name='input_format',
            field=models.TextField(default='SOME STRING'),
        ),
        migrations.AddField(
            model_name='weeklychallenges',
            name='output_format',
            field=models.TextField(default='SOME STRING'),
        ),
        migrations.AlterField(
            model_name='weeklychallenges',
            name='problem_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
