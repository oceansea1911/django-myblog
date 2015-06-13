# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_time', models.DateTimeField(auto_now=True)),
                ('ip', models.IPAddressField()),
                ('comment_parent', models.IntegerField()),
                ('content', models.TextField()),
                ('article', models.ForeignKey(to='blog.Article')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Critic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=75, blank=True)),
                ('website', models.URLField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comment',
            name='critic',
            field=models.ManyToManyField(to='blog.Critic'),
            preserve_default=True,
        ),
        migrations.RenameField(
            model_name='article',
            old_name='tag',
            new_name='tags',
        ),
    ]
