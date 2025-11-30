from rest_framework import serializers
from .models import Ingredient, Recipe


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']


class RecipeSerializer(serializers.ModelSerializer):

    ingredients = IngredientSerializer(many=True, read_only=True)
    ingredients_names = serializers.ListField(
        child=serializers.CharField(),
        write_only=True
    )

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'ingredients', 'ingredients_names']

    def create(self, validated_data):
        ingredients = validated_data.pop('ingredients_names', [])
        recipe = Recipe.objects.create(**validated_data)
        for name in ingredients:
            Ingredient.objects.create(name=name, recipe=recipe)

        return recipe
