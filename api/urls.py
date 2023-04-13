from django.urls import path
from .views import *

urlpatterns= [
    path('users/',UserView.as_view(),name='User_list'),
    path('users/<int:id>',UserView.as_view(),name='User_process'),
    path('assistants/',AsistantView.as_view(),name='Assistant_list'),
    path('assistants/<str:id_voice>',AsistantView.as_view(),name='Assistant_process'),
    path('conversations/',ConversationView.as_view(),name='Conversation_list'),
    path('conversations/<int:id>',ConversationView.as_view(),name='Conversation_process'),
    path('messages/',MessageView.as_view(),name='Message_list'),
    path('messages/<int:id>',MessageView.as_view(),name='Message_process'),
    path('estados/',EstadoView.as_view(),name='Estado_list'),
    path('estados/<int:id>',EstadoView.as_view(),name='Estado_process')
]