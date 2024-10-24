from flask_testing import TestCase
from flask import current_app, url_for
from main import app

class MainTest(TestCase):
    def create_app(self):
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        return super().create_app()
    
    def test_app_exists_web(self):
        self.assertIsNotNone(current_app)
    
    def test_app_in_testing_mode(self):
        app.assertTrue(current_app.config['TESTING'])
    
    def test_index_redirects(self):
        response = self.client.get(url_for("index"))
        self.assertRedirects(response, url_for("show_information"))
        
    def test_show_infromation_get(self):
        response = self.client.get(url_for("show_informationx"))
        self.assert200(response)

    def test_show_infromation_post(self):
        test_form_fake = {
            "username":"faso2000",
            "password": "Cl4v3123*"
        }
        response = self.client.get(url_for("show_information"), data = test_form_fake)
        self.assertRedirects(response, url_for("index"))

    def test_auth_blueprint_exists_module(self):
        self.assertIn("auth", self.app.blueprints())
