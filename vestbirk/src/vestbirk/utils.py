"""
    Utility functions used throughout the backend
    Author: Andreas Frisch
"""

import json
from django.http import HttpResponse

def json_response(response_dict, status=200):
    """
    Convert dictionary to JSON and return as a HTTP Response with JSON content
    """
    response = HttpResponse(
        #json.dumps(response_dict),
        response_dict,
        content_type="application/json",
        status=status
    )
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response

