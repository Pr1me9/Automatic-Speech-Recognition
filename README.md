# 🎙️ Automatic Speech Recognition (ASR) Project

This project implements a complete pipeline for a Automatic Speech Recognition (ASR) system, including data preprocessing, training simulation, evaluation using Word Error Rate (WER), text cleanup, and spell checking.

---

## 📌 Project Overview

The goal of this project is to build and analyze an ASR system using Hindi speech data. The pipeline covers:

- Data preprocessing from JSON transcripts  
- Dataset creation (audio-text pairs)  
- Training pipeline simulation  
- Evaluation using Word Error Rate (WER)  
- Text cleanup and normalization  
- Spell checking system  
- Lattice-based decoding (theoretical implementation)  

---

## 📁 Project Structure

Automatic-Speech-Recognition/
├── data/
│   ├── audio/
│   │   └── 825780.wav
│   └── text/
│       └── 825780.json
├── build_dataset.py
├── preprocess.py
├── train.py
├── evaluate.py
├── cleanup.py
├── spell_check.py
├── lattice.py
├── dataset.json
├── clean_dataset.json
├── requirements.txt
└── README.md

## ⚙️ Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/Pr1me9/Automatic-Speech-Recognition.git
cd Automatic-Speech-Recognition

2. Install dependencies:
pip install -r requirements.txt

3. Activate virtual environment (optional but recommended):
.venv\Scripts\activate   # Windows


🚀 How to Run
1. Preprocessing
python preprocess.py
2. Training (Simulated)
python train.py
3. Evaluation (WER)
python evaluate.py
4. Cleanup (Text Processing)
python cleanup.py
5. Spell Check
python spell_check.py
📊 Results
Word Error Rate (WER): 0.25

This indicates a 25% error rate, which is expected due to:

Limited dataset (single sample)
Use of synthetic/dummy audio
No full model fine-tuning

🔍 Key Features
Hindi text preprocessing and normalization
Audio-text dataset creation
ASR pipeline simulation
Evaluation using WER (jiwer library)
Rule-based spell checking
Text cleanup and normalization
Lattice-based decoding (conceptual)

⚠️ Limitations
Small dataset size
Dummy audio used instead of real speech
No actual deep learning model training
Limited evaluation scope

📚 Future Improvements
Use real Hindi speech datasets
Fine-tune Whisper or similar ASR models
Improve spell-checking using NLP models
Implement real lattice decoding
Expand dataset for better accuracy

🧠 Concepts Covered
Automatic Speech Recognition (ASR)
Word Error Rate (WER)
Text normalization
Data preprocessing
Error analysis
NLP basics
📌 Conclusion

This project demonstrates a complete ASR workflow from raw data preprocessing to evaluation and analysis. It provides a strong foundation for building real-world speech recognition systems.

👤 Author
Name: Abhinav Jha
Project: Automatic Speech Recognition
