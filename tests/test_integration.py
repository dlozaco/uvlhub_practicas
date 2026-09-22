import pytest

pytestmark = pytest.mark.integration


def test_notepad_index_requires_login(test_client):
    response = test_client.get("/notepad", follow_redirects=False)

    print("\n--- DATOS DE LA RESPUESTA ---")
    print("Status code:", response.status_code)
    print("Headers Location:", response.headers.get("Location"))
    print("-----------------------------\n")

    assert response.status_code in (302, 303)
    assert "/login" in response.headers.get("Location", "")