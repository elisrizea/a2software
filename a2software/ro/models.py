from django.db import models

# Create your models here.
class HomePage(models.Model):
    # ***************************** sec 1 *************************** 
    t_1_title = models.CharField(max_length=150, null=False, blank=False, default="ok")
    t_1_subtitle = models.CharField(max_length=150, null=False, blank=False, default="ok")
    t_1_description = models.TextField(null=False, blank=False, default="ok")

    # ***************************** sec 2 ***************************     
    tile_2_1 = models.CharField(max_length=150, null=False, blank=False)
    description_2_1=models.TextField(null=False, blank=False)

    tile_2_2 = models.CharField(max_length=150, null=False, blank=False)
    description_2_2=models.TextField(null=False, blank=False)

    tile_2_3 = models.CharField(max_length=150, null=False, blank=False)
    description_2_3=models.TextField(null=False, blank=False)

    tile_2_4 = models.CharField(max_length=150, null=False, blank=False)
    description_2_4=models.TextField(null=False, blank=False)

    tile_2_5 = models.CharField(max_length=150, null=False, blank=False)
    description_2_5=models.TextField(null=False, blank=False)

    tile_2_6 = models.CharField(max_length=150, null=False, blank=False)
    description_2_6=models.TextField(null=False, blank=False)

    subtitle_1 = models.CharField(max_length=150, null=False, blank=False)
    description_1=models.TextField(null=False, blank=False)

    # ***************************** sec 3 a/b/c/d *************************** 
    tile_3_a= models.CharField(max_length=150, null=False, blank=False)
    tile_3_b= models.CharField(max_length=150, null=False, blank=False)
    tile_3_c= models.CharField(max_length=150, null=False, blank=False)
    tile_3_d= models.CharField(max_length=150, null=False, blank=False)

    # ***************************** sec 3 ***************************  
    tile_3_1 = models.CharField(max_length=150, null=False, blank=False)
    description_3_1=models.TextField(null=False, blank=False)

    tile_3_2 = models.CharField(max_length=150, null=False, blank=False)
    description_3_2=models.TextField(null=False, blank=False)

    # ***************************** sec 4 ***************************  
    tile_4_1 = models.CharField(max_length=150, null=False, blank=False)
    description_4_2=models.TextField(null=False, blank=False)
    description_4_3=models.TextField(null=False, blank=False)

    # ***************************** sec 5 ***************************     
    tile_5_1 = models.CharField(max_length=150, null=False, blank=False)
    description_5_1=models.TextField(null=False, blank=False)

    tile_5_2 = models.CharField(max_length=150, null=False, blank=False)
    description_5_2=models.TextField(null=False, blank=False)

    tile_5_3 = models.CharField(max_length=150, null=False, blank=False)
    description_5_3=models.TextField(null=False, blank=False)

    def __str__(self):
        return 'Hompage Page Content'



class AboutPage(models.Model):
    # ***************************** sec about *************************** 

    tile_0 = models.CharField(max_length=150, null=False, blank=False)
    description_0=models.TextField(null=False, blank=False)

    tile_1 = models.CharField(max_length=150, null=False, blank=False)
    description_1=models.TextField(null=False, blank=False)

    tile_2 = models.CharField(max_length=150, null=False, blank=False)
    description_2=models.TextField(null=False, blank=False)

    tile_3 = models.CharField(max_length=150, null=False, blank=False)
    description_3=models.TextField(null=False, blank=False)

    tile_4 = models.CharField(max_length=150, null=False, blank=False)
    description_4=models.TextField(null=False, blank=False)

    def __str__(self):
        return 'About Page Content'


class FaqsPage(models.Model):
    # ***************************** sec about *************************** 

    tile_0 = models.CharField(max_length=150, null=False, blank=False)
    description_0=models.TextField(null=False, blank=False)
    button_question = models.CharField(max_length=150, null=True, blank=True)
    button_name = models.CharField(max_length=150, null=True, blank=False)

    def __str__(self):
        return 'FAQs Page Content'



class AdmFaqs(models.Model):
    # ***************************** sec about *************************** 

    question = models.CharField(max_length=250, null=False, blank=False)
    answer=models.TextField(null=False, blank=False)

    def __str__(self):
        return self.question

class PlatformPage(models.Model):
    # ***************************** sec about *************************** 

    tile_0 = models.CharField(max_length=150, null=False, blank=False, default="ok")
    description_0=models.TextField(null=True, blank=False, default="ok")
    description_0_1 = models.TextField(null=False, blank=False, default="ok")

    tile_1 = models.CharField(max_length=150, null=False, blank=False , default="ok")
    tile_1_1 = models.CharField(max_length=150, null=True, blank=False, default="ok")
    description_1=models.TextField(null=False, blank=False , default="ok")

    tile_2 = models.CharField(max_length=150, null=False, blank=False, default="ok")
    description_2=models.TextField(null=False, blank=False, default="ok")

    description_3=models.TextField(null=False, blank=False, default="ok")

    tile_4 = models.CharField(max_length=150, null=False, blank=False, default="ok")
    tile_4_1 = models.CharField(max_length=150, null=True, blank=False, default="ok")
    description_4=models.TextField(null=False, blank=False, default="ok")

    tile_5 = models.CharField(max_length=150, null=False, blank=False, default="ok")
    description_5=models.TextField(null=False, blank=False, default="ok")

    def __str__(self):
        return 'Our Platform Page Content'

class CookiePage(models.Model):
    # ***************************** sec about *************************** 

    tile_0 = models.CharField(max_length=150, null=False, blank=False)
    description_0=models.TextField(null=False, blank=False)

    def __str__(self):
        return 'T&C Page Content'

class WebappePage(models.Model):
    # ***************************** sec about *************************** 

    tile_0 = models.CharField(max_length=150, null=False, blank=False, default="ok")
    description_0=models.TextField(null=False, blank=False, default="ok")

    tile_1 = models.CharField(max_length=150, null=False, blank=False, default="ok")
    description_1 = models.TextField(null=False, blank=False)

    def __str__(self):
        return 'Webapp Page Content'



class Testimonial(models.Model):
    # ***************************** sec about *************************** 

    title = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.title


class Menu(models.Model):
    # ***************************** sec about *************************** 

    home = models.CharField(max_length=80, null=False, blank=False)
    about = models.CharField(max_length=80, null=False, blank=False)
    platform = models.CharField(max_length=80, null=False, blank=False)
    store = models.CharField(max_length=80, null=False, blank=False)
    faqs = models.CharField(max_length=80, null=False, blank=False)
    coockie = models.CharField(max_length=80, null=False, blank=False)
    contact = models.CharField(max_length=80, null=False, blank=False)
    partner = models.CharField(max_length=80, null=False, blank=False)
    webapp = models.CharField(max_length=80, null=False, blank=False)
    

    def __str__(self):
        return "edit menu"