from django import template
from django.db.models import Count

from crypto.models import Network

register = template.Library()


@register.inclusion_tag('crypto/list_networks.html')
def show_networks(network_selected=0):
    networks = Network.objects.annotate(total=Count("networks")).filter(total__gt=0)
    return {'networks': networks, 'network_selected': network_selected}

