from __future__ import unicode_literals

import json

from flask import Flask, flash, redirect, render_template, request, session, abort

from webstore.data_models.users import auth_check
from webstore.data_models.purchase_history import get_purchased_items, add_to_purchased_items
from webstore.logger import logging

logger = logging.getLogger(__name__)


## auth_check makes sure user is logged in to see the purchase history
@auth_check
def history(req):
    ## Items in the cart
    purchased_items=[]

    ## If there is a valid user session
    sid = req.cookies.get('session_id')
    if sid:
        session = session_store.get(sid)
        if 'user_id' in session:
    		purchased_items=get_purchased_items(user_id)
    return render_template('purchase_history.j2', purchased_items=purchased_items)
