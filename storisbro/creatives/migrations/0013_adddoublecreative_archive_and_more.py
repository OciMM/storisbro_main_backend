# Generated by Django 5.0 on 2024-02-16 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creatives', '0012_adddoublecreative_creative_type_and_more'),
        ('reservation', '0003_delete_creativemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='adddoublecreative',
            name='archive',
            field=models.BooleanField(default=False, verbose_name='статус архива'),
        ),
        migrations.AddField(
            model_name='adddoublecreative',
            name='reservation',
            field=models.ManyToManyField(blank=True, to='reservation.dateofreservation', verbose_name='Бронирование'),
        ),
        migrations.AddField(
            model_name='addsinglecreative',
            name='archive',
            field=models.BooleanField(default=False, verbose_name='статус архива'),
        ),
        migrations.AddField(
            model_name='doublestickercreative',
            name='archive',
            field=models.BooleanField(default=False, verbose_name='статус архива'),
        ),
        migrations.AddField(
            model_name='doublestickercreative',
            name='reservation',
            field=models.ManyToManyField(blank=True, to='reservation.dateofreservation', verbose_name='Бронирование'),
        ),
        migrations.AddField(
            model_name='repostcreative',
            name='archive',
            field=models.BooleanField(default=False, verbose_name='статус архива'),
        ),
        migrations.AddField(
            model_name='repostcreative',
            name='reservation',
            field=models.ManyToManyField(blank=True, to='reservation.dateofreservation', verbose_name='Бронирование'),
        ),
        migrations.AddField(
            model_name='stickercreative',
            name='archive',
            field=models.BooleanField(default=False, verbose_name='статус архива'),
        ),
        migrations.AddField(
            model_name='stickercreative',
            name='reservation',
            field=models.ManyToManyField(blank=True, to='reservation.dateofreservation', verbose_name='Бронирование'),
        ),
    ]
