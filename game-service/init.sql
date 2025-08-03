CREATE TABLE IF NOT EXISTS games (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    release_date DATE NOT NULL,
    price NUMERIC NOT NULL
);
