# Generated by Django 4.2.11 on 2024-03-21 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_comment_options_alter_post_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='field_2',
            field=models.IntegerField(default=42),
        ),
        migrations.AddField(
            model_name='post',
            name='field_3',
            field=models.CharField(null=True),
        ),
    ]
