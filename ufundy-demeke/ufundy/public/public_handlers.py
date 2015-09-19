import webapp2

from ufundy import basehandler


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class HomeHandler(basehandler.BaseHandler):
    def get(self):

        page_title = 'testapp - The CrowdFunding Portal'
        page_description = 'testapp - The CrowdFunding Portal'

        context = {'page_title': page_title, \
                    'page_description': page_description, \
                    }

        self.render_response('public/splash.html', **context)
