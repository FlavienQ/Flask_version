'''
Old way to conenct to the database using psycopg2 instead of SQLAlchemy
'''

import os
import psycopg2
from urllib.parse import urlparse

url = urlparse.urlparse(os.environ["DATABASE_URL"])

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)