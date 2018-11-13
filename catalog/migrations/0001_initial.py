# Generated by Django 2.1.3 on 2018-11-13 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Broadcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('examination_start', models.DateTimeField(null=True)),
                ('examination_end', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BroadcastLesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('broadcast', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.Broadcast')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kana', models.CharField(max_length=255, null=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='broadcast',
            name='teachers',
            field=models.ManyToManyField(to='catalog.Teacher'),
        ),
    ]