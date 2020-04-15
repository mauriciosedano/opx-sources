from django.test import SimpleTestCase, TestCase, Client

class ProjectTest(TestCase):
    def list(self):
        c = Client()
        response = c.get('/proyectos/list/')

        self.assertEqual(response.status_code, 300)