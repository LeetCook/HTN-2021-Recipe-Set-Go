import os, io
from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'recipestogo.json'

client = vision.ImageAnnotatorClient()
