from urllib2 import urlopen, build_opener, HTTPError
from urllib import urlencode
from simplejson import loads, dumps
import os

DEFAULT_URL = os.getenv(
    "RPC_BASE_URL",
    "http://127.0.0.1:8080"
)

class Connection(object):
  def __init__(self, ns, base_url = DEFAULT_URL, auth=None):
    self.base_url = base_url
    self.ns = ns
    self.auth = auth

  def get(self, url, args):
    for key, val in args.items():
      if not isinstance(val, basestring):
        args[key] = dumps(val)

    data = urlencode(args)

    opener = build_opener(URLopener)

    authcookie = ("auth=%s" % self.auth) if self.auth else ""
    opener.addheaders = ("Cookie", authcookie),

    try:
      f = urlopen(url, data)
      data = f.read()
      f.close()
    except HTTPError, e:
      data = None
      f = e.fp
      if e.code == 500:
        print 'Server Error'
      if e.code == 404:
        raise AttributeError
      else:
        raise

    return data

  def call(self, func, **kw):

    url = "%s/api/v1/%s/%s" % (self.base_url, self.ns, func)
    ret = self.get(url, kw)

    try:
      return loads(ret)
    except:
      raise ValueError("Nonjson answer to %s: %s" % (func, ret))

  def __getattr__(self, name):
    if name in ['trait_names', '_getAttributeNames', 'sid']:
      raise AttributeError()

    name = name.replace("_", ".")

    def call(**kw):
      return self.call(name, **kw)

    return call
