'''
MIT License

Copyright (c) 2025 [Jidendiran]

Permission is hereby granted, free of charge, to any person obtaining a copy 
of this software and associated documentation files (the Software), to deal 
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import configparser  # 📄 Library for reading INI configuration files
import json  # 📜 Library to handle JSON data
import sqlite3  # 🗄️ Library for database operations
from flask import Flask, jsonify  # 🌐 Flask framework for creating a REST API

# 🚀 Initialize Flask application
app = Flask(__name__)

# 📌 Function to read the configuration file and convert it into a dictionary
def read_config(file_path):
    """
    Reads an INI configuration file and returns its contents as a dictionary.

    Args:
        file_path (str): Path to the configuration file.

    Returns:
        dict: Parsed configuration data.
    """
    config = configparser.ConfigParser()  # 🛠️ Create a config parser object
    try:
        config.read(file_path)  # 📖 Read the file
        config_data = {}  # 📂 Dictionary to store configuration values
        
        # 🔄 Loop through each section in the config file
        for section in config.sections():
            config_data[section] = {key: value for key, value in config.items(section)}
        
        return config_data  # 🔙 Return the extracted data
    except Exception as e:
        print(f"❌ Error reading configuration file: {e}")
        return None

# 📌 Function to save extracted configuration data to an SQLite database
def save_to_database(data):
    """
    Saves the extracted configuration data into an SQLite database.

    Args:
        data (dict): The configuration data to be stored.
    """
    conn = sqlite3.connect("config.db")  # 🗄️ Connect to SQLite database
    cursor = conn.cursor()  # 🎯 Create a cursor object for executing SQL commands
    
    # 📋 Create table if it does not exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS config_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            json_data TEXT
        )
    """)
    print("✅ Table `config_data` has been created successfully.")

    # 📤 Insert JSON data into the database
    cursor.execute("INSERT INTO config_data (json_data) VALUES (?)", (json.dumps(data),))
    conn.commit()  # 💾 Save changes
    conn.close()  # 🔚 Close database connection

# 📌 Function to fetch the latest configuration data from the database
def fetch_from_database():
    """
    Retrieves the most recent configuration entry from the database.

    Returns:
        dict: The stored configuration data.
    """
    conn = sqlite3.connect("config.db")  # 🗄️ Connect to database
    cursor = conn.cursor()
    
    # 🔎 Retrieve the most recent entry
    cursor.execute("SELECT json_data FROM config_data ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()  # 📤 Fetch the result
    conn.close()  # 🔚 Close the connection
    
    return json.loads(row[0]) if row else {}  # 🔄 Convert JSON string back to dictionary

# 🌍 API Endpoint to get stored configuration data
@app.route("/config", methods=["GET"])
def get_config():
    """
    Flask API endpoint to retrieve stored configuration data.

    Returns:
        JSON response with the configuration data.
    """
    data = fetch_from_database()  # 🔄 Get data from database
    return jsonify(data)  # 📤 Return data as JSON response

# 🏁 Main function to execute the script
if __name__ == "__main__":
    """
    The main execution block of the script.

    - Reads configuration data from `config.ini`
    - Saves it to an SQLite database
    - Fetches and verifies the stored data
    - Starts the Flask web server
    """
    config_data = read_config("config.ini")  # 📖 Read configuration file
    
    if config_data:
        print("📂 Configuration File Parser Results:")
        
        # 🔍 Print extracted configuration data
        for section, values in config_data.items():
            print(f"📌 {section}:")
            for key, value in values.items():
                print(f"  - {key}: {value}")
        
        # 💾 Save extracted data into database
        save_to_database(config_data)
    
    # 🔄 Fetch data once to verify if it's stored correctly
    stored_data = fetch_from_database()
    if not stored_data:
        print("❌ No data found in database! Ensure the configuration is inserted before fetching.")

    # 🚀 Start Flask application
    app.run(debug=True)
