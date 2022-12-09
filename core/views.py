from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import json
# Create your views here.


@csrf_exempt ## To exempt from default requirement for CSRF tokens to use postman
def TheModelView(request):

    if (request.method == "GET"):
        data = {"key1": "value1", "key2": "value2"}
        json_object = json.dumps(data, indent=3)
        return HttpResponse(json_object)