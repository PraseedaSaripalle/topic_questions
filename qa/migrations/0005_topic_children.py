# Generated by Django 3.2.9 on 2022-03-06 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0004_remove_topic_children'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='children',
            field=models.ManyToManyField(blank=True, null=True, to='qa.Topic'),
        ),
    ]
