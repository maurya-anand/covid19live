from django.shortcuts import render
import requests
from django.http import JsonResponse
import json
from datetime import datetime, timedelta

# Create your views here.
def index(request):
    return render(request, "index.html")