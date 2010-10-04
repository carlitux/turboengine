##################################################################################
# The MIT License - turboengine
#
# Copyright (c) Oct 2010 Luis C. Cruz <carlitos.kyo@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
##################################################################################

__all__ = ['RequestHandler']

from turboengine.conf import settings

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class RequestHandler(webapp.RequestHandler):
    '''Base request handler to provide common methods.'''
    
    @property
    def user(self):
        return users.get_current_user()

    def render_template(self, relative_path, parameters={}):
        self.response.out.write(template.render(settings.TEMPLATE_PATH%relative_path, parameters))
        