from django.test import TestCase


class EventPageTests(TestCase):
    def test_events_url_renders_event_template(self):
        response = self.client.get('/events/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Event.html')

    def test_navbar_pages_render(self):
        routes_and_templates = (
            ('/', 'homepage.html'),
            ('/events/', 'Event.html'),
            ('/services/', 'services.html'),
            ('/about/', 'Aboutus.html'),
            ('/contact/', 'Contactus.html'),
            ('/login/', 'login.html'),
            ('/signup/', 'signup.html'),
        )

        for route, template in routes_and_templates:
            with self.subTest(route=route):
                response = self.client.get(route)
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, template)
