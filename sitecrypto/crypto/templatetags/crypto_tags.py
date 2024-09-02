from django import template

from crypto.models import Network

register = template.Library()


@register.inclusion_tag('crypto/list_networks.html')
def show_networks(network_selected=0):
    networks = Network.objects.all()
    return {'networks': networks, 'network_selected': network_selected}

