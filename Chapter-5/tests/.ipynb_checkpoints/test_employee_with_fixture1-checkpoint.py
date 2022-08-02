
from datetime import datetime


def test_employee_get_name(dummy_employee):
    assert dummy_employee.get_name() == f"{dummy_employee.fname} {dummy_employee.lname}"
