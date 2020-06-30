import json

from django import template

register = template.Library()

@register.filter
def loadjson(data):
    return json.loads(data)

@register.filter
def index(indexable, i):
    return indexable[i]