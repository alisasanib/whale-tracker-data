# from requests import api
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TransactionSerializer
from .models import TransactionModel
from django.shortcuts import get_object_or_404
from django.core import management
import requests
from time import time

# management.call_command('seed')


class TransactionViews(APIView):
    def delete(self, request, id=None):
        item = get_object_or_404(TransactionModel, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})

    def patch(self, request, id=None):
        item = TransactionModel.objects.get(id=id)
        serializer = TransactionSerializer(
            item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def get(self, request, id=None):
        if id:
            item = TransactionModel.objects.get(id=id)
            serializer = TransactionSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = TransactionModel.objects.all()
        serializer = TransactionSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def _get_whale_data(self):
        url = "https://api.whale-alert.io/v1/transactions"
        timestamp = int(time()) - 60
        api_key = 'krFJYgcYCcsuYOGFpxV6FOooanzIB71v'
        min_value = 500000
        external_api_url = f'{url}?api_key={api_key}&min_value={min_value}&start={timestamp}'

        api_request = requests.get(external_api_url)
        newRes = api_request.json()
        print('newRes', newRes)

        try:
            api_request.raise_for_status()
            return api_request.json()
        except:
            return None

    def save_whale_data(self):
        
        # [{"blockchain": "test new one", "symbol": "1",
        #             "transaction_type": "2", "hash": "2"}]
        print('save')
        whale_data = self._get_whale_data()
        newData = whale_data["transactions"]
        print("weather_data")
        if newData is not None:
            for newEl in newData:
                try:
                    print('newel', newEl)
                    weather_object = TransactionModel.objects.create(
                        blockchain=newEl["blockchain"], symbol=newEl["symbol"], transaction_type=newEl["transaction_type"], hash=newEl["hash"])
                    whale_data.save()
                except:
                    pass
