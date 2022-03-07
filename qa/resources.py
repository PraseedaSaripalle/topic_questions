
from . models import Person

class PersonResource(resources.ModelResource):
    class meta:
        models=Person