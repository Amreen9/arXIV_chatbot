ArXiv Document Retrieval + Chatbot

This is a web-based document retrieval and chatbot application designed to search, retrieve, and interact with academic research papers from ArXiv. 
The application leverages Flask for the backend and PyQt5 for a desktop UI, enabling seamless document search, retrieval, and conversational interaction with a chatbot powered by Google's Generative AI.

Features:
 
 Document Search: Search for academic papers on ArXiv and retrieve details such as the title, authors, abstract, and PDF links.
 
 Search Result Ranking: Papers are ranked by relevance, considering factors like content similarity, and temporal relevance.
 
 Chatbot Interaction: A chatbot that can answer questions based on the full text of retrieved research papers. It uses Google’s Gemini API to provide intelligent responses.
 
 Desktop UI: A PyQt5-based desktop application that integrates with the Flask app to display the web interface locally in a desktop window.

Components:

1.NIC6.py (Flask Backend):
 -Handles the Flask server and routes for document search and chatbot interaction.
 -Integrates with the ArXiv API for document retrieval and ranks the results using a custom LLM agent.
 -Executes the UI application via a subprocess.

2.NIC_UI.py (Desktop UI):
 -Creates a PyQt5-based UI to load the Flask web app in a local desktop window using QWebEngineView.
 -Runs Flask in a separate thread to handle the backend while keeping the UI responsive.

3.arxiv_client.py:
 -Provides functionality to query ArXiv for papers based on a user-defined query.
 -Downloads and extracts the full text from the resulting PDFs.

4.llm.py:
 -A custom agent that improves the search results using advanced techniques.
 -Query expansion (via synonyms).
 -Document Length Normalization
 -TF-IDF Vectorization
 -Sentence Embeddings
 -Semantic Search
 -Temporal Relevance.

5.chatbot.py:Implements a chatbot powered by Google's Generative AI API (Gemini) to answer user questions based on the content of the retrieved research papers.

6.index.html, results.html: HTML pages for displaying the search form and results.

7.styles.css: Styling for the web interface.

8.script.js: JavaScript for handling form submission and chatbot interactions.

Requirements:

Backend:
Flask, PyQt5, PyQtWebEngine, arxiv, requests, PyPDF2, scikit-learn, sentence-transformers, nltk, numpy. google-generativeai

Desktop UI:
PyQt5

Installation:

Clone the repository.

Install the required Python dependencies:
pip install -r requirements.txt

Install PyQt5 for the desktop UI:
pip install PyQt5

Download and install the necessary spaCy model:
python -m spacy download en_core_web_sm

Set up the environment variable for the Google Generative AI API:
export api_key="YOUR_GOOGLE_API_KEY"

Running the Application:

Backend:
Run the Flask server via the Python script:
python NIC6.py

The Flask app will be accessible at http://127.0.0.1:5000/ for search and chatbot interactions.

Desktop UI:
To launch the desktop UI:

python NIC_UI.py
The desktop application will open, displaying the web interface locally.

Search and Chatbot:

1.Use the search form to find academic papers from ArXiv.

2.The results will be displayed with a "Download PDF" link.

3.A chatbot can be activated by clicking the "Chatbot" button, allowing users to interact with the chatbot based on the content of the retrieved documents.

