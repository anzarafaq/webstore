from __future__ import unicode_literals

import json

from flask import Flask, flash, redirect, render_template, request, session, abort

from webstore.web_app.data_models.users import authenticate as pw_auth
from webstore.authenticate import authenticate_user
from webstore.logger import logging

logger = logging.getLogger(__name__)


def login(req):
    ## Reditrect to next_url after login, if so needed.
    next_url = req.values.get('next_url')
    return render_template('signin.j2', next_url=next_url)


def logout(req):
    #Destroy the session
    sid = req.cookies.get('session_id')
    if sid:
        session = session_store.get(sid)
        if 'user_id' in session: del (session['user_id'])
        session_store.save(session)
    ## Assuming, we get redirected to login, after logout
    return render_template('signin.j2')


@auth_check
def home(req):
    return render_template('home.j2')
