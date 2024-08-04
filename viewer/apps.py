from django.apps import AppConfig

import pymysql


class ViewerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'viewer'


db = pymysql.connect(host='localhost', user='root', password='Sanderka25')


print(db)
