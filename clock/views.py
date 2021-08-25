from django.db.models import query
from django.shortcuts import render
from rest_framework.response import Response
from .models import Notice
from rest_framework.views import APIView
from .serializers import NoticeSerializer
from .parser import parse_notice

# Create your views here.
class NoticeListAPI(APIView):
    def get(self, request):
        Notice.objects.all().delete()
        notice_data_dict = parse_notice()
        for t, d in notice_data_dict.items():
            Notice(title = t, date = d[0], link = d[1]).save()
        queryset = Notice.objects.all()
        print(queryset)
        serializer = NoticeSerializer(queryset, many=True)
        return Response(serializer.data)