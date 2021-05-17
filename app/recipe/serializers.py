from rest_framework import serializers
from core.models import Tag, Ingredient


class TagSerializer(serializers.ModelSerializer):
    """serializer for the tag object"""

    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only_fields = ['id']


class IngredientSerializer(serializers.ModelSerializer):
    """serializer for the ingredient object"""

    class Meta:
        model = Ingredient
        fields = ['id', 'name']
        read_only_fields = ['id']
