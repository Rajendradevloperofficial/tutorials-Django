"""
ASGI config for ludomission project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
from django.conf.urls import url
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ludomission.settings")
django_asgi_app = get_asgi_application()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from game import consumers


ws_pattern= [
    path('ws/tableData/<username>',consumers.TableData),
    path('ws/allgames/' , consumers.AllGames),
    path('ws/room/' , consumers.Room),
    path('ws/game/room/<room_name>' , consumers.ChatConsumer),
    path('ws/join/' , consumers.JoinRequest),
    path('ws/running' , consumers.FakeGames)
]

application= ProtocolTypeRouter(
   
    {
        #"http": django_asgi_app,
        'websocket':AuthMiddlewareStack(URLRouter(ws_pattern))
    }
)