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

__all__ = ['SOAPCallbackHandler', 'SOAPHandlerChainFactory']

from turboengine.errors import TException

try:
    from ZSI.twisted import wsgi
    
    from ZSI.twisted.reverse import ReverseHandlerChain
    from ZSI.twisted.reverse import DataHandler
except ImportError:
    raise TException('If you want to use webservices please install ZSI and zope.interface or put it into PYTHONPATH')


##################################################################################
## Hacking this class to enable a ServiceSOAPBinding subclass with wsgi
## And SOAPApplication and delegate field.
##################################################################################


class SOAPCallbackHandler(wsgi.SOAPCallbackHandler):

    @classmethod
    def processRequest(cls, ps, **kw):
        """invokes callback that should return a (request,response) tuple.
        representing the SOAP request and response respectively.
        ps -- ParsedSoap instance representing HTTP Body.
        request -- twisted.web.server.Request
        """
        resource = kw['resource']
        method = resource.getOperation(ps, None) # This getOperation method is valid for ServiceSOAPBinding subclass
        rsp = method(ps, **kw)[1] # return (request, response) but we only need response
        return rsp
    
class SOAPHandlerChainFactory(wsgi.SOAPHandlerChainFactory):
    protocol = ReverseHandlerChain

    @classmethod
    def newInstance(cls):
        return cls.protocol(DataHandler, SOAPCallbackHandler)

##################################################################################
## end Hacking
##################################################################################