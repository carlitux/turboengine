##################################################################################
# The MIT License - turboengine
#
# Copyright (c) Oct 2010 - Luis C. Cruz <carlitos.kyo@gmail.com>
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

import os

TEMPLATE_PATH = 'templates'

# setting DEBUG
DEBUG = True
SITE_TITLE = 'turboengine for GAE'

# mapping (parent url, appname) 
INSTALLED_APPS = []

TEMPLATE_TAGS_PATHS = []

ERROR_PAGE_PATH = '/error/' # path where will be redirected the error

LOGIN_PATH_REDIRECT = '/'   # path where redirect after login or logout
LOGIN_PATH = '/accounts/login/'   # path where redirect after login or logout

SIGNUP_PATH = '/account/signup/'
PROFILE_PATH = '/account/profile/'

try:
    import settings
    _APP_DIR = os.path.abspath(os.path.dirname(settings.__file__))
    del settings
except ImportError:
    raise ImportError('Please define the settings.py file to set some configurations.')

from settings import *

TEMPLATE_PATH = os.path.join(_APP_DIR, TEMPLATE_PATH, '%s')
TEMPLATE_TAGS_PATHS = [ os.path.join(_APP_DIR, path) for path in TEMPLATE_TAGS_PATHS]