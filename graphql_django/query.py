import graphene


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


def create_query(types):
    print("self")
    attributes = {}
    for class_type in types:
        model_class = class_type._meta.model
        list_arguments = {}

        for field in model_class._meta.fields:
            if field.unique:
                list_arguments[field.name] = graphene.String()

        list_name = str(model_class._meta.verbose_name_plural)
        attributes[list_name] = graphene.List(class_type)

        resolve_list_name = 'resolve_%s' % list_name
        resolve_list = make_resolver_list(list_name, model_class)
        attributes[resolve_list_name] = resolve_list

        field_name = str(model_class._meta.verbose_name)
        field = graphene.Field(class_type, args=list_arguments)
        attributes[field_name] = field

        resolve_field_name = 'resolve_%s' % field_name
        resolve_field = make_resolver_record(field_name, model_class)
        attributes[resolve_field_name] = resolve_field

    return type("Query", (graphene.ObjectType, ), attributes)
