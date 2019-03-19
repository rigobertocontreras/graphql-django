from graphql_django.server.schema import create_schema
"""
    We can exclude from here ex:
    schema = create_schema(exclude=['post'])
"""
schema = create_schema()
