"""api test xdate."""
from fastapi import FastAPI
from fastapi.testclient import TestClient

from src.app import APP


client = TestClient(APP)


def test_index_page_api():
    response = client.get('/')
    assert response.status_code == 200
