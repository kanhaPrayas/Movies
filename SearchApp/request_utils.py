RESPONSE_CODE_POSTPARAMS_ERROR, RESPONSE_STRING_POST_PARAMS = '90', 'Insufficient post parameters'

def check_add_movies(request):
    r_code, r_str = '0', None
    #Dictionary contains all the possible parameters those are expected in this api call
    rsc_dict = {
                'email_id':None,
                'name': None,
                'director': None,
                'genre':None,
                'imdb_score':None,
                'popularity':None,
                'details': {},
                'response_type':'json'
            }
    #List contains the mandatory parameters
    reqd_params = ['email_id','name', 'director','genre']
    for k,v in rsc_dict.items():
        if k in request.POST:
            rsc_dict[k]  = request.POST[k]
            if k in reqd_params:
                #Removes the received parameters
                reqd_params.remove(k)
    if len(reqd_params) != 0:
        #returns the array of not received parameters which will be sent back to client.
        rsc_dict['details']['params_not_sent'] = ",".join(reqd_params)
        r_code, r_str =  RESPONSE_CODE_POSTPARAMS_ERROR, \
                                RESPONSE_STRING_POST_PARAMS
    return r_code, r_str, rsc_dict    


def check_edit_movies(request):
    r_code, r_str = '0', None
    #Dictionary contains all the possible parameters those are expected in this api call
    rsc_dict = {
                'email_id':None,
                'id': None,
                'name': None,
                'director': None,
                'genre':None,
                'imdb_score':None,
                'popularity':None,
                'details': {},
                'response_type':'json'
            }
    #List contains the mandatory parameters
    reqd_params = ['email_id','name', 'director','genre','id']
    for k,v in rsc_dict.items():
        if k in request.POST:
            rsc_dict[k]  = request.POST[k]
            if k in reqd_params:
                #Removes the received parameters
                reqd_params.remove(k)
    if len(reqd_params) != 0:
        #returns the array of not received parameters which will be sent back to client.
        rsc_dict['details']['params_not_sent'] = ",".join(reqd_params)
        r_code, r_str =  RESPONSE_CODE_POSTPARAMS_ERROR, \
                                RESPONSE_STRING_POST_PARAMS
    return r_code, r_str, rsc_dict 

def check_delete_movies(request):
    r_code, r_str = '0', None
    #Dictionary contains all the possible parameters those are expected in this api call
    rsc_dict = {
                'email_id':None,
                'id': None,
                'details': {},
                'response_type':'json'
            }
    #List contains the mandatory parameters
    reqd_params = ['id','email_id']
    for k,v in rsc_dict.items():
        if k in request.POST:
            rsc_dict[k]  = request.POST[k]
            if k in reqd_params:
                #Removes the received parameters
                reqd_params.remove(k)
    if len(reqd_params) != 0:
        #returns the array of not received parameters which will be sent back to client.
        rsc_dict['details']['params_not_sent'] = ",".join(reqd_params)
        r_code, r_str =  RESPONSE_CODE_POSTPARAMS_ERROR, RESPONSE_STRING_POST_PARAMS
    return r_code, r_str, rsc_dict 

def check_movies(request):
    r_code, r_str = '0', None
    #Dictionary contains all the possible parameters those are expected in this api call
    rsc_dict = {
                'name':None,
                'details': {},
                'response_type':'json'
            }
    #List contains the mandatory parameters
    reqd_params = ['name']
    for k,v in rsc_dict.items():
        if k in request.POST:
            rsc_dict[k]  = request.POST[k]
            if k in reqd_params:
                #Removes the received parameters
                reqd_params.remove(k)
    if len(reqd_params) != 0:
        #returns the array of not received parameters which will be sent back to client.
        rsc_dict['details']['params_not_sent'] = ",".join(reqd_params)
        r_code, r_str =  RESPONSE_CODE_POSTPARAMS_ERROR, RESPONSE_STRING_POST_PARAMS
    return r_code, r_str, rsc_dict 