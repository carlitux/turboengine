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

__all__ = ['generate_urls', 'cached_urls']

def _import_mapping(name):
    m = __import__(name)
    for n in name.split(".")[1:]:
        m = getattr(m, n)
    return m

def _generate_absolute_paths(parent, app):
    mapping = _import_mapping('%s.mapping'%(app)) # import mapping module
    paths = []
    if hasattr(mapping, 'map'):
        for path, handler in mapping.map:
            paths.append(('%s%s'%(parent, path), handler))
    return paths

def generate_urls(iterable):    
    mapped = []
    for parent, app in iterable:
        mapped.extend(_generate_absolute_paths(parent, app))
        
    return mapped