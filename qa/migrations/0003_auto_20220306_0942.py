# Generated by Django 3.2.9 on 2022-03-06 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0002_auto_20220305_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=1000)),
                ('grade', models.CharField(choices=[('E', 'excellent'), ('G', 'good'), ('A', 'average'), ('P', 'poor')], default='E', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=200)),
                ('children', models.ManyToManyField(to='qa.Topic')),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.AddField(
            model_name='question',
            name='topics',
            field=models.ManyToManyField(related_name='topic_questions', to='qa.Topic'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa.question'),
        ),
    ]
