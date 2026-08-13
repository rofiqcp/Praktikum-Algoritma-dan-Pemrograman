import json
from pathlib import Path

MOCK_FILE = Path(__file__).parent / "mock_external.json"


def fetch_external(mode="success"):
    """Simulasi integrasi external/mock API yang deterministik untuk praktikum."""
    if mode == "empty":
        return {"state": "empty", "data": [], "message": "Data tidak ditemukan pada simulasi."}
    if mode == "timeout":
        return {"state": "timeout", "data": [], "message": "Simulasi request melewati batas waktu."}
    if mode == "error":
        return {"state": "error", "data": [], "message": "Simulasi service tidak tersedia."}
    if mode != "success":
        return {"state": "error", "data": [], "message": "Mode simulasi tidak dikenal."}

    payload = json.loads(MOCK_FILE.read_text(encoding="utf-8"))
    data = payload.get("data", payload) if isinstance(payload, dict) else payload
    if not data:
        return {"state": "empty", "data": [], "message": "Response valid tetapi tidak berisi data."}
    return {"state": "success", "data": data, "message": None}


if __name__ == "__main__":
    for sample_mode in ["success", "empty", "timeout", "error"]:
        print(sample_mode, "->", fetch_external(sample_mode))
