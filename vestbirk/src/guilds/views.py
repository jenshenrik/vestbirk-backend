from django.shortcuts import render

#from vestbirk.guilds.models import Guild

# Create your views here.

def index(request):
    return json_response('Hello world!')
    #lguilds = Guild.objects.all()
    #return json_response(guilds)

def guild_by_id(request, id):
    return json_response(id)
