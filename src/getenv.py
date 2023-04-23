import os
from dotenv import load_dotenv
load_dotenv()

#EMAIL LOGIN
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASS = os.getenv('EMAIL_PASS')