# Generated by Django 5.0 on 2023-12-06 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter the title for your blog post', max_length=100)),
                ('publish_date', models.DateField()),
                ('body', models.TextField(help_text='Enter the content for your blog post')),
            ],
        ),
    ]