# Generated by Django 3.2.9 on 2022-03-06 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0005_topic_children'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='children',
            field=models.ManyToManyField(blank=True, null=True, related_name='topic_children', to='qa.Topic'),
        ),
    ]