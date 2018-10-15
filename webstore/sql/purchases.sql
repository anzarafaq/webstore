DROP TABLE IF EXISTS webstore.purchases CASCADE;

CREATE TABLE webstore.purchases (
    purchase_id      serial PRIMARY KEY,
    user_id          integer REFERENCES webstore.users (user_id),
    created_at       TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at       TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    item_id          integer REFERENCES webstore.items (item_id)  
);
