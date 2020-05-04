#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json
def id_finder():
    url = 'https://api.themoviedb.org/3/genre/movie/list?'
    params = {'api_key' : '0c6c8857f6fa10e885d4d503a6cbb3a6'}
    response = requests.get(url,params = params)
    genre = response.json()
    genre_int = 0
    if genre_str == genre['genres'][0]['name']:
        genre_int = 28
    elif genre_str == genre['genres'][1]['name']:
        genre_int = 12
    elif genre_str == genre['genres'][2]['name']:
        genre_int = 16
    elif genre_str == genre['genres'][3]['name']:
        genre_int = 35
    elif genre_str == genre['genres'][4]['name']:
        genre_int = 80
    elif genre_str == genre['genres'][5]['name']:
        genre_int = 99
    elif genre_str == genre['genres'][6]['name']:
        genre_int = 18
    elif genre_str == genre['genres'][7]['name']:
        genre_int = 10751
    elif genre_str == genre['genres'][8]['name']:
        genre_int = 14
    elif genre_str == genre['genres'][9]['name']:
        genre_int = 36
    elif genre_str == genre['genres'][10]['name']:
        genre_int = 27
    elif genre_str == genre['genres'][11]['name']:
        genre_int = 10402
    elif genre_str == genre['genres'][12]['name']:
        genre_int = 9648
    elif genre_str == genre['genres'][13]['name']:
        genre_int = 10749
    elif genre_str == genre['genres'][14]['name']:
        genre_int = 878
    elif genre_str == genre['genres'][15]['name']:
        genre_int = 10770
    elif genre_str == genre['genres'][16]['name']:
        genre_int = 53
    elif genre_str == genre['genres'][17]['name']:
        genre_int = 10752
    elif genre_str == genre['genres'][18]['name']:
        genre_int = 37
    else:
        genre_int = 1
        print("I do not recognize this genre!")


    return(genre_int)


# In[2]:


def get_recs():   
   genre = get_id
   year = movieyear
   url = 'https://api.themoviedb.org/3/discover/movie?'
   params = {'api_key' : '0c6c8857f6fa10e885d4d503a6cbb3a6', 'year' : year, 'with_genres' : genre }
   response = requests.get(url,params = params)
   recommendations = response.json()
   for data in recommendations["results"]:
       movie_dict = {
           'title' : data['title'],
           'Plot' : data['overview'],
           'Release Date': data['release_date'],
           'Genre Ids' : data['genre_ids'] 
   }
   return(movie_dict)


# In[ ]:


while True:
    genre_str = input("Enter a genre: ").capitalize()
    if genre_str == 'Quit':
        print("Quitting")
        break
    else:
        try:
            get_id = id_finder()
            movieyear = int(input("Enter a movie release year: "))
            recs = get_recs()
            print(recs)
        except:
            ValueError


# In[ ]:





# In[ ]:




