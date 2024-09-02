import json
from django.core.management.base import BaseCommand
from crypto.models import Network


class Command(BaseCommand):
    help = 'Load networks data from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str)

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']
        with open(json_file, 'r') as file:
            data = json.load(file)

            for item in data:
                network, created = Network.objects.update_or_create(
                    slug=item['title'].lower(),
                    defaults={
                        'title': item['title'],
                        'full_name': item['full_name'],
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created network: {network.id} - {network.title}'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Updated network: {network.id} - {network.title}'))
