# Generated by Django 2.1.3 on 2019-01-16 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DZ1', '0003_auto_20190116_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='./static/photo'),
        ),
    ]