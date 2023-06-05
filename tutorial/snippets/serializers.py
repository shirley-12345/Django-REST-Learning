from operator import truediv
from typing import Required
from rest_framework import serializers
from snippets.models import Snippets,LANGUAGE_CHOICES,STYLE_CHOICES

class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.IntegerField(Required=False)