# Generated by Django 2.2.1 on 2019-06-02 01:53

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('callyourmoms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PodcastIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('index_page_content', wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='memberdetailpage',
            name='best_finnish',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='memberdetailpage',
            name='playoffs_made',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='memberdetailpage',
            name='playoffs_won',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='memberdetailpage',
            name='profile_image',
            field=models.ForeignKey(blank=True, help_text='thumb nail images will be rendered 100 x 100 px', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='memberdetailpage',
            name='weekly_win_total',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.CreateModel(
            name='PodcastDetailPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('description', models.CharField(max_length=250)),
                ('week', models.CharField(blank=True, choices=[('undefined', 'UNDEFINED'), ('Week 1', 'WEEK-ONE'), ('Week 2', 'WEEK-TWO'), ('Week 3', 'WEEK-THREE'), ('Week 4', 'WEEK-FOUR'), ('Week 5', 'WEEK-FIVE'), ('Week 6', 'WEEK-SIX'), ('Week 7', 'WEEK-SEVEN'), ('Week 8', 'WEEK-EIGHT'), ('Week 9', 'WEEK-NINE'), ('Week 10', 'WEEK-TEN'), ('Week 11', 'WEEK-ELEVON'), ('Week 12', 'WEEK-TWELVE'), ('Week 13', 'WEEK-THIRTEEN'), ('Playoffs QuarterFinals', 'PLAYOFFS-QUARTERFINALS'), ('Playoffs SemiFinals', 'PLAYOFFS-SEMIFINALS'), ('Playoffs Championship', 'PLAYOFFS-CHAMPIONSHIP'), ('Pre-Season', 'PRE-SEASON'), ('Off-Season', 'OFF-SEASON'), ('Post-Season', 'POST-SEASON')], max_length=50, null=True)),
                ('authors', models.ManyToManyField(to='callyourmoms.Author')),
                ('thumbnail_image', models.ForeignKey(blank=True, help_text='thumb nail images will be rendered 200 x 200 px', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('year', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='callyourmoms.YearTag')),
            ],
            options={
                'verbose_name': 'Podcast',
                'verbose_name_plural': 'Podcasts',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='articledetailpage',
            name='authors',
            field=models.ManyToManyField(to='callyourmoms.Author'),
        ),
    ]