import pytest
from stockanalysis.api.api import build_app

flask_app = build_app()


@pytest.fixture
def client():
    with flask_app.app.test_client() as c:
        yield c
