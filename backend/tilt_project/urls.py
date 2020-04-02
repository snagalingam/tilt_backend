import os

from django.contrib import admin
from django.urls import path, re_path
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from graphene_django.views import GraphQLView

ENVIRONMENT = os.environ.get('ENVIRONMENT', default='production')

if ENVIRONMENT == 'development':
    urlpatterns = [
        path('teamtilt', admin.site.urls),
        path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    ]

if ENVIRONMENT == 'production':
    urlpatterns = [
        path('teamtilt', admin.site.urls),
        path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
        re_path(".*", TemplateView.as_view(template_name="index.html")),
    ]
