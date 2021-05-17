from __future__ import absolute_import, unicode_literals

from celery import shared_task

import requests

@shared_task
def getRepo(url,url_post_request):

    response = requests.get(url).json()
        
    for repository in response:

        parameter = {
            "repo_id": repository['id'],
            "name": repository['name'],
            "description": repository['description'],
            "github_url": repository['html_url'],
            "created_at": repository['created_at'][0:10],
        }

        requests.post(url=url_post_request, params=parameter)