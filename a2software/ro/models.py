from django.db import models


# ***************************** HomePage ***************************
class HomePage(models.Model):
    class Meta:
        verbose_name = "PAGES: Home"
        verbose_name_plural = "PAGES: Home"

    # ***************************** sec 1 ***************************
    t_1_title = models.CharField(max_length=150, null=False, blank=False, default="ok")
    t_1_subtitle = models.CharField(
        max_length=150, null=False, blank=False, default="ok"
    )
    t_1_description = models.TextField(null=False, blank=False, default="ok")

    # ***************************** sec 2 ***************************
    tile_2_1 = models.CharField(max_length=150, null=False, blank=False)
    description_2_1 = models.TextField(null=False, blank=False)

    tile_2_2 = models.CharField(max_length=150, null=False, blank=False)
    description_2_2 = models.TextField(null=False, blank=False)

    tile_2_3 = models.CharField(max_length=150, null=False, blank=False)
    description_2_3 = models.TextField(null=False, blank=False)

    tile_2_4 = models.CharField(max_length=150, null=False, blank=False)
    description_2_4 = models.TextField(null=False, blank=False)

    tile_2_5 = models.CharField(max_length=150, null=False, blank=False)
    description_2_5 = models.TextField(null=False, blank=False)

    tile_2_6 = models.CharField(max_length=150, null=False, blank=False)
    description_2_6 = models.TextField(null=False, blank=False)

    subtitle_1 = models.CharField(max_length=150, null=False, blank=False)
    description_1 = models.TextField(null=False, blank=False)

    # ***************************** sec 3 a/b/c/d ***************************
    tile_3_a = models.CharField(max_length=150, null=False, blank=False)
    tile_3_b = models.CharField(max_length=150, null=False, blank=False)
    tile_3_c = models.CharField(max_length=150, null=False, blank=False)
    tile_3_d = models.CharField(max_length=150, null=False, blank=False)

    # ***************************** sec 3 ***************************
    tile_3_1 = models.CharField(max_length=150, null=False, blank=False)
    description_3_1 = models.TextField(null=False, blank=False)

    tile_3_2 = models.CharField(max_length=150, null=False, blank=False)
    description_3_2 = models.TextField(null=False, blank=False)

    # ***************************** sec 4 ***************************
    tile_4_1 = models.CharField(max_length=150, null=False, blank=False)
    description_4_2 = models.TextField(null=False, blank=False)
    description_4_3 = models.TextField(null=False, blank=False)

    # ***************************** sec 5 ***************************
    tile_5_1 = models.CharField(max_length=150, null=False, blank=False)
    description_5_1 = models.TextField(null=False, blank=False)

    tile_5_2 = models.CharField(max_length=150, null=False, blank=False)
    description_5_2 = models.TextField(null=False, blank=False)

    tile_5_3 = models.CharField(max_length=150, null=False, blank=False)
    description_5_3 = models.TextField(null=False, blank=False)

    def __str__(self):
        return "Hompage Page Content"


# ***************************** AboutPage ***************************
class AboutPage(models.Model):
    class Meta:
        verbose_name = "PAGES: About"
        verbose_name_plural = "PAGES: About"

    tile_0 = models.CharField(max_length=150, null=False, blank=False)
    description_0 = models.TextField(null=False, blank=False)

    tile_1 = models.CharField(max_length=150, null=False, blank=False)
    description_1 = models.TextField(null=False, blank=False)

    tile_2 = models.CharField(max_length=150, null=False, blank=False)
    description_2 = models.TextField(null=False, blank=False)

    tile_3 = models.CharField(max_length=150, null=False, blank=False)
    description_3 = models.TextField(null=False, blank=False)

    tile_4 = models.CharField(max_length=150, null=False, blank=False)
    description_4 = models.TextField(null=False, blank=False)

    def __str__(self):
        return "About Page Content"


# ***************************** FaqsPage ***************************
class FaqsPage(models.Model):
    class Meta:
        verbose_name = "PAGES: Faq"
        verbose_name_plural = "PAGES: Faq"

    tile_0 = models.CharField(max_length=150, null=False, blank=False)
    description_0 = models.TextField(null=False, blank=False)
    button_question = models.CharField(max_length=150, null=True, blank=True)
    button_name = models.CharField(max_length=150, null=True, blank=False)

    def __str__(self):
        return "FAQs Page Content"


