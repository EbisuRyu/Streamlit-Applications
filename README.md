# Streamlit Applications

This repository contains three Streamlit applications developed as part of the AIO course.

## Clone the Repository

```bash
git clone https://github.com/EbisuRyu/Streamlit-Applications.git
cd Streamlit-Applications
```

## Projects

1. **Word Correction**
   - A Streamlit application that uses Levenshtein distance to correct misspelled words.
   - Streamlit App: [Word Correction](https://ebisuryu-word-correction.streamlit.app/)
   - [Word-Correction/README.md](/Word-Correction/README.md)

2. **Object Detection**
   - A Streamlit application for detecting objects in images using a pre-trained MobileNetSSD model.
   - Streamlit App: [Object Detection](https://ebisuryu-object-detection.streamlit.app/)
   - [Object-Detection/README.md](/Object-Detection/README.md)

3. **Chatbot**
   - A Streamlit application that implements a simple chatbot using Hugging Face's HugChat.
   - Streamlit App: [Chatbot](https://ebisuryu-chatbot.streamlit.app/)
   - [Chatbot/README.md](/Chatbot/README.md)

## Install the Required Dependencies
```bash
pip install -r requirements.txt
```

## Starting the Application

#### Word Correction

Navigate to the `Word-Correction` directory and run:
```bash
cd Word-Correction
streamlit run levenshtein_distance.py
```
#### Object Detection

Navigate to the `Object-Detection` directory and run:
```bash
cd Object-Detection
streamlit run object_detection.py
```

#### Chatbot
Navigate to the `Chatbot` directory and run:
```bash
cd Chatbot
streamlit run chatbot.py
```

## Contributing
Feel free to contribute to this repository by opening issues or submitting pull requests.