from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class Customer(AbstractUser):
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        related_query_name="custom_user",
        help_text=(
            'The permissions this user has. '
            'Those with the "Can change users" permission '
            'can edit other users.'
        ),
        related_name="custom_user_permissions",
    )
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        related_name="custom_user_groups",
        related_query_name="custom_user",
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
    )
    username = None 
    email = models.EmailField(unique=True)

    # Set the email field as the username field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    company_name= models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    
    
    def save(self, *args, **kwargs):
        # self.password = make_password(self.password)
        super(Customer, self).save(*args, **kwargs)

    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class Order(models.Model):
    class FrequncyEnum(models.TextChoices):
        WEEKLY = 'W', ('Weekly')
        FORTNIGHT = 'FN', ('Fortnight')

    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    start_date = models.DateField()
    frequency = models.CharField(max_length=20,   choices=FrequncyEnum.choices,
        default=FrequncyEnum.WEEKLY,)
    duration = models.DecimalField( max_digits=5, decimal_places=2)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self) -> str:
        return f"{self.email} {self.duration}"

    
class Invoice(models.Model):
    class PaymentEnum(models.TextChoices):
        Order = 'O', ('Order')
        UrgentDelivery = 'UD', ('UrgentDelivery')
    
    order_id = models.OneToOneField(Order, on_delete=models.CASCADE)
    user_id= models.OneToOneField(Customer, on_delete=models.CASCADE)
    is_paid = models.BooleanField()
    payment_type= models.CharField(max_length=20,   choices=PaymentEnum.choices,
        default=PaymentEnum.UrgentDelivery,)
    payment_date  = models.DateTimeField()
    
    def __str__(self) -> str:
        return f"{self.order_id} has been paid in ${self.payment_date}"
    
    


class UrgentDelivery(models.Model):
   
    email = models.EmailField()
    address = models.CharField(max_length=100)
    start_date = models.DateField()
    phone_number = models.CharField(max_length=20)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"{self.email} has urgernt develivery to {self.address}"
    
    
class Maintainence(models.Model):

    email = models.EmailField()
    address = models.CharField(max_length=100)
    date = models.DateField()
    phone_number = models.CharField(max_length=20)
    problem_statment = models.TextField()
    
    def __str__(self):
        return f"{self.email} has urgernt maintained  to {self.address}"
    