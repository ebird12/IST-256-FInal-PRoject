#!/usr/bin/env python
# coding: utf-8

# In[65]:


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
#still awaiting access to the ap




    
    
    
    

    


# In[62]:


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


# In[64]:


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


# In[61]:


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




