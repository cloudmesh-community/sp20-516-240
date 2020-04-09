import os

from google.oauth2 import service_account
import googleapiclient.discovery
import io
from google.cloud import storage, vision


#!export GOOGLE_APPLICATION_CREDENTIALS = ""

# Get credentials
credentials = service_account.Credentials.from_service_account_file(
    '../../google-api-key.json')

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

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket"""
    # bucket_name = "your-bucket-name"
    # source_file_name = "local/path/to/file"
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )

def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io

    credentials = service_account.Credentials.from_service_account_file(
        '../../google-api-key.json')

    client = vision.ImageAnnotatorClient(credentials=credentials)

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

detect_text('sign_text.png')