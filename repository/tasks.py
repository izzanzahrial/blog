from __future__ import absolute_import, unicode_literals    

from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from celery import shared_task

from .models import Repository

import requests

@shared_task
def getRepo(url,url_post_request):

    response = requests.get(url).json()
        
    for repository in response:

        repo_id = repository['id']

        request_data = {
            "repo_id": repository['id'],
            "name": repository['name'],
            "description": repository['description'],
            "github_url": repository['html_url'],
            "created_at": repository['created_at'][0:10],
        }

        try: 
            Repository.objects.get(repo_id=repo_id)
            requests.put(url=url_post_request + "/" + str(repo_id), data=request_data)
            return HttpResponse(status=201)
        except ObjectDoesNotExist:
            requests.post(url=url_post_request, data=request_data)
            return HttpResponse(status=201)