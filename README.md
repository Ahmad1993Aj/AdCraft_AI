# 🎵 Concert Hall Marketing Text Generator

**Concert Hall Marketing Text Generator** is a **Streamlit-based web application** that generates customized marketing texts for concert halls. The application uses the powerful OpenAI API to create creative and targeted content based on user inputs.

---

## 🚀 Features

- ✨ Generate marketing texts based on target audience, channel, and text length  
- � AI-powered text suggestions using OpenAI API  
- 🖥️ User-friendly interface with Streamlit  
- 📏 Adjustable text length for short or detailed content  
- 📦 Ready for containerization with Docker  

---

## 🛠️ Technologies Used

- **Python** – Main programming language  
- **Streamlit** – Web UI framework  
- **OpenAI API** – Text generation  
- **Docker** – Containerization and deployment  

---

## ✅ Requirements

- Python 3.10 or higher  
- Docker & Docker Compose  
- A valid OpenAI API key  

---

## ⚙️ Installation & Setup

### 🔹 1. Clone repository

```bash
git clone https://github.com/Ahmad1993Aj/AdCraft_AI.git
cd Concert-Hall-Marketing-Text-Generator
```
### 🔹 2. Configure API access
Create a file called credentials.py in the factory folder with the following content:
```bash
python
openapi_key = "DEIN_OPENAI_API_KEY"  # Ersetze dies mit deinem tatsächlichen API-Schlüssel
```
### 🔹 3. Install dependencies
```bash

pip install -r requirements.txt

```
### 🔹 4. Start application

```bash 

streamlit run main.py
```
###  🐳 Docker (Optional)
If you want to use Docker, you can start the application with the following command:
```bash
docker-compose up --build
```

### 📄 Lizenz
This project is licensed under the MIT License.

### 👨‍💻 Autor
Ahmad
GitHub: Ahmad1993Aj