from flask import request,jsonify
import flask
import requests

url="https://okis.pythonanywhere.com/doviz-altin"
response=requests.post(url)
print(response.json())