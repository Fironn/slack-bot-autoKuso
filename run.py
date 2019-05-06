# -*- coding: utf-8 -*-
import json
import webapp2

class EchoHandler(webapp2.RequestHandler):
    VERIFICATION_TOKEN = 'xoxp-460747175155-460238652017-625527914960-2fd8a0980cd6bbfefae50cc6c551867d'

    def post(self):
        body = json.loads(self.request.body)
        if body['token'] != self.VERIFICATION_TOKEN:
            self.response.headers['Content-Type'] = 'text/plain'
            self.status = 403
            self.response.write('403 Forbidden')
            return
        if body['type'] == 'url_verification':
            self.verify_url(body)

    def verify_url(self, params):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(params['challenge'])

app = webapp2.WSGIApplication([
    ('/echo-bot-hook', EchoHandler)
], debug=True)