#-*- coding:utf-8 -*-
import os
import sae
import web
from hello import hello 
from wsucai import wsgi

urls = ("/","hello",
        )


application = sae.create_wsgi_app(wsgi.application)