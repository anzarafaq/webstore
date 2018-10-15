DROP TABLE IF EXISTS webstore.users CASCADE;

CREATE TABLE webstore.users (
    user_id          serial PRIMARY KEY,
    created_at       TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at       TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    screen_name      varchar(64),  
    email            varchar(64),
    passwd           varchar(256),
);
