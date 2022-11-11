# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DataTerminal(models.Model):
    switch_lable = models.CharField(max_length=20)
    terminal_1 = models.IntegerField(blank=True, null=True)
    terminal_2 = models.IntegerField(blank=True, null=True)
    terminal_3 = models.IntegerField(blank=True, null=True)
    terminal_4 = models.IntegerField(blank=True, null=True)
    terminal_5 = models.IntegerField(blank=True, null=True)
    unix_timestamp = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_terminal'
