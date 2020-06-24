from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from taxi.models import Car, Report, TO_History


def get_report(request):
    if request.method == 'POST':
        print(request)
        return HttpResponse(request)
