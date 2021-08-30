from django.forms.forms import Form
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin
from core.settings import EMAIL_HOST_USER
from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from .models import Repository
from .serializer import RepositorySerializer
from .forms import ContactForm

# Create your views here.
class RepositoryViewSet(LoginRequiredMixin, viewsets.ViewSet):
    login_url = "/account/login/"
    redirect_field_name = "login"

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

def repositoryView(request):
    repositories = Repository.objects.all()
    contact_form2 = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']
            message1 = render_to_string('repository/template.html', {'name':name})
            message2 = f"{name}'s email address = {email}, and this is the message \n\n{message}"
            subject1 = "Thank you for contacting me!"
            subject2 = f"{name} try to contact you!"
            send_email = EmailMessage(
                subject1,
                message1,
                EMAIL_HOST_USER,
                [email],
            )
            send_email2 = EmailMessage(
                subject2,
                message2,
                EMAIL_HOST_USER,
                ['izzanzahrial@gmail.com']
            )
            send_email.fail_silently = False
            send_email.send()
            send_email2.fail_silently = False
            send_email2.send()
            # return render(request, 'repository/index.html', {"repositories": repositories, "form": contact_form2})
            return redirect('home')
    
    return render(request, 'repository/index.html', {"repositories": repositories, "form": contact_form2})