
def test_student_add_credits(dummy_employee):
    assert dummy_employee.get_salary() == 100000.00

def test_get_salary_after_tax(dummy_employee,tax):
    assert dummy_employee.get_salary_after_tax(tax) == (dummy_employee.salary - dummy_employee.salary*tax)
