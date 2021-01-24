from polvalcalc import app

def test_polvalcalc():
    response = app.test_client().get('/')
    assert response.status_code == 200

