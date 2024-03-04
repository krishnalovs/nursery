# models.py
from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from django.contrib.auth.models import User


class Navbar(models.Model):
    name = models.CharField(max_length=255, null=True)
    slug = AutoSlugField(populate_from='name', editable=True, always_update=True)
    img = models.URLField(max_length=200,null=True, blank=True)

    class Meta:
        verbose_name_plural = "Navbar"
        db_table = "Navbar"

    def __str__(self):
        return self.name
    def get_url(self):
        return reverse('nav_lists', args=[self.slug])


class Category(models.Model):
    navbar = models.ForeignKey(Navbar, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, null=True)
    slug = AutoSlugField(populate_from='name', editable=False, always_update=True)
    img = models.URLField(max_length=200,null=True, blank=True)

    class Meta:
        verbose_name_plural = "Category"
        db_table = "Category"

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('category_list', args=[self.slug])


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, null=True)
    slug = AutoSlugField(populate_from='name', editable=True, always_update=True)
    img = models.URLField(max_length=200,null=True, blank=True)
    
    def get_url(self):
        return reverse('subcategory_list', args=[self.category.slug,self.slug])

    class Meta:
        verbose_name_plural = "SubCategory"
        db_table = "SubCategory"

    def __str__(self):
        return self.name

class Items(models.Model):
    navbar = models.ForeignKey(Navbar, on_delete=models.CASCADE, null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,blank=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True,blank=True)
    name = models.CharField(max_length=255, null=True)
    slug = AutoSlugField(populate_from='name', editable=True, always_update=True)
    dis_price = models.DecimalField(max_digits=10, decimal_places=3)
    org_price = models.DecimalField(max_digits=10, decimal_places=3,default=0)
    img = models.URLField(max_length=7000,null=True)
    conditions = models.CharField(max_length=10000)
    offer =   models.CharField(max_length=5000)
    discount = models.DecimalField(max_digits=10, decimal_places=3,default=0)
    description = models.TextField(max_length=10000,default=0)

    class Meta:
        verbose_name_plural = "Items"
        db_table = "Items"
   
    def get_url(self):
        return reverse('product', args=[self.slug])

    def __str__(self):
        return self.name
    
    
class UserProfile(models.Model):
    first_name= models.CharField(max_length=100, null=True, blank=True)
    last_name= models.CharField(max_length=100, null=True, blank=True)
    username = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    image = models.FileField(null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.username.username
    class Meta:
        verbose_name_plural = "UserProfile"
        db_table = "UserProfile"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name_plural = "Cart"
        db_table = "Cart"

class Address(models.Model):
    number = models.IntegerField(default=0)
    user = models.ForeignKey (User, on_delete=models.CASCADE, null=True, blank=True)
    street_address = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    def __str__(self):
        return self.street_address 
    


choices = (('Received', 'Received'),
        ('Scheduled', 'Scheduled'), 
        ('Shipped', 'Shipped'),
        ('In Progress','In Progress'),
        )
class Order(models.Model):
    customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    name = models.CharField(max_length=30,null=True)
    status = models.CharField(max_length = 100, choices = choices ,default="In Progress")


class Feedback(models.Model):
    name=models.CharField(max_length=40)
    feedback=models.CharField(max_length=500)
    date= models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    number = models.IntegerField(default=0)
    company_name = models.CharField(max_length=1000)
    message =  models.TextField(max_length=10000)
    def __str__(self):
        return self.name
    
class Subscribe(models.Model):
        name = models.CharField(max_length=100)
        email = models.EmailField(max_length=254)
        def __str__(self):
          return self.name