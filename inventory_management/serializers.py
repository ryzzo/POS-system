from rest_framework import serializers

class CategorySerializers(serializers.ModelSerializer):
    id = serializers.integer