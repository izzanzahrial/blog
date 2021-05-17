from django.shortcuts import render
from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from .models import Repository
from .serializer import RepositorySerializer

# Create your views here.
class RepositoryViewSet(viewsets.ViewSet):
    def list(self, request):
        repository = Repository.objects.all()
        serializer = RepositorySerializer(repository, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = RepositorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        repository = Repository.objects.get(repo_id=pk)
        serializer = RepositorySerializer(repository)
        return Response(serializer.data)

    def update(self, request, pk=None):
        repository = Repository.objects.get(repo_id=pk)
        serializer = RepositorySerializer(instance=repository, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        repository = Repository.objects.get(repo_id=pk)
        repository.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
