import os

from django.contrib import admin
from django.urls import path, re_path, include
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from graphene_django.views import GraphQLView
from .views import index, logout_view

ENVIRONMENT = os.environ.get('ENVIRONMENT', default='production')

if ENVIRONMENT == 'development':
    urlpatterns = [
        path("", index),
        path("signup", index),
        path("dashboard", index),
        path("logout", logout_view),
        path("teamtilt", admin.site.urls),
        path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    ]

if ENVIRONMENT == 'production':
    urlpatterns = [
        path("teamtilt", admin.site.urls),
        path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
        path("robots.txt", TemplateView.as_view(
            template_name="robots.txt", content_type="text/plain")),
        path("sitemap.xml", TemplateView.as_view(
            template_name="sitemap.xml", content_type="text/plain")),
        re_path(".*", TemplateView.as_view(template_name="index.html")),
    ]
