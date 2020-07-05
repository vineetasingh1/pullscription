# Generated by Django 3.0.6 on 2020-06-02 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diamd_no', models.CharField(blank=True, db_column='DIAMD_NO', max_length=10, null=True)),
                ('stock_no', models.CharField(blank=True, db_column='STOCK_NO', max_length=9, null=True)),
                ('parent_item_no_alt', models.CharField(blank=True, db_column='PARENT_ITEM_NO_ALT', max_length=9, null=True)),
                ('bounce_use_item', models.CharField(blank=True, db_column='BOUNCE_USE_ITEM', max_length=20, null=True)),
                ('full_title', models.CharField(blank=True, db_column='FULL_TITLE', max_length=255, null=True)),
                ('main_desc', models.CharField(blank=True, db_column='MAIN_DESC', max_length=255, null=True)),
                ('variant_desc', models.CharField(blank=True, db_column='VARIANT_DESC', max_length=255, null=True)),
                ('series_code', models.IntegerField(blank=True, db_column='SERIES_CODE', null=True)),
                ('issue_no', models.IntegerField(blank=True, db_column='ISSUE_NO', null=True)),
                ('issue_seq_no', models.IntegerField(blank=True, db_column='ISSUE_SEQ_NO', null=True)),
                ('volume_tag', models.IntegerField(blank=True, db_column='VOLUME_TAG', null=True)),
                ('max_issue', models.CharField(blank=True, db_column='MAX_ISSUE', max_length=255, null=True)),
                ('price', models.DecimalField(blank=True, db_column='PRICE', decimal_places=0, max_digits=65, null=True)),
                ('publisher', models.CharField(blank=True, db_column='PUBLISHER', max_length=255, null=True)),
                ('upc_no', models.CharField(blank=True, db_column='UPC_NO', max_length=255, null=True)),
                ('short_isbn_no', models.CharField(blank=True, db_column='SHORT_ISBN_NO', max_length=255, null=True)),
                ('ean_no', models.CharField(blank=True, db_column='EAN_NO', max_length=255, null=True)),
                ('cards_per_pack', models.IntegerField(blank=True, db_column='CARDS_PER_PACK', null=True)),
                ('pack_per_box', models.IntegerField(blank=True, db_column='PACK_PER_BOX', null=True)),
                ('box_per_case', models.IntegerField(blank=True, db_column='BOX_PER_CASE', null=True)),
                ('discount_code', models.CharField(blank=True, db_column='DISCOUNT_CODE', max_length=3, null=True)),
                ('increment', models.IntegerField(blank=True, db_column='INCREMENT', null=True)),
                ('prnt_date', models.DateField(blank=True, db_column='PRNT_DATE', null=True)),
                ('foc_vendor', models.IntegerField(blank=True, db_column='FOC_VENDOR', null=True)),
                ('ship_date', models.DateField(blank=True, db_column='SHIP_DATE', null=True)),
                ('srp', models.DecimalField(blank=True, db_column='SRP', decimal_places=0, max_digits=65, null=True)),
                ('category', models.IntegerField(blank=True, db_column='CATEGORY', null=True)),
                ('genre', models.CharField(blank=True, db_column='GENRE', max_length=255, null=True)),
                ('brand_code', models.CharField(blank=True, db_column='BRAND_CODE', max_length=255, null=True)),
                ('mature', models.IntegerField(blank=True, db_column='MATURE', null=True)),
                ('adult', models.IntegerField(blank=True, db_column='ADULT', null=True)),
                ('oa', models.IntegerField(blank=True, db_column='OA', null=True)),
                ('caut1', models.IntegerField(blank=True, db_column='CAUT1', null=True)),
                ('caut2', models.IntegerField(blank=True, db_column='CAUT2', null=True)),
                ('caut3', models.IntegerField(blank=True, db_column='CAUT3', null=True)),
                ('resol', models.IntegerField(blank=True, db_column='RESOL', null=True)),
                ('note_price', models.IntegerField(blank=True, db_column='NOTE_PRICE', null=True)),
                ('order_form_notes', models.CharField(blank=True, db_column='ORDER_FORM_NOTES', max_length=255, null=True)),
                ('page', models.IntegerField(blank=True, db_column='PAGE', null=True)),
                ('writer', models.CharField(blank=True, db_column='WRITER', max_length=255, null=True)),
                ('artist', models.CharField(blank=True, db_column='ARTIST', max_length=255, null=True)),
                ('cover_artist', models.CharField(blank=True, db_column='COVER_ARTIST', max_length=255, null=True)),
                ('colorist', models.CharField(blank=True, db_column='COLORIST', max_length=255, null=True)),
                ('alliance_sku', models.CharField(blank=True, db_column='ALLIANCE_SKU', max_length=255, null=True)),
                ('foc_date', models.DateField(blank=True, db_column='FOC_DATE', null=True)),
                ('offered_date', models.DateField(blank=True, db_column='OFFERED_DATE', null=True)),
                ('number_of_pages', models.IntegerField(blank=True, db_column='NUMBER_OF_PAGES', null=True)),
                ('unit_weight', models.DecimalField(blank=True, db_column='UNIT_WEIGHT', decimal_places=0, max_digits=50, null=True)),
                ('unit_length', models.DecimalField(blank=True, db_column='UNIT_LENGTH', decimal_places=0, max_digits=50, null=True)),
                ('unit_width', models.DecimalField(blank=True, db_column='UNIT_WIDTH', decimal_places=0, max_digits=50, null=True)),
                ('unit_height', models.DecimalField(blank=True, db_column='UNIT_HEIGHT', decimal_places=0, max_digits=50, null=True)),
                ('case_weight', models.DecimalField(blank=True, db_column='CASE_WEIGHT', decimal_places=0, max_digits=50, null=True)),
                ('case_length', models.DecimalField(blank=True, db_column='CASE_LENGTH', decimal_places=0, max_digits=50, null=True)),
                ('case_width', models.DecimalField(blank=True, db_column='CASE_WIDTH', decimal_places=0, max_digits=50, null=True)),
                ('case_height', models.DecimalField(blank=True, db_column='CASE_HEIGHT', decimal_places=0, max_digits=50, null=True)),
            ],
            options={
                'db_table': 'comics',
                'managed': False,
            },
        ),
    ]