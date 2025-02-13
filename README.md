# ⚙️ Configuration File Manager API

## 📌 Project Description
This is a **Flask-based API** that reads a configuration file (`config.ini`), stores it in an **SQLite database**, and serves it via an API endpoint. It allows users to fetch the stored configuration details in JSON format.

## 📚 Table of Contents
1. [⚙️ Prerequisites](#prerequisites)
2. [📅 Installation Instructions](#installation-instructions)
3. [🖊 Usage Instructions](#usage-instructions)
4. [🔧 Configuration](#configuration)
5. [🚀 CI/CD Pipeline Details](#cicd-pipeline-details)
6. [🔒 Security Best Practices](#security-best-practices)
7. [🐞 Troubleshooting](#troubleshooting)
8. [🤝 Contribution Guidelines](#contribution-guidelines)
9. [📜 License](#license)
10. [📸 Screenshots & Architecture Diagrams](#screenshots--architecture-diagrams)
11. [📅 Changelog](#changelog)

## ⚙️ Prerequisites
- 🐳 Python 3.x installed
- 📦 Required Python libraries:
  ```bash
  pip install flask configparser sqlite3
  ```

## 📅 Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/config-manager-api.git
   ```
2. Navigate to the project directory:
   ```bash
   cd config-manager-api
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🖊 Usage Instructions
1. Place your `config.ini` file inside the project directory.
2. Run the script:
   ```bash
   python app.py
   ```
3. Access the API via:
   ```bash
   http://127.0.0.1:5000/config
   ```
   This will return the stored configuration as a JSON response.

## 🔧 Configuration
Your `config.ini` file should have the following structure:
```ini
[Database]
host = localhost
port = 3306
username = admin
password = secret

[Server]
address = 192.168.0.1
port = 8080
```

## 🚀 CI/CD Pipeline Details
- Automate testing using **GitHub Actions**.
- Deploy the API using **Docker** for easy containerization.

## 🔒 Security Best Practices
- **Do not store sensitive data (like passwords) in plaintext!**
- Use **environment variables** instead of hardcoding credentials.

## 🐞 Troubleshooting
- If Flask is not installed, run:
  ```bash
  pip install flask
  ```
- If the API doesn’t start, check for **port conflicts**.

## 🤝 Contribution Guidelines
- 🔄 Fork the repository.
- 🚀 Submit a pull request with your changes.

## 📜 License
This project is licensed under the MIT License.

## 📸 Screenshots & Architecture Diagrams
![API Workflow](screenshot.png)

## 📅 Changelog
- **v1.0** - Initial release with configuration parsing & API.

---
🚀 **Happy Coding!** 💻

