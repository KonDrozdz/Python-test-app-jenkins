from app import app
import pytest

@pytest.fixture
def client():
    return app.test_client()

def test_hello(client):
    response = client.get('/')
    assert b"Hello, World!" in response.data