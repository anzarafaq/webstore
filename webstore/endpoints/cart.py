from __future__ import unicode_literals

import json

from flask import Flask, flash, redirect, render_template, request, session, abort

from webstore.data_models.users import auth_check
from webstore.data_models.users import get_cart_items, add_to_cart, remove_from_cart
from webstore.logger import logging

logger = logging.getLogger(__name__)


## auth_check makes sure user is logged in to see the cart
@auth_check
def cart(req):
    ## Items in the cart
    cart_items=[]

    ## If there is a valid user session
    sid = req.cookies.get('session_id')
    if sid:
        session = session_store.get(sid)
        if 'user_id' in session:
    		cart_items=get_cart_items(user_id)
    return render_template('cart.j2', cart_items=cart_items)


@auth_check
def add(req):
    item=get_item(req.item_id)
    sid = req.cookies.get('session_id')
    if sid:
        session = session_store.get(sid)
        if 'user_id' in session:
                user_id = session['user_id']
		add_to_cart(user_id, item)
		## Rerturn the cart
		cart_items=get_cart_items(user_id)
    return render_template('cart.j2', cart_items=cart_items)


@auth_check
def remove(req):
    item=get_item(req.item_id)
    sid = req.cookies.get('session_id')
    if sid:
        session = session_store.get(sid)
        if 'user_id' in session:
                user_id = session['user_id']
		remove_from_cart(item_id, user_id)
		## Rerturn the cart
		cart_items=get_cart_items(user_id)
    return render_template('cart.j2', cart_items=cart_items)
