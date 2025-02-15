# ⚙️ Configuration File Manager API

## 📌 Project Description
This is a **Flask-based API** that reads a configuration file (`config.ini`), stores it in an **SQLite database**, and serves it via an API endpoint. It allows users to fetch the stored configuration details in JSON format.

## 📚 Table of Contents
1. [⚙️ Prerequisites](https://github.com/Jidendiran-coder/Config_File_Manager_Python#%EF%B8%8F-prerequisites)
2. [📅 Installation Instructions](https://github.com/Jidendiran-coder/Config_File_Manager_Python#-installation-instructions)
3. [🖊 Usage Instructions](https://github.com/Jidendiran-coder/Config_File_Manager_Python#-usage-instructions)
4. [🔧 Configuration](https://github.com/Jidendiran-coder/Config_File_Manager_Python#-configuration)
5. [🚀 CI/CD Pipeline Details](https://github.com/Jidendiran-coder/Config_File_Manager_Python#-cicd-pipeline-details)
6. [🔒 Security Best Practices](https://github.com/Jidendiran-coder/Config_File_Manager_Python#-security-best-practices)
7. [🐞 Troubleshooting](https://github.com/Jidendiran-coder/Config_File_Manager_Python#-troubleshooting)
8. [🤝 Contribution Guidelines](https://github.com/Jidendiran-coder/Config_File_Manager_Python#-contribution-guidelines)
9. [📜 License](https://github.com/Jidendiran-coder/Config_File_Manager_Python#-license)
10. [📸 Screenshots & Architecture Diagrams](https://github.com/Jidendiran-coder/Config_File_Manager_Python#-screenshots--architecture-diagrams)
11. [📅 Changelog](https://github.com/Jidendiran-coder/Config_File_Manager_Python#-changelog)

## ⚙️ Prerequisites
- 🐳 Python 3.x installed
- 📦 Required Python libraries:
  ```bash
  pip install flask configparser sqlite3
  ```

## 📅 Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/Jidendiran-coder/Config_File_Manager_Python.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Config_File_Manager_Python
   ```

## 🖊 Usage Instructions
1. With the `config.ini` file inside the project directory.
2. Run the script:
   ```bash
   python Config_file_Manager.py
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
- ⭐ Star the repository.
- 🔄 Fork the repository.
- 🚀 Submit a pull request with your changes.

## 📜 License
This project is licensed under the MIT License.

## 📸 Screenshots
![image](https://github.com/user-attachments/assets/0c3c5f5c-584d-4a01-b2f5-6daf3ad50607)
From Browser

![image](https://github.com/user-attachments/assets/0d1a931e-412d-4aca-ae31-dbcc769189e3)

## 📅 Changelog
- **v1.0** - Initial release with configuration parsing & API.

---
🚀 **Happy Coding!** 💻

