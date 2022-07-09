import json
import os
import pathlib
import random
import tempfile

import pytest

from blog.models import Article


@pytest.fixture
def random_name():
    names = ["John", "Jane", "Marry"]
    return random.choice(names)


@pytest.fixture(autouse=True)
def database():
    _, file_name = tempfile.mkstemp()
    os.environ["DATABASE_NAME"] = file_name
    Article.create_table(database_name=file_name)
    yield
    os.unlink(file_name)
