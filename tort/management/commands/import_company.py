import csv

from django.core.management.base import BaseCommand

from ...models import Company

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-p', '--path', type=str, help='path to csv file', )
                
    def handle(self, *args, **kwargs):
        path = kwargs['path']
        file = open(path)
        csvreader = csv.reader(file)
        locations = []
        for row in csvreader:
            locations.append(Company(iata_code=row[0], name=row[1]))

        Company.objects.bulk_create(locations)