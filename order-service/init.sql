CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100),
    cart_items TEXT,
    total_price NUMERIC(10, 2)
);
