from django.db import migrations
import json
from django.contrib.gis.geos import fromstr
from pathlib import Path

DATA_FILENAME = 'hotels.json'
def load_data(apps, schema_editor):
    Hotel = apps.get_model('hotels', 'Hotel')
    jsonfile = Path(__file__).parents[2] / DATA_FILENAME

    with open(str(jsonfile), encoding="utf8") as datafile:
        objects = json.load(datafile)
        for obj in objects['elements']:
            try:
                objType = obj['type']
                if objType == 'node':
                    tags = obj['tags']
                    name = tags.get('name','no-name')
                    longitude = obj.get('lon', 0)
                    latitude = obj.get('lat', 0)
                    location = fromstr(f'POINT({longitude} {latitude})', srid=4326)
                    Hotel(name=name, location=location).save()
            except KeyError:
                pass


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0002_auto_20210821_1617'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]
