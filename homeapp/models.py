# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdrssInfo(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    recipient = models.CharField(max_length=20, blank=True, null=True)
    adress = models.CharField(max_length=80, blank=True, null=True)
    zip_code = models.BigIntegerField(blank=True, null=True)
    tel = models.BigIntegerField(db_column='TEL', blank=True, null=True)  # Field name made lowercase.
    phone = models.BigIntegerField(blank=True, null=True)
    pid = models.ForeignKey('User', models.DO_NOTHING, db_column='pid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adrss_info'


class BookClassT(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.CharField(max_length=30, blank=True, null=True)
    pid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_class_t'


class BooksT(models.Model):
    id = models.BigAutoField(primary_key=True)
    book_name = models.CharField(max_length=30, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    author = models.CharField(max_length=20, blank=True, null=True)
    press = models.CharField(max_length=30, blank=True, null=True)
    press_date = models.DateField(blank=True, null=True)
    edition = models.BigIntegerField(blank=True, null=True)
    printing_time = models.DateField(blank=True, null=True)
    impression = models.BigIntegerField(blank=True, null=True)
    isbn = models.CharField(db_column='ISBN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    words = models.BigIntegerField(blank=True, null=True)
    pages = models.BigIntegerField(blank=True, null=True)
    format = models.CharField(max_length=20, blank=True, null=True)
    paper = models.CharField(max_length=20, blank=True, null=True)
    packing = models.CharField(max_length=20, blank=True, null=True)
    dd_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    save = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pid = models.ForeignKey(BookClassT, models.DO_NOTHING, db_column='pid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'books_t'


class OrderItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    book_name = models.CharField(max_length=30, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    count_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    my_or = models.IntegerField(blank=True, null=True)
    pid = models.ForeignKey('Orders', models.DO_NOTHING, db_column='pid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_item'


class Orders(models.Model):
    id = models.BigAutoField(primary_key=True)
    or_num = models.IntegerField(blank=True, null=True)
    recipient = models.CharField(max_length=30, blank=True, null=True)
    adress = models.CharField(max_length=50, blank=True, null=True)
    uid = models.ForeignKey('User', models.DO_NOTHING, db_column='uid', blank=True, null=True)
    aid = models.ForeignKey(AdrssInfo, models.DO_NOTHING, db_column='aid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    pwd = models.CharField(max_length=30, blank=True, null=True)
    nickname = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


