from django.db.models import QuerySet
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from main.models import Bb
from .serializers import BbSerializer


@api_view(['GET'])
def bbs(request):
    if request.method == 'GET':
        bbs: QuerySet[Bb] = Bb.objects.filter(is_active=True)[:10]
        serializer = BbSerializer(bbs, many=True)
        return Response(serializer.data)
