import importlib
import graphene

from graphene_django import DjangoObjectType
from django.apps import apps


def dump(obj):
    for attr in dir(obj):
        print("obj.%s = %r" % (attr, getattr(obj, attr)))


def make_resolver_list(record_name, record_cls):
    def resolver(self, info):
        return record_cls.objects.all()
    resolver.__name__ = 'resolve_%s' % record_name
    return resolver


def make_resolver_record(record_name, record_cls):
    def resolver(self, info, **kwargs):
        try:
            record = record_cls.objects.get(**kwargs)
        except record_cls.DoesNotExist:
            record = None
        return record
    resolver.__name__ = 'resolve_%s' % record_name
    return resolver


def create_schema(exclude=[]):
    module = importlib.import_module('graphql_django.server.models')
    # print("dir", dir(module))
    app = apps.all_models['server']
    record_schemas = {}
    for content_type in app:
        if(content_type not in exclude):
            model_class = getattr(module, content_type.capitalize())
            name = content_type
            record_schemas[name] = model_class

    fields = {}
    types = []
    for key, model_class in record_schemas.items():
        properties = {}
        properties["model"] = model_class

        meta = type("Meta", (), properties)
        typeName = key + 'Type'
        listName = model_class._meta.verbose_name_plural
        t = type(typeName, (DjangoObjectType, ), {"Meta": meta})
        types.append(t)

        # fields[listName] = graphene.List(t)
        list_arguments = {}
        for field in model_class._meta.fields:
            if field.unique:
                list_arguments[field.name] = graphene.String()

        resolve_list_name = 'resolve_%s' % listName
        fields[resolve_list_name] = make_resolver_list(listName, model_class)
        fields[listName] = graphene.List(t)

        fields[key] = graphene.Field(t, args=list_arguments)
        fields['resolve_%s' % key] = make_resolver_record(key, model_class)

    Query = type('Query', (graphene.ObjectType,), fields)

    return graphene.Schema(query=Query, types=types)


schema = create_schema()
