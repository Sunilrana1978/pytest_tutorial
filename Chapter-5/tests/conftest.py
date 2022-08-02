import pytest

from src.employee import Employee

@pytest.fixture(scope="module" )
def dummy_employee():
    return Employee("Sunil", "Kumar", 100000.00)

@pytest.fixture(scope="module" )
def tax():
    return 0.25