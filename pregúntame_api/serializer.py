from rest_framework import serializers
from Pregúntame.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'context',
            'user',
            'status'
        )
