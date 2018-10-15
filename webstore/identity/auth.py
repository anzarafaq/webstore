from __future__ import unicode_literals

import json

from werkzeug.utils import redirect
from werkzeug import Request, Response 
from werkzeug.contrib.sessions import FilesystemSessionStore

from webstore.datastore.users import authenticate as pw_auth
from webstore.render import render

from webstore.logger import logging
logger = logging.getLogger(__name__)

session_store = FilesystemSessionStore('/tmp/sessions')


def auth_check(f):
    '''
    Decorator to do basic auethentication checks.
    It also attaches the session to the request
    so that the endpoint methods will have access
    to the session.
    If session is not valid, user gets redirected to login.
    '''

    def wrapped(*args, **kwds):
        sid = req.cookies.get('session_id')
        if sid is None:
            return redirect('/login?next_url=%s' % next_url)
        else:
            session = session_store.get(sid)
            if session is None:
                return redirect('/login?next_url=%s' % next_url)
            if 'user_id' not in session:
                return redirect('/login?next_url=%s' % next_url)
            req.session = session
            # Any additional information can go into session here.

        return f(*args, **kwds)

    return wrapped


def login(req):
    next_url = req.values.get('next_url')
    return Response(render('ng/signin.j2',
                           next_url=next_url,
                           login_form=True,
                           show_search=True),
                    mimetype='text/html')


def logout(req):
    next_url = req.values.get('next_url')
    sid = req.cookies.get('session_id')
    if sid:
        session = session_store.get(sid)
        if 'user_id' in session: del (session['user_id'])
        session_store.save(session)
    return Response(render('ng/signin.j2', next_url="/", login_form=True), mimetype='text/html')
