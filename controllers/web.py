#! /usr/bin/env python3
# coding: utf-8
"""
Jean-Pierre [Prototype]
A Raspberry Pi robot helping people to build groceries list.
Matteo Cargnelutti - github.com/matteocargnelutti

controllers/web.py - Web server : uses Flask
"""
#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------
import os
import random
import string

from flask import Flask

from utils import Database
import models

#-----------------------------------------------------------------------------
# Controller
#-----------------------------------------------------------------------------
class Web:

    @classmethod
    def secret_key(cls):
        """
        Creates / Return a secret key, stored in a file
        :rtype: str
        """
        filename = 'flask_secret_key'
        # Is there a secret key ?
        if os.path.isfile(filename):
            file = open(filename, 'r')
            secret_key = file.read()
            file.close()
            return secret_key

        # If there's none : generate a new one
        newkey = "".join([random.choice(string.printable) for _ in range(24)])
        keyfile = open(filename, 'w')
        keyfile.write(newkey)
        keyfile.close()
        return newkey

#-----------------------------------------------------------------------------
# Flask WSGI init and views
#-----------------------------------------------------------------------------
if __name__ != '__main__':

    # Flask init
    webapp = Flask(__name__)
    webapp.config['SECRET_KEY'] = Web.secret_key()

    @webapp.route("/")
    def hello():
        return flask.render_template('index.html')
