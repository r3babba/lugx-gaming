from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST", "postgres-order")
DB_NAME = os.environ.get("DB_NAME", "ordersdb")
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "password")

conn = psycopg2.connect(
    host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD
)
conn.autocommit = True

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    customer_name = data.get('customer_name')
    cart_items = data.get('cart_items', [])
    total_price = data.get('total_price')

    items_str = ",".join(cart_items)

    cur = conn.cursor()
    cur.execute(
        "INSERT INTO orders (customer_name, cart_items, total_price) VALUES (%s, %s, %s)",
        (customer_name, items_str, total_price)
    )
    cur.close()

    return jsonify({"message": "Order created"}), 201

@app.route('/orders', methods=['GET'])
def get_orders():
    cur = conn.cursor()
    cur.execute("SELECT id, customer_name, cart_items, total_price FROM orders")
    rows = cur.fetchall()
    cur.close()

    orders = []
    for row in rows:
        orders.append({
            "id": row[0],
            "customer_name": row[1],
            "cart_items": row[2].split(",") if row[2] else [],
            "total_price": float(row[3])
        })

    return jsonify(orders)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
