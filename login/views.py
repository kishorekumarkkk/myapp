from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from login.models import User
from login.serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = User.objects.all()
        data = self.serializer_class(queryset, many=True).data
        return Response(data)

    def create(self, request, *args, **kwargs):
        data = request.data
        u = User.objects.create(first_name=data['first_name'], last_name=data['last_name'], email=data['email'])
        u.save()
        return Response(data)

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = User.objects.get(pk=pk)
        serializer = UserSerializer(queryset).data
        return Response(serializer)

    def destroy(self, request, pk=None, *args, **kwargs):
        query = User.objects.filter(id=pk).delete()
        return Response(True)
