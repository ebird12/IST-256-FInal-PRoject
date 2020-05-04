#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install letterboxd')
import requests
import json
url = 'https://api.letterboxd.com/api/v0/auth/username-check/json'
username = input("Enter a username")
params = {'username' : username}
response = requests.get(url, params = params)
verification = response.json()
verification
#username verificaton for letterboxd movie reccommendation api
#still awaiting access to the api




    
    
    
    

    


# In[ ]:


def movieID(movie_title):
    url = f'https://imdb-internet-movie-database-unofficial.p.rapidapi.com/search/{movie_title}'
    headers = {
        'X-RapidAPI-Key' : '0e2346792amsh887d13ea9fb8846p1a932cjsn661f19509e3a',
        'X-RapidAPI-Host' : 'imdb-internet-movie-database-unofficial.p.rapidapi.com'
    }
    response = requests.get(url, headers = headers)
    movies = response.json()
    movieid = movies['titles'][0]['id']
    return movienum


# In[ ]:


def movieID(movie_title):
    url = f'https://imdb-internet-movie-database-unofficial.p.rapidapi.com/search/{movie_title}'
    headers = {
        'X-RapidAPI-Key' : '0e2346792amsh887d13ea9fb8846p1a932cjsn661f19509e3a',
        'X-RapidAPI-Host' : 'imdb-internet-movie-database-unofficial.p.rapidapi.com'
    }
    response = requests.get(url, headers = headers)
    movies = response.json()
    movienum = movies['titles'][0]['id']
    return movienum
#gets and returns the movie id
def moviedata(get_id):
    url = f'https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/{get_id}'
    headers = {
        'X-RapidAPI-Key' : '0e2346792amsh887d13ea9fb8846p1a932cjsn661f19509e3a',
        'X-RapidAPI-Host' : 'imdb-internet-movie-database-unofficial.p.rapidapi.com'
    }
    response = requests.get(url, headers = headers)
    info = response.json()
    data_dict = {
    'title' : info['title'],
    'length' : info['length'],
    'rating': info['rating'],
    'plot' : info['plot']
    }
    return data_dict
#uses movie id to return a list of attributes of the movie
while True:
    movie_title = input("Enter a movie title: ")
    if movie_title == 'quit':
        print('Quititing')
        break
    else:
        get_id = (movieID(movie_title))
        get_data =(moviedata(get_id))
        print(f"{moviedata(get_id)}")
#returns data based on the title of the movie the user generates


# In[ ]:


def moviedata(get_id):
    url = f'https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/{get_id}'
    headers = {
        'X-RapidAPI-Key' : '0e2346792amsh887d13ea9fb8846p1a932cjsn661f19509e3a',
        'X-RapidAPI-Host' : 'imdb-internet-movie-database-unofficial.p.rapidapi.com'
    }
    response = requests.get(url, headers = headers)
    info = response.json()
    data_dict = {
    'title' : info['title'],
    'length' : info['length'],
    'rating': info['rating'],
    'plot' : info['plot']
    }
    return data_dict


# In[ ]:


url = f'https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/{get_id}'
headers = {
        'X-RapidAPI-Key' : '0e2346792amsh887d13ea9fb8846p1a932cjsn661f19509e3a',
        'X-RapidAPI-Host' : 'imdb-internet-movie-database-unofficial.p.rapidapi.com'
    }
response = requests.get(url, headers = headers)
info = response.json()
info


# In[ ]:


#returns movie reccommendations based on parameters release year and genre
genre = 35
year = 2018
url = 'https://api.themoviedb.org/3/discover/movie?'
params = {'api_key' : '0c6c8857f6fa10e885d4d503a6cbb3a6', 'year' : year, 'with_genres' : genre }
response = requests.get(url,params = params)
recommendations = response.json()
movie_dict = {
    'title' : recommendations['results'][0]['title'],
    'Plot' : recommendations['results'][0]['overview'],
    'Release Date': recommendations['results'][0]['release_date'],
    'Genre Ids' : recommendations['results'][0]['genre_ids'] 
    }
movie_dict


# In[ ]:


#list genre codes and their corresponding genres
url = 'https://api.themoviedb.org/3/genre/movie/list?'
params = {'api_key' : '0c6c8857f6fa10e885d4d503a6cbb3a6'}
response = requests.get(url,params = params)
genre = response.json()
genre


# In[ ]:


#takes user inputted genre name and converts to corresponding genre id
url = 'https://api.themoviedb.org/3/genre/movie/list?'
params = {'api_key' : '0c6c8857f6fa10e885d4d503a6cbb3a6'}
response = requests.get(url,params = params)
genre = response.json()
genre_str = input("Enter a genre: ")
def id_finder():
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
        print("I do not recognize this genre!")

    return(genre_int)
    


# In[ ]:


genre = 35
year = 2018
url = 'https://api.themoviedb.org/3/discover/movie?'
params = {'api_key' : '0c6c8857f6fa10e885d4d503a6cbb3a6', 'year' : year, 'with_genres' : genre }
response = requests.get(url,params = params)
recommendations = response.json()
movie_dict = {
    'title' : recommendations['results'][0]['title'],
    'Plot' : recommendations['results'][0]['overview'],
    'Release Date': recommendations['results'][0]['release_date'],
    'Genre Ids' : recommendations['results'][0]['genre_ids'] 
    }
movie_dict


# In[ ]:


def get_recs():   
   genre = get_id
   year = movieyear
   url = 'https://api.themoviedb.org/3/discover/movie?'
   params = {'api_key' : '0c6c8857f6fa10e885d4d503a6cbb3a6', 'year' : year, 'with_genres' : genre }
   response = requests.get(url,params = params)
   recommendations = response.json()
   movie_dict = {
       'title' : recommendations['results'][0]['title'],
       'Plot' : recommendations['results'][0]['overview'],
       'Release Date': recommendations['results'][0]['release_date'],
       'Genre Ids' : recommendations['results'][0]['genre_ids'] 
       }
   return movie_dict


# In[ ]:



while True:
    genre_str = input("Enter a genre: ")
    get_id = id_finder()
    movieyear = int(input("Enter a movie release year: "))
    recs = get_recs()
    print(recs)
    
    
    


# In[ ]:




