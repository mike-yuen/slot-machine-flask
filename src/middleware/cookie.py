class CookieMiddleWare(object):
    """ Simple WSGI middleware """


    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        # Get the cookies from the environ dictionary
        cookies = environ.get('HTTP_COOKIE')

        # Process the cookies as needed
        if cookies:
            print("Cookies:", cookies)

        return self.app(environ, start_response)