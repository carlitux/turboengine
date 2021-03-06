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

__all__ = []

from turboengine.errors import TException
from turboengine.webservices.hacks import SOAPHandlerChainFactory

from ZSI.twisted import wsgi

class WSGIApplication(wsgi.SOAPApplication):
    pass

class SOAPApplication(wsgi.SOAPApplication):
   
    factory = SOAPHandlerChainFactory
   
    def __init__(self, delegate, *args, **kwargs):
        '''Params:
        
            delegate: ServiceSOAPBinding object generated by ZSI that handles services
            *args, **kwargs: params valids for ZSI.SOAPAplication.
        '''
        wsgi.SOAPApplication.__init__(self, *args, **kwargs)
        self.delegate = delegate
   
    # overriden this method
    def _handle_GET(self, env, start_response):
        if env['QUERY_STRING'].lower() == 'wsdl':
            if hasattr(self.delegate, 'wsdl'):
                start_response('200 OK', [('Content-Type','text/xml; charset="utf-8')])
                return [self.delegate.wsdl]
            else:
                start_response('404 ERROR', [('Content-Type','text/html; charset="utf-8"')])
                return ['NO WSDL description found']
        if env['QUERY_STRING'].lower() == 'disco':
            if hasattr(self.delegate, 'disco'):
                start_response('200 OK', [('Content-Type','text/xml; charset="utf-8')])
                return [self.delegate.disco]
            else:
                start_response('404 ERROR', [('Content-Type','text/html; charset="utf-8"')])
                return ['NO disco description found']
        elif env['QUERY_STRING'].lower() == '':
            if hasattr(self.delegate, 'index'):
                start_response('200 OK', [('Content-Type','text/html; charset="utf-8')])
                return [self.delegate.index()]
            else:
                start_response('404 ERROR', [('Content-Type','text/html; charset="utf-8"')])
                return ['No index method found for root path.']
        else:
            start_response('404 ERROR', [('Content-Type','text/html; charset="utf-8"')])
            return ['NO RESOURCE FOR GET']