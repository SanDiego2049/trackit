from django.db import models 
from django.contrib.auth.models import  AbstractBaseUser, BaseUserManager


class  UserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        if not email:raise ValueError("Users must have email address!")
        user= self.model( email= self.normalize_email(email), date_of_birth = date_of_birth)
        user.set_password(password)
        user.save(using=self.db)
        return user
    def create_super(self, email, date_of_birth, password=None ):
        user=self.create_user( email, password=password, date_of_birth= date_of_birth)
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
    username= models.CharField(unique=True, max_length= 30)
    first_name= models.CharField(max_length= 30)
    last_name= models.CharField(max_length= 30)
    date_joined= models.DateTimeField(auto_now_add=True)
    date_of_birth= models.DateField()
    weight= models.IntegerField()
    height= models.IntegerField()
    #TODO : goals=
    USERNAME_FIELD = 'email'
    def __str__(self):
       return self.email
    
    def has_perm(self, perm, obj=None ):
        return True
    def has_module_perms(self, app_label):
        return True
    @property
    def is_staff(self):
        return self.is_admin




