import time
from utils.config import CIRCUIT_FAIL_THRESHOLD, CIRCUIT_RESET_TIMEOUT

# Store state per service
circuit_state = {}


def is_request_allowed(service: str):
    state = circuit_state.get(service, {
        "failures": 0,
        "status": "CLOSED",
        "opened_at": 0
    })

    # If OPEN → block requests
    if state["status"] == "OPEN":
        if time.time() - state["opened_at"] > CIRCUIT_RESET_TIMEOUT:
            # Move to HALF-OPEN
            state["status"] = "HALF_OPEN"
        else:
            return False

    return True


def record_success(service: str):
    circuit_state[service] = {
        "failures": 0,
        "status": "CLOSED",
        "opened_at": 0
    }


def record_failure(service: str):
    state = circuit_state.setdefault(service, {
        "failures": 0,
        "status": "CLOSED",
        "opened_at": 0
    })

    state["failures"] += 1

    if state["failures"] >= CIRCUIT_FAIL_THRESHOLD:
        state["status"] = "OPEN"
        state["opened_at"] = time.time()