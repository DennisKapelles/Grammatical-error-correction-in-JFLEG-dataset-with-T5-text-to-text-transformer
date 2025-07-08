# 🧠 Grammatical Error Correction with T5 and mT5 Transformers

This project presents a deep learning system for **automated grammatical error correction (GEC)** in English and Greek texts, developed using the **pretrained T5 (Text-to-Text Transfer Transformer)** and **mT5 (multilingual Text-to-Text Transfer Transformer)** models. It investigates the use of fine-tuning techniques on pre-trained language models to produce context-aware grammatical corrections for written language (spelling, punctuation, and grammatical errors).

## 📝 Thesis Title
**Error correction of texts using natural language embedding techniques**  
📍 *University of Patras – Department of Computer Engineering and Informatics*  
🎓 *Dionysios Kapelles, 2024*

---

## 📝 Publication

This work has been **submitted for presentation at COLING 2025** (International Conference on Computational Linguistics):

> **Title**: Finetuning LLMs for Grammatical Error Correction in English and Greek Texts

> **Authors**: *Dionysios Kapelles*

---

## 📌 Abstract

Grammatical Error Correction (GEC) involves the automatic correction of various types of grammatical errors, including spelling, punctuation and grammar. In order to convert an incorrect sentence to the correct version, a GEC system usually requires the input of the sentence itself. There are many approaches to grammatical error correction, ranging from rule-based models to neural machine translation. This thesis delves into the field of natural language processing by exploring the detailed setup of the T5-based Text-to-Text Transfer Transformer (T5) model for the specific task of grammatical correction. Accurate grammatical correction is paramount for effective communication, especially for non native speakers of a language. This research aims to harness the power of the productive capabilities of the T5 model and transfer learning to develop an efficient and flexible system for automated grammatical correction in written text. It involves the detail of a pre trained T5 model on a custom dataset containing sentences with varying degrees of grammatical errors. Data preprocessing involves encoding the sentences in the T5 format, allowing it to generate corrected sentences for input with grammatical errors. The results show the effectiveness of the improved T5 model in grammatical correction. The model achieves competitive performance on benchmarking metrics, outperforming existing methods in terms of accuracy and contextual understanding. The findings highlight the importance of using pre-trained models and detail techniques to develop sophisticated grammar correction systems. In conclusion, this study highlights the ability of an improved T5 model in addressing the challenges of grammar correction. The insights gained pave the way for future research to improve architectural models and expand the scope of automated language correction applications.

---

## 🧠 Models

- **T5-base**: Fine-tuned on the English JFLEG dataset for high-accuracy grammatical correction.
- **mT5-base**: Adapted and fine-tuned for Greek grammar correction using custom parallel datasets.

---

## 🧪 Datasets

- **English**: [JFLEG Corpus](https://huggingface.co/datasets/jhu-clsp/jfleg)
- **Greek**: Custom-crafted datasets with realistic grammatical errors (e.g., accent errors, dropped final "n", etc.).

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

## 🛠️ Technologies Used

- Python 3.8+
- PyTorch
- HuggingFace Transformers
- Happy Transformer
- Scikit-learn
- SentencePiece
- ELERRANT / GLEU evaluation tools
- Google Colab (GPU-enabled)
- T5 / mT5 models

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
