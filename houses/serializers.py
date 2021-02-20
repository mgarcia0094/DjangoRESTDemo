from rest_framework import serializers
from houses.models import House

"""
FIRST WAY CREATE SERIALIZER
class HouseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, allow_null=False, max_length=100)
    more_info = serializers.CharField(style={'base_template':'textarea.html'})
    m2 = serializers.IntegerField(required=True, allow_null=False)
    num_bathrooms = serializers.IntegerField(required=True, allow_null=False)
    num_bedrooms = serializers.IntegerField(required=True, allow_null=False)
    garden = serializers.BooleanField(required=True, allow_null=False)

    def create(self, validated_data):
        return House.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.more_info = validated_data.get('more_info', instance.more_info)
        instance.m2 = validated_data.get('m2', instance.m2)
        instance.num_bathrooms = validated_data.get('num_bathrooms', instance.num_bathrooms)
        instance.num_bedrooms = validated_data.get('num_bedrooms', instance.num_bedrooms)
        instance.garden = validated_data.get('garden', instance.garden)
        instance.save()
        return instance
"""

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['id', 'name', 'more_info', 'm2', 'num_bathrooms', 'num_bedrooms', 'garden', 'owner']

