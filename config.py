import os

class Config:
    LINKEDIN_USERNAME = os.environ.get('LINKEDIN_USERNAME')
    LINKEDIN_PASSWORD = os.environ.get('LINKEDIN_PASSWORD')
    PATH_TO_SELENIUM = os.environ.get('PATH_TO_SELENIUM')