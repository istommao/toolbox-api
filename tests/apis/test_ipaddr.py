"""api test ipaddr."""
from fastapi import FastAPI
from fastapi.testclient import TestClient

from src.app import APP


client = TestClient(APP)


def test_ip_addr_api():
    ip = '127.0.0.1'
    response = client.get('/api/ipaddr/?w=' + ip)
    assert response.status_code == 200
    assert response.json()['is_valid'] == True
