# Generated by Django 2.1.7 on 2019-02-20 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('userName', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('hostName', models.TextField()),
                ('githubUrl', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField()),
                ('regected', models.BooleanField(default=False)),
                ('from_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_request_sent', to='Author.Author')),
                ('to_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_request_recieved', to='Author.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('author1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend1', to='Author.Author')),
                ('author2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend2', to='Author.Author')),
            ],
        ),
    ]
