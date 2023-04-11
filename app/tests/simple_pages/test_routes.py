def test_index_success(client):
    response = client.get('/')
    assert response.status_code == 200