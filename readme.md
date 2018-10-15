Sample cart application.

Datastore
Identity/Session Management (Simplified)
CART
WebStore

Main idea is that:

- User logins in
- User searches for some items
- User add items to cart
- Cart lists the items
- User Performs a purchase
- User can list the purchases whenever he wants


SCHEMA:

Users 
Items
CART (1-many relation to Items, 1-1 relationship with user)
Purchases (1-many relation to Items, 1-1 relationship with user)

