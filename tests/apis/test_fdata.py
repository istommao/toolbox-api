"""api test fake data."""
from fastapi import FastAPI
from fastapi.testclient import TestClient

from src.app import APP


client = TestClient(APP)


def test_fake_data_list_api():
    response = client.get('/api/fdata/list/')
    assert response.status_code == 200
