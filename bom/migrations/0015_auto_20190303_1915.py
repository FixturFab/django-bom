# Generated by Django 2.1.5 on 2019-03-03 19:15

from django.db import migrations, models
import django.db.models.deletion


def update_partchangehistory(apps, schema_editor):
    PartChangeHistory = apps.get_model('bom', 'PartChangeHistory')

    for pch in PartChangeHistory.objects.all():
        pch.description = pch.old_description
        pch.revision = pch.old_revision
        pch.value = pch.new_value
        pch.save()


class Migration(migrations.Migration):
    dependencies = [
        ('bom', '0014_auto_20190223_2353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assembly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='AssemblySubparts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'bom_assembly_subparts',
            },
        ),
        migrations.AddField(
            model_name='assembly',
            name='subparts',
            field=models.ManyToManyField(related_name='assemblies', through='bom.AssemblySubparts', to='bom.Subpart'),
        ),
        migrations.AddField(
            model_name='assemblysubparts',
            name='assembly',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bom.Assembly'),
        ),
        migrations.AddField(
            model_name='assemblysubparts',
            name='subpart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bom.Subpart'),
        ),
        migrations.AlterUniqueTogether(
            name='assemblysubparts',
            unique_together={('assembly', 'subpart')},
        ),
        # migrations.AddField(
        #     model_name='assembly',
        #     name='subparts',
        #     field=models.ManyToManyField(to='bom.Subpart', related_name='assemblies'),
        # ),
        migrations.RemoveField(
            model_name='partfile',
            name='part',
        ),
        migrations.DeleteModel(
            name='PartFile',
        ),
        migrations.RenameField(
            model_name='partchangehistory',
            old_name='attribute_time_stamp',
            new_name='timestamp',
        ),
        migrations.AddField(
            model_name='partchangehistory',
            name='description',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='partchangehistory',
            name='revision',
            field=models.CharField(db_index=True, max_length=2),
        ),
        migrations.AddField(
            model_name='partchangehistory',
            name='value',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='partchangehistory',
            name='attribute',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='partchangehistory',
            name='assembly',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT,
                                    to='bom.Assembly'),
        ),
        migrations.RemoveField(
            model_name='partchangehistory',
            name='original_value',
        ),
        migrations.RemoveField(
            model_name='partchangehistory',
            name='old_number_item',
        ),
        migrations.RemoveField(
            model_name='partchangehistory',
            name='old_number_variation',
        ),
        migrations.RemoveField(
            model_name='partchangehistory',
            name='old_time_stamp',
        ),
        migrations.RunPython(update_partchangehistory),
        migrations.RemoveField(
            model_name='partchangehistory',
            name='new_value',
        ),
        migrations.RemoveField(
            model_name='partchangehistory',
            name='old_description',
        ),
        migrations.RemoveField(
            model_name='partchangehistory',
            name='old_revision',
        ),
        migrations.AddField(
            model_name='subpart',
            name='part_revision',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='assembly_subpart', to='bom.PartChangeHistory'),
        )
    ]
