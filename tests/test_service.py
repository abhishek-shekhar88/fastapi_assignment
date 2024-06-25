from fast_api_app.services.addition_service import addition_worker, perform_addition
from datetime import datetime
from typing import List

def test_addition_worker() -> None:
    result = addition_worker([1, 2, 3])
    assert result == 6

def test_perform_addition() -> None:
    payload = [[1, 2], [3, 4]]
    result = perform_addition(payload)
    assert result["response"] == [3, 7]
    assert result["status"] == "complete"
    assert datetime.fromisoformat(result["started_at"])
    assert datetime.fromisoformat(result["completed_at"])
