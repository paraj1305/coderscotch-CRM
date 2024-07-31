# employee/authentication_backends.py

from django.contrib.auth.backends import BaseBackend
from superadmin.models import Employee
from django.contrib.auth.hashers import check_password

class EmployeeBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            employee = Employee.objects.get(email=email)
            if employee.check_password(password):
                return employee
        except Employee.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Employee.objects.get(pk=user_id)
        except Employee.DoesNotExist:
            return None
