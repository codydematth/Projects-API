from rest_framework import serializers
from .models import Post

# Serialiser Class-------------------------

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = '__all__'
        