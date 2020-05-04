#!/usr/bin/env python
# coding: utf-8

# In[32]:


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


# In[36]:


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


# In[46]:



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


# In[30]:


url = 'https://api.themoviedb.org/3/genre/movie/list?'
params = {'api_key' : '0c6c8857f6fa10e885d4d503a6cbb3a6'}
response = requests.get(url,params = params)
genre = response.json()
genre


# In[ ]:




