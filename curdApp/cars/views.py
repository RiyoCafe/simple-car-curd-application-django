from django.shortcuts import render, redirect
from .models import Cars
from .serializers import CarsSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import json

def list_cars(request):
    items = Cars.objects.all()
    serializer = CarsSerializer(items, many=True)
    data = {
        "status": "success",
        "data": serializer.data
    }
    return JsonResponse(data, status=200)

def get_car_by_id(request, id):
    try:
        item = Cars.objects.get(id=id)
    except Cars.DoesNotExist:
        return JsonResponse({"status": "error", "data": "Car not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = CarsSerializer(item)
    data = {
        "status": "success",
        "data": serializer.data
    }
    return JsonResponse(data, status=200)

@csrf_exempt
def add_car(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        serializer = CarsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return redirect('list_cars')
            # return JsonResponse({"status": "success", "data": serializer.data}, status=200)
        return JsonResponse({"status": "error", "data": serializer.errors}, status=400)
    

# define update_car function using patch method
@csrf_exempt
def update_car(request, id):
    try:
        item = Cars.objects.get(id=id)
    except Cars.DoesNotExist:
        return JsonResponse({"status": "error", "data": "Car not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PATCH':
        data = json.loads(request.body)
        serializer = CarsSerializer(item, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return redirect('list_cars')
            # return JsonResponse({"status": "success", "data": serializer.data}, status=200)
        return JsonResponse({"status": "error", "data": serializer.errors}, status=400)
@csrf_exempt
def delete_car(request, id):
    try:
        item = Cars.objects.get(id=id)
    except Cars.DoesNotExist:
        return JsonResponse({"status": "error", "data": "Car not found"}, status=status.HTTP_404_NOT_FOUND)
    
    item.delete()
    return redirect('list_cars')
    #return JsonResponse({"status": "success", "data": "Car deleted successfully"}, status=200)