import json
from django.core.management.base import BaseCommand
from crypto.models import Crypto, Network


class Command(BaseCommand):
    help = 'Load crypto data from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str)

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']
        with open(json_file, 'r') as file:
            data = json.load(file)

            for item in data:
                networks = Network.objects.filter(slug__in=item['networks'])
                crypto, created = Crypto.objects.update_or_create(
                    title=item['title'],
                    full_name=item['full_name'],
                    defaults={
                        'content': item['content'],
                    }
                )
                crypto.networks.set(networks)
                self.stdout.write(self.style.SUCCESS(f'Processed crypto: {item["title"]}'))
