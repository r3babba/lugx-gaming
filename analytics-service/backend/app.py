from flask import Flask, request, jsonify
from clickhouse_driver import Client
import os
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

client = Client(
    host='localhost',
    port=int(os.getenv('CLICKHOUSE_PORT', 9000)),
    user='default',
        password='newStrongPassword123'
)

# Create database and table on startup
def init_db():
    client.execute('CREATE DATABASE IF NOT EXISTS analytics')
    client.execute('''
        CREATE TABLE IF NOT EXISTS analytics.web_events (
            event_time DateTime,
            event_type String,
            page_url String,
            session_id String,
            scroll_depth UInt8,
            page_time Float32,
            session_time Float32
        ) ENGINE = MergeTree()
        ORDER BY event_time
    ''')

init_db()

# Create database and table on startup
def init_db():
    client.execute('CREATE DATABASE IF NOT EXISTS analytics')
    client.execute('''
        CREATE TABLE IF NOT EXISTS analytics.web_events (
            event_time DateTime,
            event_type String,
            page_url String,
            session_id String,
            scroll_depth UInt8,
            page_time Float32,
            session_time Float32
        ) ENGINE = MergeTree()
        ORDER BY event_time
    ''')

init_db()

@app.route('/event', methods=['POST'])
def receive_event():
    data = request.json
    
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    # Extract expected fields with default fallbacks
    event_time_str = data.get("event_time")
    event_type = data.get("event_type", "")
    page_url = data.get("page_url", "")
    session_id = data.get("session_id", "")
    scroll_depth = int(data.get("scroll_depth", 0))
    page_time = float(data.get("page_time", 0.0))
    session_time = float(data.get("session_time", 0.0))

    # Convert event_time string to datetime object
    if event_time_str:
        if event_time_str.endswith('Z'):
            event_time_str = event_time_str[:-1] + '+00:00' # Convert Z to a valid UTC offset
        try:
            event_time = datetime.fromisoformat(event_time_str)
        except ValueError:
            return jsonify({"error": "Invalid event_time format"}), 400
    else:
        event_time = datetime.now()

    local_client = Client(
        host='localhost',
        port=int(os.getenv('CLICKHOUSE_PORT', 9000)),
        user='default',
        password='newStrongPassword123'
    )
    local_client.execute('''
        INSERT INTO analytics.web_events 
        (event_time, event_type, page_url, session_id, scroll_depth, page_time, session_time) 
        VALUES
    ''', [(event_time, event_type, page_url, session_id, scroll_depth, page_time, session_time)])

    # Verify the connection is still active
    local_client.execute('SELECT 1')
    local_client.disconnect()

    return jsonify({"status": "ok"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)