from django.db import models
from ecoapp.utils import create_slug_shortcode
from django.contrib.auth import get_user, get_user_model
from datetime import datetime
from django.utils.text import slugify
from utils import seo
User = get_user_model()

class BaseMixin(models.Model):
    slug = models.SlugField(unique=True,editable=False,blank=True,null=True)
    created_at = models.DateField(auto_now_add=True,blank=True,null=True,)
    seo_title = models.CharField(max_length=1200,null=True,blank=True,verbose_name='title for seo')
    seo_keyword = models.CharField(max_length=1200,null=True,blank=True,verbose_name='keyword for seo')
    seo_description = models.CharField(max_length=1200,null=True,blank=True,verbose_name='description for seo')
    
    class Meta:
        abstract = True

class Subject(models.Model):
    name = models.CharField(max_length=340)
    def __str__(self):
        return self.name
    
class Blog(BaseMixin):
    title = models.CharField(max_length=1200)
    description = models.TextField()
    views = models.SmallIntegerField(default=0)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(null=True,blank=True)
    

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        new_slug = slugify(self.title)
        
        if Blog.objects.filter(slug=new_slug).exists():
            count = 1
            while Blog.objects.filter(slug=new_slug).exists():
                new_slug = f"{slugify(self.title)}-{count}"
                count += 1
        self.slug = new_slug
        super(Blog, self).save(*args, **kwargs)  
       
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Brend(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField()
    
    def __str__(self):
        return self.name
    
class Product(BaseMixin):
    name = models.CharField(max_length=200)
    price = models.SmallIntegerField()
    discount_price = models.SmallIntegerField()
    wishlist = models.ManyToManyField(User,blank=True)
    stock = models.BooleanField(default=True)
    weight = models.CharField(max_length=220)
    brend = models.ForeignKey(Brend,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    lifetime = models.CharField(max_length=100)
    description = models.TextField()
    information = models.TextField()
    image = models.ImageField(null=True,blank=True)
    hoverimage = models.ImageField(null=True,blank=True)
    hot = models.BooleanField(default=False)
    def __str__(self):
        return self.name
        
    def save(self, *args, **kwargs):
        new_slug = slugify(self.name)
        self.slug = new_slug
        if Product.objects.filter(slug=new_slug).exists():

            count = 1
            while Product.objects.filter(slug=new_slug).exists():
                new_slug = f"{slugify(self.name)}-{count}"
                count += 1
        super(Product, self).save(*args, **kwargs)
        
    
    
class NutritionValue(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='terkib')
    name = models.CharField(max_length=200)
    value = models.FloatField()
    
    def __str__(self):
        return self.name

class Basket_card(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='products')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    
    def __str__(self):
        return self.product.name
    
#9BB61B
class Header(models.Model):
    title = models.CharField(max_length=520)
    minititle = models.CharField(max_length=520)
    image = models.ImageField()
    link = models.CharField(max_length=900)
    
    def __str__(self):
        return self.title
    
class HomeAbout(models.Model):
    minititle = models.CharField(max_length=230)
    title = models.CharField(max_length=230)
    description1 = models.TextField() 
    description2 = models.TextField() 
    image1 = models.ImageField()
    image2 = models.ImageField()
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.pk = 1
        super(HomeAbout, self).save(*args, **kwargs)
        
class HomeIcons(models.Model):
    title = models.CharField(max_length=100)
    icon = models.ImageField()
    
    def __str__(self):
        return self.title
    
class Partners(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    
    def __str__(self):
        return self.title


class Slides(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    link = models.CharField(max_length=2050,null=True,blank=True)

    def __str__(self):
        return self.title


class Message(models.Model):
    name = models.CharField(max_length=600)
    message = models.TextField()
    email = models.EmailField()
    
    def __str__(self):
        return self.name + '---'