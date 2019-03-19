from django.contrib import admin
from graphql_django.server.models import Post, Comment

admin.site.register(Comment)
admin.site.register(Post)
