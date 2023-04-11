from graphene_django.utils.testing import GraphQLTestCase
from mixer.backend.django import mixer
import graphene
import json

# Create your tests here.

from liquors.schema import schema
from liquors.models import Liquor

LIQUORS_QUERY = '''
{
  liquors{
    id,
    destilado,
    nombre,
    description
  }
}
'''

class LiquorTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    def setUp(self):
        self.liquor1 = mixer.blend(Liquor)
        self.liquor2 = mixer.blend(Liquor)
    
    def test_liquors_query(self):
        response = self.query(
            LIQUORS_QUERY,
        )


        content = json.loads(response.content)
        # print(content)
        self.assertResponseNoErrors(response)
        print("query liquors results ")
        print(content)
        assert len(content['data']['liquors']) == 2