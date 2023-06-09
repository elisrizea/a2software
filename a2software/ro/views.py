from django.shortcuts import render
from .models import HomePage, AboutPage


# Create your views here.
def home(request):

    home_page = HomePage.objects.filter().first()
    context = {
        # ***************************** sec 1 *************************** 
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
    return render(request, "ro/pag/home.html", context)


def about(request):
    home_page = HomePage.objects.filter().first()
    about_page = AboutPage.objects.filter().first()
    context = {

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


        # ***************************** sec 3a/b/c/d *************************** 

    }
    return render(request, "ro/pag/about.html", context)
