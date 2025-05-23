# Generated by Django 5.2 on 2025-04-26 12:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bartender',
            new_name='Employee',
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Работник', 'verbose_name_plural': 'Работники'},
        ),
        migrations.AlterUniqueTogether(
            name='desiredtimeoff',
            unique_together=set(), 
        ),
        migrations.AlterUniqueTogether(
            name='worksummary',
            unique_together=set(), 
        ),
        migrations.AddField(
            model_name='desiredtimeoff',
            name='employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='desired_time_off', to='scheduler.employee', verbose_name='Работник'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shift',
            name='employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='shifts', to='scheduler.employee', verbose_name='Работник'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worksummary',
            name='employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='work_summaries', to='scheduler.employee', verbose_name='Работник'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='shift',
            name='bartender',
        ),
        migrations.RemoveField(
            model_name='desiredtimeoff',
            name='bartender',
        ),
        migrations.RemoveField(
            model_name='worksummary',
            name='bartender',
        ),
        migrations.AlterUniqueTogether(
            name='desiredtimeoff',
            unique_together={('employee', 'date')},
        ),
        migrations.AlterUniqueTogether(
            name='worksummary',
            unique_together={('employee', 'month')},
        ),
    ]
