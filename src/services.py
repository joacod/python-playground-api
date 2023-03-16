"""This module contains all the services that are used in the application"""
import requests

# Public api for getting TV shows info
URL = "https://api.tvmaze.com/search/shows?q="

def get_show_info(show_name):
    """Returns show info for a show name."""
    response = requests.get(URL, params={"q": show_name}, timeout=10)
    return response.json()
