# Generated by Django 4.2.3 on 2023-10-15 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_app', '0005_user_remove_salesperson_is_admin_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
