DROP TABLE IF EXISTS webstore.items CASCADE;

CREATE TABLE webstore.items (
    item_id          serial PRIMARY KEY,
    title varchar(264),
    description      varchar(264),
    primary_image_url varchar(264),
    created_at       TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at       TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
);

