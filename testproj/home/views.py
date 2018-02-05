from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
# Create your views here.
# import requests
import flask
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User
# from oauth2client.contrib.django_orm import Storage
from oauth2client.contrib.django_util.storage import DjangoORMStorage
from .models import CredentialsModel
import google.oauth2.credentials
import google_auth_oauthlib.flow
import urllib.parse as urlparse
import time 

from oauth2client.client import flow_from_clientsecrets

flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
    'C:/Users/jatin/Documents/Django Projects/login/login/client_secrets.json',
    scopes=settings.SOCIAL_AUTH_YOUTUBE_SCOPE)

flow.redirect_uri = "http://127.0.0.1:8000/accounts/google/login/callback/"



def Home(request):
    print (request.method)
    print (type(request.user))
    print ("AnonymousUser")
    # print (request.email)
    if str(request.user) != "AnonymousUser":
       print (request.method)
       print (request.user.email)
       authorization_url, state = flow.authorization_url(
            prompt='consent',
            access_type='offline',
            state= settings.SECRET_KEY)
       # print (authorization_url)
       print ("asdf")
       # return flask.redirect(authorization_url)
       print (type(authorization_url))
       print (authorization_url)
       print ("asdf")
       return HttpResponseRedirect(authorization_url)
    # func(request)
    # print ("JAtin")
    # # time.sleep(5) 
    # print ("wadhwa")
    



