from fastapi.testclient import TestClient
from main import app  # предполагается, что ваш код находится в main.py
from urllib.parse import urlparse


client = TestClient(app)


def test_scrape():
    response = client.get("/scrape?url=https://www.example.com")
    assert response.status_code == 200
    links = response.json()
    assert isinstance(links, list)
    for link in links:
        parsed = urlparse(link)
        assert parsed.scheme in ['http', 'https']
        assert bool(parsed.netloc)
        assert bool(parsed.path)
