from django.db import models
import uuid
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator


class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tc_no = models.CharField(max_length=11 , unique=True ,
                              validators=[MinLengthValidator(11),MaxLengthValidator(11),]
                              ,)
    name = models.CharField(max_length=100,
                             validators=[RegexValidator(r'^[A-Za-zÇçĞğİıÖöŞşÜü]+$',
                                                        message="Sadece harf kullanılabilir.")])
    surname = models.CharField(max_length=100,
                             validators=[RegexValidator(r'^[A-Za-zÇçĞğİıÖöŞşÜü]+$',
                                                        message="Sadece harf kullanılabilir.")])

    phone = models.CharField(max_length=11 ,validators=[MinLengthValidator(11),MaxLengthValidator(11),],)
    city = models.CharField(max_length=100,
                             validators=[RegexValidator(r'^[A-Za-zÇçĞğİıÖöŞşÜü]+$',
                                                        message="Sadece harf kullanılabilir.")])
    district = models.CharField(max_length=100,
                             validators=[RegexValidator(r'^[A-Za-zÇçĞğİıÖöŞşÜü]+$',
                                                        message="Sadece harf kullanılabilir.")])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def _str_(self):
        return self.name
