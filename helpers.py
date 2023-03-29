import requests

from flask import redirect, session
from functools import wraps

def lookup(param):
    try:
        api_key = '2b15dcdccd77a2803a30cea7e78b42a1'
        api_id = '27e4f5c3'
        response = requests.get(f"https://api.edamam.com/api/recipes/v2?type=public&q=%22{param}%22&app_id={api_id}&app_key={api_key}")
        response.raise_for_status()
    except requests.RequestException:
        return None
    try:
        result = response.json()
        return None
        #TODO return results to use within db ie result['hits'][0]['recipe']['source']
    
    except (KeyError, TypeError, ValueError):
        return None

def login_required(f):
    """
    Decorate routes to require login.


    
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function