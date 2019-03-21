import graphene

from graphene_django import DjangoObjectType
from django.apps import apps
from django.contrib.auth import get_user_model
from .types import create_types
from .query import create_query


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
        exclude_fields = ('password')


def create_schema(app_name, exclude=[], expose_user=True):

    class_dictionary = apps.get_app_config(app_name).models

    types = create_types(class_dictionary, exclude)

    if expose_user:
        types.append(UserType)

    query = create_query(types)
    print(dir(query))

    return graphene.Schema(query=query, types=types)
