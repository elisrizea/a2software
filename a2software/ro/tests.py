from django.test import TestCase
from django.urls import reverse
from .models import (
    HomePage,
    AboutPage,
    FaqsPage,
    AdmFaqs,
    CookiePage,
    PlatformPage,
    WebappePage,
    Testimonial,
    BaseHeaderFooterMenu,
)


# ***** Moddels Tests ***********************************************
class ModelsTestCase(TestCase):
    # ****** Test HomePage ******************************************
    def test_home_page_model(self):
        homepage = HomePage.objects.create(
            t_1_title="TestTitle",
            t_1_subtitle="TestSubtitle",
            t_1_description="TestDescription",
            tile_2_1="TestTile1",
            description_2_1="TestDescription1",
        )
        self.assertEqual("TestTitle", homepage.t_1_title)
        self.assertEqual("TestSubtitle", homepage.t_1_subtitle)
        self.assertEqual("TestDescription", homepage.t_1_description)
        self.assertEqual("TestTile1", homepage.tile_2_1)
        self.assertEqual("TestDescription1", homepage.description_2_1)
        self.assertEqual(str(homepage), "Hompage Page Content")

    # ****** Test AboutPage ******************************************

    def test_about_page_model(self):
        aboutpage = AboutPage.objects.create(
            tile_0="TestTile0",
            description_0="TestDescription0",
            tile_1="TestTile1",
            description_1="TestDescription1",
        )
        self.assertEqual("TestTile0", aboutpage.tile_0)
        self.assertEqual("TestDescription0", aboutpage.description_0)
        self.assertEqual("TestTile1", aboutpage.tile_1)
        self.assertEqual("TestDescription1", aboutpage.description_1)
        self.assertEqual(str(aboutpage), "About Page Content")

    # ****** Test FaqsPage ******************************************

    def test_faqs_page_model(self):
        faqspage = FaqsPage.objects.create(
            tile_0="TestTile0",
            description_0="TestDescription0",
            button_question="TestQuestion",
            button_name="TestButtonName",
        )

        self.assertEqual("TestTile0", faqspage.tile_0)
        self.assertEqual("TestDescription0", faqspage.description_0)
        self.assertEqual("TestQuestion", faqspage.button_question)
        self.assertEqual("TestButtonName", faqspage.button_name)
        self.assertEqual(str(faqspage), "FAQs Page Content")

    # ****** Test PlatformPage ******************************************

    def test_patform_page_model(self):
        platform_page = PlatformPage.objects.create(
            tile_0="tile_0",
            description_0="description_0",
            description_0_1="description_0_1",
            tile_1="tile_1",
            tile_1_1="tile_1_1",
            description_1="description_1",
            tile_2="tile_2",
            description_2="description_2",
            description_3="description_3",
            tile_4="tile_4",
            tile_4_1="tile_4_1",
            description_4="description_4",
            tile_5="tile_5",
            description_5="description_5",
        )

        self.assertEqual("tile_0", platform_page.tile_0)
        self.assertEqual("description_0", platform_page.description_0)
        self.assertEqual("description_0_1", platform_page.description_0_1)
        self.assertEqual("tile_1", platform_page.tile_1)
        self.assertEqual("tile_1_1", platform_page.tile_1_1)
        self.assertEqual("description_1", platform_page.description_1)
        self.assertEqual("tile_2", platform_page.tile_2)
        self.assertEqual("description_2", platform_page.description_2)
        self.assertEqual("description_3", platform_page.description_3)
        self.assertEqual("tile_4", platform_page.tile_4)
        self.assertEqual("tile_4_1", platform_page.tile_4_1)
        self.assertEqual("description_4", platform_page.description_4)
        self.assertEqual("tile_5", platform_page.tile_5)
        self.assertEqual("description_5", platform_page.description_5)
        self.assertEqual(str(platform_page), "Our Platform Page Content")

    # ****** Test CookiePage ******************************************

    def test_coockie_page_model(self):
        coockiepage = CookiePage.objects.create(
            tile_0="TestTile0",
            description_0="TestDescription0",
        )

        self.assertEqual("TestTile0", coockiepage.tile_0)
        self.assertEqual("TestDescription0", coockiepage.description_0)
        self.assertEqual(str(coockiepage), "T&C Page Content")

    # ****** Test Testimonial ******************************************

    def test_testimonial_page_model(self):
        testimonialspage = Testimonial.objects.create(
            title="TestTile0",
            description="TestDescription0",
        )

        self.assertEqual("TestTile0", testimonialspage.title)
        self.assertEqual("TestDescription0", testimonialspage.description)
        self.assertEqual(str(testimonialspage), testimonialspage.title)

    # ****** Test WebappePage ******************************************

    def test_testimonial_page_model(self):
        testimonialspage = WebappePage.objects.create(
            tile_0="TestTile0",
            description_0="TestDescription0",
            tile_1="TestTile0",
            description_1="TestDescription0",
        )

        self.assertEqual("TestTile0", testimonialspage.tile_0)
        self.assertEqual("TestDescription0", testimonialspage.description_0)
        self.assertEqual("TestTile0", testimonialspage.tile_1)
        self.assertEqual("TestDescription0", testimonialspage.description_1)
        self.assertEqual(str(testimonialspage), "Webapp Page Content")

    # ****** Test CookiePage ******************************************

    def test_faqs_page_model(self):
        faqspage = FaqsPage.objects.create(
            tile_0="TestTile0",
            description_0="TestDescription0",
            button_question="TestQuestion",
            button_name="TestButtonName",
        )

        self.assertEqual("TestTile0", faqspage.tile_0)
        self.assertEqual("TestDescription0", faqspage.description_0)
        self.assertEqual("TestQuestion", faqspage.button_question)
        self.assertEqual("TestButtonName", faqspage.button_name)
        self.assertEqual(str(faqspage), "FAQs Page Content")

    # ****** Test FAQs model ******************************************
    def test_adm_faqs_model(self):
        admfaqs = AdmFaqs.objects.create(
            question="TestQuestion",
            answer="TestAnswer",
        )
        self.assertEqual("TestQuestion", admfaqs.question)
        self.assertEqual("TestAnswer", admfaqs.answer)
        self.assertEqual(str(admfaqs), admfaqs.question)


