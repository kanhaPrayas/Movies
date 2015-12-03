from .models import Users, Movies


def get_add_movies(rsc_dict):
	r_code, r_str = '0', None
	try:
		user = Users.objects.get(email_id = rsc_dict['email_id'])
		if user.role != '0':
			raise Exception("user is not an admin")
	except Users.DoesNotExist,e:
		r_code, r_str = '98', 'user does not exist'
	except Exception,e:
		r_code, r_str = '97', 'user is not an admin'
	return r_code, r_str, rsc_dict


def get_edit_movies(rsc_dict):
	r_code, r_str = '0', None
	try:
		user = Users.objects.get(email_id = rsc_dict['email_id'])
		if user.role != '0':
			raise Exception("user is not an admin")
		rsc_dict['movie'] = Movies.objects.get(id = rsc_dict['id'])
	except Users.DoesNotExist,e:
		r_code, r_str = '98', 'user does not exist'
	except Movies.DoesNotExist,e:
		r_code, r_str = '98', 'movie does not exist'
	except Exception,e:
		r_code, r_str = '97', 'user is not an admin'
	return r_code, r_str, rsc_dict


def get_delete_movies(rsc_dict):
	r_code, r_str = '0', None
	try:
		user = Users.objects.get(email_id = rsc_dict['email_id'])
		if user.role != '0':
			raise Exception("user is not an admin")
		rsc_dict['movie'] = Movies.objects.get(id = rsc_dict['id'])
	except Users.DoesNotExist,e:
		r_code, r_str = '98', 'user does not exist'
	except Movies.DoesNotExist,e:
		r_code, r_str = '98', 'movie does not exist'
	except Exception,e:
		r_code, r_str = '97', 'user is not an admin'
	return r_code, r_str, rsc_dict

def get_movies(rsc_dict):
	r_code, r_str = '0', None
	rsc_dict['details']['movies'] = list(Movies.objects.filter(name__icontains = \
			rsc_dict['name']).values('id','name','director','genre',\
												'imdb_score','popularity'))
	return r_code, r_str, rsc_dict




