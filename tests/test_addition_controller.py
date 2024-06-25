from fastapi.testclient import TestClient
from fast_api_app.main import app

client = TestClient(app)

def test_add_numbers_success() -> None:
    response = client.post("/add", json={
        "batchid": "id0101",
        "payload": [[5, 10], [15, 20]]
    })
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["batchid"] == "id0101"
    assert json_response["response"] == [15, 35]
    assert json_response["status"] == "complete"

def test_add_numbers_error_handling() -> None:
    response = client.post("/add", json={
        "batchid": "id0101"
    })
    assert response.status_code == 422
