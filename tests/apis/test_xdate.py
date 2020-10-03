"""api test xdate."""
from fastapi import FastAPI
from fastapi.testclient import TestClient

from src.app import APP


client = TestClient(APP)


def test_ts_to_datetime_api():
    ts = '1601452767'
    response = client.get('/api/dateutils/ts?w=' + ts)
    assert response.status_code == 200
    assert response.text == '2020-09-30 15:59:27\n'


def test_datetime_to_ts_api():
    dt = '2020-09-30 15:59:27'
    response = client.get('/api/dateutils/dt?w=' + dt)
    assert response.status_code == 200
    assert response.text == '1601452767\n'
