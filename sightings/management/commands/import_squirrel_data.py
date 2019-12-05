from django.core.management.base import BaseCommand, CommandError
from sightings.models import Squirrel
import csv

# reference: https://docs.djangoproject.com/en/2.2/howto/custom-management-commands/
class Command(BaseCommand):
    help = 'A command that can be used to import the data from a given path'

    def add_arguments(self, parser):
        parser.add_argument('path',help='/path/to/file.csv',type=str)

    def handle(self, *args, **options):
        path = options['path']
        # reference: https://stackoverflow.com/questions/2459979/how-to-import-csv-data-into-django-models
        with open(path) as f:
            reader = csv.reader(f)
            first_row = 1

            for row in reader:

                if first_row == 1:
                    first_row =0
                    continue

                _, created = Squirrel.objects.get_or_create(
                    longitude = float(row[0]),
                    latitude = float(row[1]),
                    squirrel_id = row[2],
                )
            # creates a tuple of the new object or
            # current object and a boolean of if it was created


        self.stdout.write(self.style.SUCCESS('Successfully import data from "%s"' % path))
