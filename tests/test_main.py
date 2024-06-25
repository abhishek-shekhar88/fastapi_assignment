from fastapi.testclient import TestClient
from fast_api_app.main import (app)

client = TestClient(app)

def test_main_route() -> None:
    response = client.get("/")
    assert response.status_code == 404  # Assuming there's no root endpoint defined
