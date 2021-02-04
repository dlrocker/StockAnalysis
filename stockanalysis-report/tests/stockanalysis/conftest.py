import pytest
from stockanalysis.api.api import build_app

flask_app = build_app()


@pytest.fixture
def client():
    """
    Creates a Flask rest client that can be used for API testing
    """
    with flask_app.app.test_client() as c:
        yield c
