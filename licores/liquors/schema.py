import graphene
from graphene_django import DjangoObjectType

from .models import Liquor


class LiquorType(DjangoObjectType):
    class Meta:
        model = Liquor


class Query(graphene.ObjectType):
    liquors = graphene.List(LiquorType)

    def resolve_liquors(self, info, **kwargs):
        return Liquor.objects.all()