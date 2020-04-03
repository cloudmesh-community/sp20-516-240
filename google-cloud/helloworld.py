import os

from google.oauth2 import service_account
import googleapiclient.discovery

#!export GOOGLE_APPLICATION_CREDENTIALS = ""

# Get credentials
credentials = service_account.Credentials.from_service_account_file(
    '../../cloudmesh-3f8ecb78efbf.json')

# Create the Cloud IAM service object
service = googleapiclient.discovery.build(
    'iam', 'v1', credentials=credentials)

# Call the Cloud IAM Roles API
# If using pylint, disable weak-typing warnings
# pylint: disable=no-member
response = service.roles().list().execute()
roles = response['roles']

# Process the response
for role in roles:
    print('Title: ' + role['title'])
    print('Name: ' + role['name'])
    if 'description' in role:
        print('Description: ' + role['description'])
    print('')


def my_super_function(x, y):
    pass
    # insert ML function
    # read up on typing for functions
