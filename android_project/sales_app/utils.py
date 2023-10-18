from django.db import transaction

from android_project.sales_app.models import SalesPerson
from typing import Tuple, Union, Any


@transaction.atomic
def user_get(*, username: str, password: str, **extra_data) -> Tuple[SalesPerson, bool]:
    user = SalesPerson.objects.filter(username=username).first()

    if user:
        if user.check_password(password):
            return user, True

    return False, False