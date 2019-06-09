#!/home/kaur/miniconda3/envs/oauth-flow-test/bin/python
import json
#import ssl

import logging

logging.getLogger('flask_cors').level = logging.DEBUG

from auth import verify_access_token
from flask import Flask, request

from flask_cors import CORS
from flask_cors import cross_origin

DEBUG=True
app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}}, supports_credentials=True)

app.config['CORS_AUTOMATIC_OPTIONS'] = True
app.config['CORS_HEADERS'] = 'Authorization, Content-Type'

@app.before_request
def before_request():
  # Checks if the access token is present and valid.

  if request.method == 'OPTIONS': 
    # This is here to allow client browser preflights to succeed
    # TODO this check should go somewhere else, probably into a pre route decorator
    return

  auth_header = request.headers.get('Authorization')
  if auth_header is None or 'Bearer' not in auth_header:
    return json.dumps({
      'error': 'Access token does not exist.'
    }), 400
  
  access_token = auth_header[7:]

  if access_token and verify_access_token(access_token):
      pass
  else:
    return json.dumps({
      'error': 'Access token is invalid.'
    }), 400


@app.route('/users', methods = ['GET'])
def get_user():
  # Returns a list of users.
  users = [
    { 'username': 'Jane Doe', 'email': 'janedoe@example.com'},
    { 'username': 'John Doe', 'email': 'johndoe@example.com'}
  ]

  return json.dumps({
    'results': users
  })

@app.route('/ping', methods = ['GET'])
def ping_pong():
  return json.dumps('pong!')
    

if __name__ == '__main__':
  #context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
  #context.load_cert_chain('domain.crt', 'domain.key')
  #app.run(port = 5000, debug = True, ssl_context = context)
  app.run(port = 5002, debug = True)