import os
from google.oauth2 import service_account
import io
from google.cloud import storage, vision

# Get credentials
credentials = service_account.Credentials.from_service_account_file(
    '../../google-api-key.json')


def detect_text(path: str) -> str:
    """
    Detects text in the file.

    Parameters:
        path (str): path to image file
    """

    client = vision.ImageAnnotatorClient(credentials=credentials)

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    #print("{}".format(texts[0].description))
    print('Texts: \n{}'.format(texts[0].description))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))



def detect_document(path: str) -> str:
    """
    Detects document features in an image.

    Parameters:
        path (str): path to image file
    """

    client = vision.ImageAnnotatorClient(credentials=credentials)

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.document_text_detection(image=image)
    document = response.full_text_annotation

    for page in document.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    print('Word text: {}'.format(
                        word_text))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

detect_text('sign_text.png')

detect_document('hand_writing.png')