from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response


class IndexAPI(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            "name": "John",
            "age": 17,
            }
        return Response(data)


# def index(request):
    # data = {
    #     "name": "John",
    #     "age": 17,
    # }
    # return JsonResponse(data)