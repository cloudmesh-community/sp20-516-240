import csv
import boto3

# get credentials
with open('../../aws-credentials.csv', 'r') as input:
    next(input)
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]

def detect_text(path: str) -> str:
    """
    Function that detects text from image

    :param path:
    :return:
    """

    client = boto3.client('rekognition',
                          aws_access_key_id=access_key_id,
                          aws_secret_access_key=secret_access_key)

    with open(path, 'rb') as image_file:
        content = image_file.read()


    response = client.detect_text(
        Image={
            'Bytes': content,
            #'S3Object': {
            #    'Bucket': 'string',
            #    'Name': 'string',
            #    'Version': 'string'
            #}
        },
        Filters={
            'WordFilter': {
                'MinConfidence': 95
        #        'MinBoundingBoxHeight': ...,
        #        'MinBoundingBoxWidth': ...
        #    },
        #    'RegionsOfInterest': [
        #        {
        #            'BoundingBox': {
        #                'Width': ...,
                        #'Height': ...,
                        #'Left': ...,
                        #'Top': ...
                    }
                },
            #]
        #}
    )

    text_detections = response['TextDetections']

    for group in text_detections:
        print(group['DetectedText'])

detect_text('sign_text.png')