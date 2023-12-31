# Generated by Django 4.2.3 on 2023-10-15 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales_app', '0004_salesperson_img_salesperson_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('is_admin', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='salesperson',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='salesperson',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='salesperson',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='salesperson',
            name='password',
        ),
        migrations.RemoveField(
            model_name='salesperson',
            name='token',
        ),
        migrations.RemoveField(
            model_name='salesperson',
            name='username',
        ),
        migrations.AddField(
            model_name='salesperson',
            name='REGION_CHOICES',
            field=models.CharField(choices=[('northern', 'northern'), ('southern', 'southern'), ('coastal', 'coastal'), ('lebanese', 'lebanese')], default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='salesperson',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='salesperson',
            name='img',
            field=models.FileField(upload_to='img'),
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=50)),
                ('northern', models.FloatField(default=0)),
                ('southern', models.FloatField(default=0)),
                ('coastal', models.FloatField(default=0)),
                ('lebanese', models.FloatField(default=0)),
                ('financial', models.FloatField(default=0)),
                ('sales_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales_app.salesperson')),
            ],
        ),
    ]
