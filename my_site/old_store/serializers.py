from rest_framework import serializers
from .models import Product


class Productserializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "pk",
            "name",
            "discription",
            "price",
            "discount",
            "created_at",
            "archived",
            "preview",
        )

        # можно написать ("__all__")
