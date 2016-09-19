from app import app
import unittest

class FlaskTestCase(unittest.TestCase):

    #ensuring flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)          #test client is what's used to create a test, mocking up the functionslity of current app
        response = tester.get('/login', content_type='html/text') #using unittest lib to call login route
        self.assertEqual(response.status_code, 200) #checking if response status code if== 200

    #ensure page loads corectly
    def test_login(self):
        tester = app.test_client(self)          #test client is what's used to create a test, mocking up the functionslity of current app
        response = tester.get('/login', content_type = 'html/text') #using unittest lib to call login route
        self.assertTrue(b'Please login' in response.data) #check if 'Log in first' is part of the login page

    #login behaviour given correct credentials
    def test_login_correctness(self):
        tester = app.test_client( self)
        response = tester.post('/login', data=dict(username="admin", password="admin"),
                                   follow_redirects=True)  # using unittest lib to call login route
        self.assertIn('you logged in', response.data)

    # login behaviour given false credentials
    def test_false_login(self):
        tester = app.test_client( self)
        response = tester.post('/login', data=dict(username="admid", password="vdmin"),
                                   follow_redirects=True)  # using unittest lib to call login route
        self.assertIn(b'Invalid credentials. Please enter correct details', response.data)

    #login required
    def test_login_required(self):
        tester = app.test_client(self)
        response = tester.get('/', follow_redirects=True)
        self.assertTrue(b'Log in first' in response.data)

    #posts in main page
    def test_post(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username="admin", password="admin"),
                               follow_redirects=True)  # using unittest lib to call login route
        self.assertIn('post: looking', response.data)


if __name__== '__main__':
    unittest.main()