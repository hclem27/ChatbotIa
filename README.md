🦙 Flask + Ollama Chat API
Cette application est une API REST simple basée sur Flask qui expose un endpoint /chat permettant d’envoyer un message utilisateur et de recevoir une réponse générée par le modèle Ollama (ex. llama3).

🚀 Fonctionnalités
✅ Endpoint /chat en POST pour envoyer un message utilisateur.
✅ Communication avec Ollama pour générer une réponse.
✅ Réponse renvoyée au format JSON.
✅ Gestion des erreurs si aucun message n’est fourni.
✅ CORS activé (permet d’appeler l’API depuis un frontend, ex. React ou Vue).

📦 Installation
Cloner le projet
git clone https://github.com/ton-repo/flask-ollama-chat.git
cd flask-ollama-chat
Créer un environnement virtuel (optionnel mais recommandé)
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
Installer les dépendances
pip install -r requirements.txt

⚙️ Prérequis
Python 3.8+
Ollama doit être installé et fonctionnel sur la machine.
👉 Installation d’Ollama
▶️ Lancer l’API
python app.py
L’API sera disponible à l’adresse :
👉 http://localhost:5000/chat

📡 Exemple d’appel API
Requête
curl -X POST http://localhost:5000/chat \
     -H "Content-Type: application/json" \
     -d '{"content": "Bonjour, comment ça va ?"}'
Réponse
{
  "message": {
    "content": "Bonjour ! Je vais très bien, merci. Et vous ?"
  }
}
🛠️ Technologies utilisées
Flask
Flask-CORS
Ollama

📌 Notes
Par défaut, l’API écoute sur 0.0.0.0:5000.
Le modèle par défaut est llama3, mais tu peux le modifier dans le code :
response = ollama.chat(model='llama3', messages=[ ... ])
Idéal pour brancher un frontend (React, Vue, etc.) ou tester avec Postman / curl.
