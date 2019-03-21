from graphene_django import DjangoObjectType


def create_types(class_dictionary, exclude):
    types = []

    exclude_lower = [x.lower() for x in exclude]

    for key, model_class in class_dictionary.items():
        if key not in exclude_lower:
            properties = {"model": model_class}
            meta = type("Meta", (), properties)

            name = key.capitalize() + 'Type'
            props = {"Meta": meta}
            djangoObjectType = type(name, (DjangoObjectType, ), props)

            types.append(djangoObjectType)
    return types
