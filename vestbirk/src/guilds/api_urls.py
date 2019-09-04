from django.urls import path
from guilds.views import index, guild_by_id

urlpatterns = [
    path('', index, name='all_guilds'),
    path('<int:id>', guild_by_id),
]