# ****** Test BaseHeaderFooterMenuTestCase model ******************************************
class BaseHeaderFooterMenuTestCase(TestCase):
    def test_base_header_footer_menu_model(self):
        baseheaderfootermenu = BaseHeaderFooterMenu.objects.create(
            m_home="Home",
            m_about="About",
            m_platform="Platform",
            m_store="Store",
            m_faqs="FAQs",
            m_coockie="Cookie",
            m_contact="Contact",
            m_partner="Partner",
            m_webapp="Webapp",
            h_title="TestHeaderTitle",
            h_meta_author="TestMetaAuthor",
            h_meta_keywords="TestMetaKeywords",
            h_meta_description="TestMetaDescription",
            f_moto_description="TestMotoDescription",
            f_about_title="TestAboutTitle",
            f_company_title="TestCompanyTitle",
            f_info_title="TestInfoTitle",
            f_support_title="TestSupportTitle",
        )
        self.assertEqual("Home", baseheaderfootermenu.m_home)
        self.assertEqual("About", baseheaderfootermenu.m_about)
        self.assertEqual("Platform", baseheaderfootermenu.m_platform)
        self.assertEqual("FAQs", baseheaderfootermenu.m_faqs)
        self.assertEqual("Cookie", baseheaderfootermenu.m_coockie)
        self.assertEqual("Contact", baseheaderfootermenu.m_contact)
        self.assertEqual("Partner", baseheaderfootermenu.m_partner)
        self.assertEqual("Webapp", baseheaderfootermenu.m_webapp)
        self.assertEqual("TestHeaderTitle", baseheaderfootermenu.h_title)
        self.assertEqual("TestMetaAuthor", baseheaderfootermenu.h_meta_author)
        self.assertEqual(str(baseheaderfootermenu), "edit Header Footer Menu")


# ***************************** tests views ***************************


class ViewsTestCase(TestCase):
    def setUp(self):
        # Create test data
        self.header_footer_menu = BaseHeaderFooterMenu.objects.create()
        self.home_page = HomePage.objects.create(
            t_1_title="Title 1",
            t_1_subtitle="Subtitle 1",
            t_1_description="Description 1",
        )
        self.about_page = AboutPage.objects.create(
            tile_0="Tile 0", description_0="Description"
        )
        self.platform_page = PlatformPage.objects.create(
            tile_0="Tile 0", description_0="Description 0"
        )
        self.faqs_page = FaqsPage.objects.create(
            tile_0="Tile 0", description_0="Description 0"
        )
        self.cookie_page = CookiePage.objects.create(
            tile_0="Tile 0", description_0="Description 0"
        )
        self.webapp_page = WebappePage.objects.create(
            tile_0="Tile 0", description_0="Description 0"
        )

    def test_home_view(self):
        url = reverse("home")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cms/pag/home.html")

    def test_about_view(self):
        url = reverse("about")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cms/pag/about.html")

    def test_platform_view(self):
        url = reverse("platform")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cms/pag/platform.html")
        self.assertContains(response, "Tile 0")
        self.assertContains(response, "Description 0")

    def test_faqs_view(self):
        url = reverse("faqs")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cms/pag/faqs.html")
        self.assertContains(response, "Tile 0")
        self.assertContains(response, "Description 0")

    def test_cookie_view(self):
        url = reverse("cookie")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cms/pag/cookie.html")
        self.assertContains(response, "Tile 0")
        self.assertContains(response, "Description 0")

    def test_webapp_view(self):
        url = reverse("webapp")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cms/pag/webapp.html")
        self.assertContains(response, "Tile 0")
        self.assertContains(response, "Description 0")

    def test_contact_view(self):
        url = reverse("contact")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cms/pag/contact.html")


# *********** test urls *****************************


class UrlsTestCase(TestCase):
    def test_home_url(self):
        url = reverse("home")
        self.assertEqual(url, "/ro/home/")

    def test_about_url(self):
        url = reverse("about")
        self.assertEqual(url, "/ro/about/")

    def test_platform_url(self):
        url = reverse("platform")
        self.assertEqual(url, "/ro/platform/")

    def test_faqs_url(self):
        url = reverse("faqs")
        self.assertEqual(url, "/ro/faqs/")

    def test_cookie_url(self):
        url = reverse("cookie")
        self.assertEqual(url, "/ro/cookie/")

    def test_webapp_url(self):
        url = reverse("webapp")
        self.assertEqual(url, "/ro/webapp/")

    def test_contact_url(self):
        url = reverse("contact")
        self.assertEqual(url, "/ro/contact/")
