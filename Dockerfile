# Verwende eine spezifische Python-Version für Reproduzierbarkeit
FROM python:3.10-slim

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Systempakete installieren
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Kopiere die requirements-Datei und installiere Python-Abhängigkeiten
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den restlichen Code in den Container
COPY . .

# Exponiere den Port, auf dem die App läuft
EXPOSE 5000

# Starte die Streamlit-Anwendung
CMD ["streamlit", "run", "main.py", "--server.port=5000", "--server.address=0.0.0.0"]