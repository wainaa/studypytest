import pytest


@pytest.fixture(scope='function', autouse=False)
def setup():
    print('\nstart=================start')
    yield
    print('\nend=====================end')
