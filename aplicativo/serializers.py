from rest_framework import serializers
from .models import Item,Category, User

class itemSerializer(serializers.ModelSerializer):

    class Meta:
        model=Item
        fields='__all__'


class categorySerializer(serializers.ModelSerializer):

    class Meta:
        model=Category
        fieds=('ct_name','ct_id')


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model=User 
        fiels='__all__'
        