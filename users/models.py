from django.db import models 
from django.contrib.auth.models import  AbstractBaseUser, BaseUserManager


class  UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:raise ValueError("Users must have email address!")
        user= self.model( email= self.normalize_email(email))
        user.set_password(password)
        user.save(using=self.db)
        return user
    def create_superuser(self, email,  password=None ):
        user=self.create_user( email, password=password)
        user.is_admin=True
        user.save(using= self.db)
        return user


class User(AbstractBaseUser):
    email= models.EmailField (
        verbose_name= ' email address', 
        max_length= 255,
        unique= True
    )
    is_active= models.BooleanField(default=True)
    staff= models.BooleanField( default = False)
    is_admin= models.BooleanField( default= False)
    username = models.CharField(null=True, max_length=30)
    first_name= models.CharField(max_length= 30)
    last_name= models.CharField(max_length= 30)
    date_joined= models.DateTimeField(auto_now_add=True)
    date_of_birth= models.DateField( null= True, blank=True)
    weight= models.IntegerField(null=True, blank=True)
    height= models.IntegerField(null=True, blank=True)
    #TODO : goals=
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects=UserManager()
    def __str__(self):
       return self.email
    
    def has_perm(self, perm, obj=None ):
        return True
    def has_module_perms(self, app_label):
        return True
    @property
    def is_staff(self):
        return self.is_admin

# class Goal(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goals')
#     goal_name = models.CharField(max_length=255)