# ***************************** Admin Faqs ***************************
class AdmFaqs(models.Model):
    class Meta:
        verbose_name = "FAQs"
        verbose_name_plural = "FAQs"

    question = models.CharField(max_length=250, null=False, blank=False)
    answer = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.question


# ***************************** PlatformPage ***************************
class PlatformPage(models.Model):
    class Meta:
        verbose_name = "PAGES: Platform"
        verbose_name_plural = "PAGES: Platform"

    tile_0 = models.CharField(max_length=150, null=False, blank=False, default="ok")
    description_0 = models.TextField(null=True, blank=False, default="ok")
    description_0_1 = models.TextField(null=False, blank=False, default="ok")

    tile_1 = models.CharField(max_length=150, null=False, blank=False, default="ok")
    tile_1_1 = models.CharField(max_length=150, null=True, blank=False, default="ok")
    description_1 = models.TextField(null=False, blank=False, default="ok")

    tile_2 = models.CharField(max_length=150, null=False, blank=False, default="ok")
    description_2 = models.TextField(null=False, blank=False, default="ok")

    description_3 = models.TextField(null=False, blank=False, default="ok")

    tile_4 = models.CharField(max_length=150, null=False, blank=False, default="ok")
    tile_4_1 = models.CharField(max_length=150, null=True, blank=False, default="ok")
    description_4 = models.TextField(null=False, blank=False, default="ok")

    tile_5 = models.CharField(max_length=150, null=False, blank=False, default="ok")
    description_5 = models.TextField(null=False, blank=False, default="ok")

    def __str__(self):
        return "Our Platform Page Content"


# ***************************** T&C Page ***************************
class CookiePage(models.Model):
    class Meta:
        verbose_name = "PAGES: T&C"
        verbose_name_plural = "PAGES: T&C"

    tile_0 = models.CharField(max_length=150, null=False, blank=False)
    description_0 = models.TextField(null=False, blank=False)

    def __str__(self):
        return "T&C Page Content"


# ***************************** WebappePage ***************************
class WebappePage(models.Model):
    class Meta:
        verbose_name = "PAGES: Webapp"
        verbose_name_plural = "PAGES: Webapp"

    tile_0 = models.CharField(max_length=150, null=False, blank=False, default="ok")
    description_0 = models.TextField(null=False, blank=False, default="ok")

    tile_1 = models.CharField(max_length=150, null=False, blank=False, default="ok")
    description_1 = models.TextField(null=False, blank=False)

    def __str__(self):
        return "Webapp Page Content"


# ***************************** Testimonial ***************************
class Testimonial(models.Model):
    class Meta:
        verbose_name = "CARDS Webap"
        verbose_name_plural = "CARDS Webap"

    title = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.title


# ***************************** BaseHeaderFooterMenu ***************************
class BaseHeaderFooterMenu(models.Model):
    class Meta:
        verbose_name = "EDIT Header, Footer, Menu"
        verbose_name_plural = "EDIT Header, Footer, Menu"

    # ***************************** menu ***************************
    m_home = models.CharField(max_length=80, null=False, blank=False)
    m_about = models.CharField(max_length=80, null=False, blank=False)
    m_platform = models.CharField(max_length=80, null=False, blank=False)
    m_store = models.CharField(max_length=80, null=False, blank=False)
    m_faqs = models.CharField(max_length=80, null=False, blank=False)
    m_coockie = models.CharField(max_length=80, null=False, blank=False)
    m_contact = models.CharField(max_length=80, null=False, blank=False)
    m_partner = models.CharField(max_length=80, null=False, blank=False)
    m_webapp = models.CharField(max_length=80, null=False, blank=False)

    # ***************************** header ***************************
    h_title = models.CharField(max_length=80, null=False, blank=False)
    h_meta_author = models.CharField(max_length=80, null=False, blank=False)
    h_meta_keywords = models.TextField(null=False, blank=False)
    h_meta_description = models.TextField(null=False, blank=False)

    # ***************************** footer ***************************
    f_moto_description = models.TextField(null=False, blank=False)
    f_about_title = models.CharField(max_length=80, null=False, blank=False)
    f_company_title = models.CharField(max_length=80, null=False, blank=False)
    f_info_title = models.CharField(max_length=80, null=False, blank=False)
    f_support_title = models.CharField(max_length=80, null=False, blank=False)

    def __str__(self):
        return "edit Header Footer Menu"
