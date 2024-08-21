from urlshort import create_app

# This file contains multiple sanity checks to check if the new deployment is missing something as a result of new additions

def test_shorten(client):
    response = client.get('/')
    assert b'Shorten the URL' in response.data

def test_encode(client):
    response = client.get('/')
    assert b'Encode the file' in response.data