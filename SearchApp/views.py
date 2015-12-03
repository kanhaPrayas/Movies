from django.shortcuts import render
from models import *
from django.views.decorators.csrf import csrf_exempt, csrf_protect, requires_csrf_token, ensure_csrf_cookie
from request_utils import *
from django.http import HttpResponse
import json
import dicttoxml
from .get import *
from .eng import *

RESPONSE_XML_TYPE = 'application/xml'
RESPONSE_JSON_TYPE = 'application/json'

add_movies_success_str="New movie added successfully."
edit_movies_success_str="Movie updated successfully."
delete_movies_success_str="Movie deleted Successfully."
movies_success_str = 'Movies received successfully.'

def return_response(r_code, r_str, api_name, response, details, response_type):
    r_str = update_success_str(r_code, r_str, api_name)
    response = prepare_final_response(response, r_code, r_str, details)
    print type(response)
    response = json.dumps(response)
    response_type_header = RESPONSE_JSON_TYPE
    if response_type == 'xml':
        response_type_header = RESPONSE_XML_TYPE
        response = dicttoxml.dicttoxml(json.loads(response))
    return response, response_type_header

def prepare_final_response(response, r_code, r_str, details):
	response['r_code'] = r_code
	response['r_str'] = r_str
	response['r_det'] = details
	return response

def update_success_str(r_code, r_str, api_name):
    if r_code == '0':
        return eval(api_name + '_success_str')
    return r_str

@csrf_exempt
def add_movies(request):
    #Gets and checks the request parameters
    response = {}
    r_code, r_str, rsc_dict = check_add_movies(request)
    if r_code == '0':
        r_code, r_str, rsc_dict = get_add_movies(rsc_dict)
        if r_code == '0':
            r_code, r_str, rsc_dict = eng_add_movies(rsc_dict)
    else:
        pass
    response, response_type_header = return_response(r_code, \
                                r_str, 'add_movies', response, \
                                rsc_dict['details'], rsc_dict['response_type'] \
                            )
    return HttpResponse(response, content_type=response_type_header)


@csrf_exempt
def edit_movies(request):
    #Gets and checks the request parameters
    response = {}
    r_code, r_str, rsc_dict = check_edit_movies(request)
    if r_code == '0':
        r_code, r_str, rsc_dict = get_edit_movies(rsc_dict)
        if r_code == '0':
        	r_code, r_str, rsc_dict = eng_edit_movies(rsc_dict)
    else:
        pass
    response, response_type_header = return_response(r_code, \
                                r_str, 'edit_movies', response, \
                                rsc_dict['details'], rsc_dict['response_type'] \
                            )
    return HttpResponse(response, content_type=response_type_header)

@csrf_exempt
def delete_movies(request):
    #Gets and checks the request parameters
    response = {}
    r_code, r_str, rsc_dict = check_delete_movies(request)
    if r_code == '0':
        r_code, r_str, rsc_dict = get_delete_movies(rsc_dict)
        if r_code == '0':
            r_code, r_str, rsc_dict = eng_delete_movies(rsc_dict)
    else:
        pass
    response, response_type_header = return_response(r_code, \
                                r_str, 'delete_movies', response, \
                                rsc_dict['details'], rsc_dict['response_type'] \
                            )
    return HttpResponse(response, content_type=response_type_header)

@csrf_exempt
def movies(request):
    #Gets and checks the request parameters
    response = {}
    r_code, r_str, rsc_dict = check_movies(request)
    if r_code == '0':
        r_code, r_str, rsc_dict = get_movies(rsc_dict)
    else:
        pass
    response, response_type_header = return_response(r_code, \
                                r_str, 'movies', response, \
                                rsc_dict['details'], rsc_dict['response_type'] \
                            )
    return HttpResponse(response, content_type=response_type_header)