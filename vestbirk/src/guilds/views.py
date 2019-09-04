from django.shortcuts import get_object_or_404
from django.core import serializers

from vestbirk.utils import json_response
from guilds.models import Guild

# Create your views here.

def index(request):
    guilds = Guild.objects.all()
    data = serializers.serialize('json', guilds, fields=('title', 'short_text', 'id'))
    return json_response(data)

def guild_by_id(request, id):
    guild = get_object_or_404(Guild, id=id)
    return json_response(guild.as_dict())
