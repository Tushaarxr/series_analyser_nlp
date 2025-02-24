# Analyze Your Favourite Series with NLP  

## 🚀 Project Overview  
This project leverages Natural Language Processing (NLP) and Large Language Models (LLMs) to analyze your favorite series. We scrape our own dataset, classify text with zero-shot classifiers, build a custom LLM-based text classifier, create a character network using Named Entity Recognition (NER), and develop a chatbot to interact with your favorite characters. Finally, we integrate everything into a web-based GUI using Gradio.  

## 🏗️ Project Structure  
The project consists of five main modules:  

### 1️⃣ `crawler`  
- Scrapes the web to collect a dataset related to the series using Scrapy.  

### 2️⃣ `character_network`  
- Utilizes Spacy’s NER model to extract character names.  
- Constructs a relationship network using NetworkX and visualizes it with PyViz.  

### 3️⃣ `text_classifier`  
- Trains a classifier to categorize text into multiple predefined classes.  

### 4️⃣ `theme_classifier`  
- Extracts the main themes of the series using Zero-shot classification.  

### 5️⃣ `character_chat_bot`  
- Develops a chatbot using LLMs to interact with series characters.  

## 🖥️ Web Interface  
- The entire project is integrated into an interactive **Gradio** web GUI for user-friendly interaction.  

## 📌 Features  
✅ Web Scraping for dataset collection  
✅ Named Entity Recognition (NER) for character extraction  
✅ Character relationship network visualization  
✅ Zero-shot classification for theme extraction  
✅ Custom text classification model  
✅ AI-powered chatbot for character interaction  
✅ Web-based GUI with Gradio  
