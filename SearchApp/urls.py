#urls of CardApp

from django.conf.urls import patterns, url                                                            
                                                                                                      
urlpatterns = patterns('SearchApp.views',                                                              
    url(r'^v1/addmovies/$', 'add_movies'),
    url(r'^v1/editmovies/$', 'edit_movies'),
    url(r'^v1/deletemovies/$', 'delete_movies'),
    url(r'^v1/movies/$', 'movies'),
)    
