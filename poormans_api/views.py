import datetime

from rest_framework.response import Response
from rest_framework import generics, status
from .models import Tweets
from .serializers import TweetsSerializer


class TweetsView(generics.ListCreateAPIView):
    queryset = Tweets.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset().order_by('-dt', 'name')
        serializer = TweetsSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = TweetsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

