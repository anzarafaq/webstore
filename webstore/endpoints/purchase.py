from __future__ import unicode_literals

import json

from flask import Flask, flash, redirect, render_template, request, session, abort

from webstore.data_models.users import auth_check
from webstore.data_models.users import get_cart_items, add_to_cart, remove_from_cart
from webstore.logger import logging

logger = logging.getLogger(__name__)


## auth_check makes sure user is logged in to see the cart
@auth_check
def purchase(req):
    ## Items in the cart
    cart_items=[]

    ## If there is a valid user session
    sid = req.cookies.get('session_id')
    if sid:
        session = session_store.get(sid)
        if 'user_id' in session:
    		cart_items=get_cart_items(user_id)

    ## Check inventory for each item
    for item in cart_items:
        check_inventory(item)

    # Determine cart total, $$ value plus tax, shipping etc.
    get_cart_total(cart_items)

    # send to payments.
    return render_template('payments.j2', cart_items=cart_items, cart_total=cart_total)
