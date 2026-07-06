import pytest
import json
from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestUserEndpoint:
    """Tests for GET /users/<id> endpoint."""

    def test_get_existing_user(self, client):
        """Test retrieving an existing user returns 200 with user data."""
        response = client.get('/users/1')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['id'] == '1'
        assert data['name'] == 'Alice Johnson'
        assert data['email'] == 'alice@example.com'

    def test_get_another_existing_user(self, client):
        """Test retrieving another existing user."""
        response = client.get('/users/2')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['id'] == '2'
        assert data['name'] == 'Bob Smith'
        assert data['email'] == 'bob@example.com'

    def test_get_nonexistent_user_returns_404(self, client):
        """Test requesting a non-existent user returns 404 with error message."""
        response = client.get('/users/999')
        
        assert response.status_code == 404
        data = json.loads(response.data)
        assert 'error' in data
        assert data['error'] == 'User not found'
        assert data['id'] == '999'

    def test_get_nonexistent_user_returns_json_error(self, client):
        """Test that 404 response is valid JSON (not KeyError crash)."""
        response = client.get('/users/invalid-id')
        
        assert response.status_code == 404
        assert response.content_type == 'application/json'
        data = json.loads(response.data)
        assert isinstance(data, dict)
        assert 'error' in data
