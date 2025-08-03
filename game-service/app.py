from flask import Flask, request, jsonify
import psycopg2
import json

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host='postgres-game',
        database='games',
        user='postgres',
        password='postgres'
    )
    return conn

@app.route('/games', methods=['POST'])
def add_game():
    data = request.get_json()
    name = data['name']
    category = data['category']
    release_date = data['release_date']
    price = data['price']

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO games (name, category, release_date, price) VALUES (%s, %s, %s, %s)",
        (name, category, release_date, price)
    )
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({'message': 'Game added'}), 201

@app.route('/games', methods=['GET'])
def get_games():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM games')
    games = cur.fetchall()
    cur.close()
    conn.close()

    results = []
    for game in games:
        results.append({
            'id': game[0],
            'name': game[1],
            'category': game[2],
            'release_date': game[3].strftime('%Y-%m-%d'),
            'price': float(game[4])
        })
    return jsonify(results)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
