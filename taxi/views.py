from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from taxi.models import Car, Report, TO_History
from rest_framework import viewsets
from taxi.serializers import ReportSerializer


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
# AssertionError at /reports/
# 'ReportViewSet' should either include a `serializer_class` attribute,
# or override the `get_serializer_class()` metho


# def get_report(request):
#     if request.method == 'POST':
#         print(request)
#         return HttpResponse(request)
