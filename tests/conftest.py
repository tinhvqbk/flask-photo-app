import pytest

from app import create_app
from app.db import insert_test_data, clear_db


@pytest.fixture
def client():
    app = create_app()

    with app.test_client() as client:
        with app.app_context():
            insert_test_data()
        yield client

    with app.app_context():
        clear_db()
