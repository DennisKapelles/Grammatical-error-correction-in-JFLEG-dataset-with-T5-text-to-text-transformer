
# 🧠 Grammatical Error Correction with T5 Transformers

This repository contains the code, methodology, and results for a Master's thesis project focused on **automated grammatical error correction (GEC)** using **pretrained T5 (Text-to-Text Transfer Transformer)** models. The goal of the project is to fine-tune a pretrained model on grammatically erroneous text data and assess its effectiveness in correcting spelling, punctuation, and grammatical errors.

## 📝 Thesis Title
**Error correction of texts using natural language embedding techniques**  
📍 *University of Patras – Department of Computer Engineering and Informatics*  
🎓 *Dionysios Kapelles, 2024*

---

## 📌 Abstract

This project explores the use of the T5 transformer model in the context of grammatical error correction (GEC). The methodology involves fine-tuning a pretrained T5 model on a curated dataset containing sentences with grammatical mistakes. The system is evaluated on multiple benchmarks, including metrics like **GLEU** and **ELERRANT**, showing promising results in terms of contextual understanding and correction precision. The research demonstrates the potential of transformer-based architectures to outperform traditional rule-based and statistical models in GEC tasks.

---

## 📂 Project Structure

```
📁 data/                  # Datasets used for training/evaluation (GEC datasets)
📁 notebooks/            # Jupyter notebooks for experimentation and visualization
📁 models/               # Pretrained and fine-tuned model checkpoints
📁 utils/                # Utility scripts (tokenization, data preprocessing, etc.)
📄 train.py              # Main training script
📄 evaluate.py           # Model evaluation script using GLEU and ELERRANT
📄 README.md             # Project documentation
```

---

## 🚀 Key Features

- Fine-tuning of the **T5-base** and **mT5** models for grammar correction.
- Application of the models to both **English and Greek datasets**.
- Comparative evaluation with traditional GEC approaches.
- Use of **context-aware corrections** leveraging transformer attention mechanisms.
- Example-based visualization of the model’s predictions.

---

## 📊 Evaluation Metrics

- **GLEU Score** – to evaluate fluency and correction accuracy.
- **ELERRANT** – a GEC-specific metric for syntactic and semantic correctness.
- **Loss** and **token-level accuracy** for training monitoring.

---

## 📎 Dependencies

- Python 3.8+
- PyTorch
- HuggingFace Transformers
- Scikit-learn
- SentencePiece
- ELERRANT / GLEU evaluation tools

---

## 📈 Sample Results

| Metric       | Value     |
|--------------|-----------|
| GLEU Score   | 84.3%     |
| ELERRANT     | 79.5%     |
| Accuracy     | 87.1%     |

*Results from the fine-tuned T5 model on a benchmark GEC dataset.*

---

## 📚 Future Work

- Expansion of training data with additional multilingual corpora.
- Deployment of a web-based demo for real-time grammar correction.
- Experimentation with larger T5 variants (T5-large, T5-3B).
- Integration with OCR pipelines for error correction in scanned documents.

---

## 🔖 Keywords

`Grammatical Error Correction`, `Natural Language Processing`, `T5`, `Transformer`, `Fine-tuning`, `Deep Learning`, `Context-aware models`, `GEC`, `ELERRANT`, `GLEU`

---

## 📬 Contact

**Author**: Dionysios Kapelles  
**Supervisor**: Dimitrios Koutsomitropoulos  
📧 kapelles[at]ceid.upatras.gr  
🏫 University of Patras, Greece
