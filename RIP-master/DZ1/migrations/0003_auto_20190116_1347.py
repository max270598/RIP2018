# Generated by Django 2.1.3 on 2019-01-16 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DZ1', '0002_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='.static/photo'),
        ),
    ]

{% if atlets %}
numre:{{atlets|lenght}}
{%endif%}
{% for i in innn %}
<h1>{{i.name}}</h1>
{%endfor%}
