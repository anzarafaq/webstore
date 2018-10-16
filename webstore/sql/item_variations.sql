DROP TABLE IF EXISTS webstore.item_variations CASCADE;

CREATE TABLE webstore.item_variations (
    variation_id     int,
    item_id          int,
    created_at       TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at       TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT PK_Person PRIMARY KEY (variation_id, item_id)
);

