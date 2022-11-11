import mysql.connector as msql

from mysql.connector import Error
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    
    help = 'Test connection MySQL DB'

    def handle(self, *args, **options):
        try:
            conn = msql.connect(host='localhost', user='root',
                                password='Pernec#123')
            if conn.is_connected():
                print("Connection success!")

        except Error as e:
            print("Error while connecting to MySQL", e)