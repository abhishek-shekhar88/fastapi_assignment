from fastapi.testclient import TestClient
from fast_api_app.main import app
from datetime import datetime

client = TestClient(app)

def test_addition() -> None:
    response = client.post("/add", json={
        "batchid": "id0101",
        "payload": [[1, 2], [3, 4]]
    })
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["batchid"] == "id0101"
    assert json_response["response"] == [3, 7]
    assert json_response["status"] == "complete"
    assert "started_at" in json_response
    assert "completed_at" in json_response
    assert datetime.fromisoformat(json_response["started_at"])
    assert datetime.fromisoformat(json_response["completed_at"])

def test_invalid_input() -> None:
    response = client.post("/add", json={"batchid": "id0101", "payload": [[1, "a"], [3, 4]]})
    assert response.status_code == 422  # Unprocessable Entity for invalid input
