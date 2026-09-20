from api.app import app
from fastapi.testclient import TestClient

def test_predict():
    with TestClient(app) as client:
        response = client.post("/predict", json={
            "V1": -1.359807, "V2": -0.072781, "V3": 2.536347, "V4": 1.378155,
            "V5": -0.338321, "V6": 0.462388, "V7": 0.239599, "V8": 0.098698,
            "V9": 0.363787, "V10": 0, "V11": 0, "V12": 0, "V13": 0, "V14": 0,
            "V15": 0, "V16": 0, "V17": 0, "V18": 0, "V19": 0, "V20": 0,
            "V21": -0.018307, "V22": 0.277838, "V23": -0.110474, "V24": 0.066928,
            "V25": 0.128539, "V26": -0.189115, "V27": 0.133558, "V28": -0.021053,
            "amount": 149.62, "hours": 0, "transaction_id": 1
        })
        assert response.status_code == 200