DROP TABLE IF EXISTS webstore.variations CASCADE;

CREATE TABLE webstore.items (
    property         serial PRIMARY KEY,
    value            varchar(264),
    created_at       TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at       TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
);

