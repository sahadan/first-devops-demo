from app import add, app

# Unit test: checks one small function
def test_add():
    assert add(2,3) == 5 # Fail if false

# Route test: Flask's test client simulates a browser
def test_home_route():
        client = app.test_client()
        response = client.get("/")
        assert response.status_code == 200      # 200 = OK
        assert b"Hello, DevOps Team: CI CD 2026" in response.data

def test_health_route():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"
