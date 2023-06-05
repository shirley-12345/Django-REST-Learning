from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from tutorial import snippets
from tutorial.snippets import serializers

# views about snippet list
@csrf_exempt
def snippet_list(request):
    if request.method=='GET':
        snippets = Snippet.objects.all()
        # by setting many = true, the queryset contains multiple items
        # drf need to serialize each item with serializer with serializer class
        # serializer.data will be a list
        serializer = SnippetSerializer(snippets, many=True)
        # makes JSON accept both {Dictionaries} and others
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
# views about snippet_detail
@csrf_exempt
def snippet_detail(request,pk):
    try:
        snippet =Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)
    