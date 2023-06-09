from django.shortcuts import render
from .models import HomePage, AboutPage, FaqsPage, AdmFaqs, CookiePage, PlatformPage, WebappePage, Testimonial, Menu
menu = Menu.objects.filter().first()

# Create your views here.


# **************************
# **************************
#
#      home page
#
# **************************
# **************************
def home(request):

    home_page = HomePage.objects.filter().first()
    
    context = {
        # ***************************** sec 1 *************************** 
        "menu": menu,
        "tile_1": home_page.t_1_title,
        "subtitle_1": home_page.t_1_subtitle,
        "description_1": home_page.t_1_description,


         # ***************************** sec 2 ***************************      
        "tile_2_1" : home_page.tile_2_1,
        "description_2_1" : home_page.description_2_1,

        "tile_2_2" : home_page.tile_2_2,
        "description_2_2" :home_page.description_2_2,

        "tile_2_3":home_page.tile_2_3,
        "description_2_3": home_page.description_2_3,

        "tile_2_4": home_page.tile_2_4,
        "description_2_4": home_page.description_2_4,

        "tile_2_5":home_page.tile_2_5,
        "description_2_5": home_page.description_2_5,

        "tile_2_6": home_page.tile_2_6,
        "description_2_6": home_page.description_2_6,


        # ***************************** sec 3a/b/c/d *************************** 

       "tile_3_a" : home_page.tile_3_a,
       "tile_3_b" : home_page.tile_3_b,
       "tile_3_c" : home_page.tile_3_c,
       "tile_3_d" : home_page.tile_3_d,

        # ***************************** sec 3 *************************** 
        "tile_3_1": home_page.tile_3_1,
        "description_3_1": home_page.description_3_1,

        "tile_3_2": home_page.tile_3_2,
        "description_3_2": home_page.description_3_2,

        # ***************************** sec 4 *************************** 

        "tile_4_1": home_page.tile_4_1,
        "description_4_2": home_page.description_4_2,

        "description_4_3": home_page.description_4_3,

        # ***************************** sec 5 *************************** 

        "tile_5_1": home_page.tile_5_1,
        "description_5_1": home_page.description_5_1,

        "tile_5_2": home_page.tile_5_2,
        "description_5_2": home_page.description_5_2,

        "tile_5_3": home_page.tile_5_3,
        "description_5_3": home_page.description_5_3,

    # **************** <!-- NEWSLETTER FORM -->*******************
    # not implemented yet
    }
    return render(request, "cms/pag/home.html", context)


# **************************
# **************************
#
#      about page
#
# **************************
# **************************
def about(request):
    home_page = HomePage.objects.filter().first()
    about_page = AboutPage.objects.filter().first()
    context = {
        "menu": menu,

         # ****************************** section from home ************************** 

        "tile_5_1": home_page.tile_5_1,
        "description_5_1": home_page.description_5_1,

        "tile_5_2": home_page.tile_5_2,
        "description_5_2": home_page.description_5_2,

        "tile_5_3": home_page.tile_5_3,
        "description_5_3": home_page.description_5_3,

        # ***************************** sec about 1  ***************************  

        "tile_0": about_page.tile_0,
        "description_0": about_page.description_0,

        # ***************************** sec about 2 ***************************      
        "tile_1" : about_page.tile_1,
        "description_1" : about_page.description_1,
        
        "tile_2" : about_page.tile_2,
        "description_2" :about_page.description_2,

        "tile_3":about_page.tile_3,
        "description_3": about_page.description_3,

        "tile_4": about_page.tile_4,
        "description_4": about_page.description_4,
    }
    return render(request, "cms/pag/about.html", context)



# **************************
# **************************
#
#      platform page
#
# **************************
# **************************
def platform(request):
    platform_page = PlatformPage.objects.filter().first()
    about_page = AboutPage.objects.filter().first()
    adm_faqs = AdmFaqs.objects.filter().order_by('-id')[:5:-1]
    faqs_page = FaqsPage.objects.filter().first()
   
    context = {
        "menu": menu,
        "tile_0": platform_page.tile_0,
        "description_0": platform_page.description_0,
        "description_0_1": platform_page.description_0_1,

        "tile_1": platform_page.tile_1,
        "tile_1_1": platform_page.tile_1_1,
        "description_1": platform_page.description_1,

        "tile_2": platform_page.tile_2,
        "description_2": platform_page.description_2,

        "description_3": platform_page.description_3,

        "tile_4": platform_page.tile_4,
        "tile_4_1": platform_page.tile_4_1,
        "description_4": platform_page.description_4,

        "tile_5": platform_page.tile_5,
        "description_5": platform_page.description_5,

        # external content
        "tile_about": about_page.tile_0,
        "description_about": about_page.description_0,
        "button_question": faqs_page.button_question,
        "button_name": faqs_page.button_name,

        "faqs": adm_faqs,




    }
    return render(request, "cms/pag/platform.html", context)

# **************************
# **************************
#
#      faqs page
#
# **************************
# **************************
def faqs(request):
    faqs_page = FaqsPage.objects.filter().first()
    adm_faqs = AdmFaqs.objects.all()
    adm_faqs_left=[]
    adm_faqs_right=[]

    for adm_faq in list(adm_faqs):
        if adm_faq.id%2 ==1 :
            adm_faqs_left.append(adm_faq)
        else:
            adm_faqs_right.append(adm_faq)


   
    context = {
        "menu": menu,
        "tile_0": faqs_page.tile_0,
        "description_0": faqs_page.description_0,
        "faqs_left": adm_faqs_left,
        "faqs_right": adm_faqs_right,
        "button_question": faqs_page.button_question,
        "button_name": faqs_page.button_name,
        
    }
    return render(request, "cms/pag/faqs.html", context)


# **************************
# **************************
#
#      cookie page
#
# **************************
# **************************
def cookie(request):
    cookie_page = CookiePage.objects.filter().first()
   
    context = {
        "menu": menu,
        "tile_0": cookie_page.tile_0,
        "description_0": cookie_page.description_0,
    }
    return render(request, "cms/pag/cookie.html", context)


# **************************
# **************************
#
#      Webapp page
#
# **************************
# **************************
def webapp(request):
    webapp_page = WebappePage.objects.filter().first()
    testimonials = Testimonial.objects.all()


   
    context = {
        "menu": menu,
        "tile": webapp_page.tile_0,
        "description": webapp_page.description_0,

        "tile_1": webapp_page.tile_1,
        "description_1": webapp_page.description_1,

        "testimonials" : testimonials
    }
    return render(request, "cms/pag/webapp.html", context)

# **************************
# **************************
#
#      contact page
#
# **************************
# **************************
def contact(request):

   
    context = {
        "menu": menu,
   
    }
    return render(request, "cms/pag/contact.html", context)


    # **************************
# **************************
#
#      contact page
#
# **************************
# **************************

