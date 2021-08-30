from __future__ import absolute_import, unicode_literals    

from django.http import HttpResponse, response
from django.core.exceptions import ObjectDoesNotExist

from celery import shared_task
from requests import status_codes
from requests.sessions import Request

from .models import Repository

import time

import requests

# @shared_task
# def getRepo(url,url_post_request):

#     response = requests.get(url).json()
        
#     for repository in response:

#         repo_id = repository['id']

#         request_data = {
#             "repo_id": repository['id'],
#             "name": repository['name'],
#             "description": repository['description'],
#             "github_url": repository['html_url'],
#             "created_at": repository['created_at'][0:10],
#         }

#         r = Repository.objects.get(repo_id=repo_id)
#         if r:
#             requests.put(url=url_post_request + "/" + str(repo_id), data=request_data)
#             time.sleep(30000)
#             return HttpResponse(status=200)
#         else:
#             requests.post(url=url_post_request, data=request_data)
#             time.sleep(30000)
#             return HttpResponse(status=201)

        # try: 
        #     Repository.objects.get(repo_id=repo_id)
        #     requests.put(url=url_post_request + "/" + str(repo_id), data=request_data)
        #     time.sleep(10)
        #     return HttpResponse(status=201)
        # except ObjectDoesNotExist or requests.exceptions.ConnectionError:
        #     requests.post(url=url_post_request, data=request_data)
        #     return HttpResponse(status=429)

@shared_task
def get_repo(url):
    response = requests.get(url).json()

    for repository in response:
        repo_id = repository['id']
        name = repository['name']
        description = repository['description']
        github_url = repository['html_url']
        created_at = repository['created_at'][0:10]

        repo = Repository.objects.filter(repo_id=repo_id).exists()
        if repo:
            repo = Repository.objects.get(repo_id=repo_id)
            repo.description = description
            repo.save()
        else:
            repo = Repository(repo_id=repo_id, repo_name=name, description=description, url=github_url, created_date=created_at)
            repo.save()