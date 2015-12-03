from .models import Users, Movies

def eng_add_movies(rsc_dict):
	r_code, r_str = '0', None
	name, director, genre, imdb_score, popularity = rsc_dict['name'],\
							rsc_dict['director'],rsc_dict['genre'],\
							rsc_dict['imdb_score'],rsc_dict['popularity']
	movie = Movies(name = name, director = director, \
				genre = genre, imdb_score = imdb_score, \
				popularity = popularity)
	movie.save()
	return r_code, r_str, rsc_dict

def eng_edit_movies(rsc_dict):
	r_code, r_str = '0', None
	name, director, genre, imdb_score, popularity = rsc_dict['name'],\
							rsc_dict['director'],rsc_dict['genre'],\
							rsc_dict['imdb_score'],rsc_dict['popularity']
	movie = rsc_dict['movie']
	movie.name = name
	movie.director = director
	movie.genre = genre
	movie.imdb_score = imdb_score
	movie.popularity = popularity
	movie.save()
	return r_code, r_str, rsc_dict

def eng_delete_movies(rsc_dict):
	r_code, r_str = '0', None
	movie = rsc_dict['movie']
	movie.delete()
	return r_code, r_str, rsc_dict