from multiprocessing import Pool
from datetime import datetime
from typing import List, Dict, Any

def addition_worker(numbers: List[int]) -> int:
    return sum(numbers)

def perform_addition(payload: List[List[int]]) -> Dict[str, Any]:
    start_time = datetime.now()
    with Pool() as pool:
        results = pool.map(addition_worker, payload)
    end_time = datetime.now()
    return {
        "response": results,
        "status": "complete",
        "started_at": start_time.isoformat(),
        "completed_at": end_time.isoformat()
    }
