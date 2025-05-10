
# CLEF2025 CheckThat - Task 4a 

## 🏁 Project Overview

This repository contains the full pipeline to tackle the CLEF2025 CheckThat Lab, focusing on Task 4:

* **4a:** Scientific Web Discourse Detection (multilabel classification)

We aim for a reproducible, well-documented workflow using **Google Colab**, **GitLab CI/CD**, **DVC**, and best NLP practices.

---

## 📂 Project Structure

```
/checkthat-clef2025/
├── data/                # Raw and processed data (tracked via DVC)
├── notebooks/           # Google Colab notebooks (.ipynb)
├── scripts/             # Reusable Python modules
├── models/              # Trained models and artifacts
├── results/             # Evaluation outputs, metrics, predictions
├── dvc.yaml             # DVC pipeline configuration
├── params.yaml          # Hyperparameters and configs
├── requirements.txt     # Python dependencies
└── README.md            # This documentation file
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```
git clone https://gitlab.com/your-username/checkthat-clef2025.git
cd checkthat-clef2025
```

### 2️⃣ Install dependencies (in Colab)

```python
!pip install -r requirements.txt
```

### 3️⃣ Initialize DVC and configure remote

```bash
dvc init
dvc remote add -d gdrive_remote gdrive://<your-folder-id>
dvc pull
```

### 4️⃣ Run notebooks (Google Colab)

* `notebooks/baseline_subtask4a.ipynb`
* `notebooks/baseline_subtask4b.ipynb`

---

## 🛠 Pipeline Components

✅ **Data Management**

* `.tsv` files loaded with `pandas`
* `.pkl` models loaded with `pickle`
* Tracked with DVC, not stored in Git

✅ **Model Training**

* Subtask 4a: multilabel classifiers (Logistic Regression, RandomForest, or BERT/DeBERTa when ready)
* Subtask 4b: BM25 retrieval + rerankers (sentence embeddings, cosine similarity)

✅ **Experiment Tracking**

* Optionally integrated with **MLflow** or **Weights & Biases**

✅ **Automation**

* `.gitlab-ci.yml` configured to trigger `dvc repro` pipelines on commits

✅ **Evaluation Metrics**

* 4a: Macro F1-score
* 4b: MRR\@5

---

## 📊 Submission & Reporting

For Codalab submission:

* Follow the format provided in `baselines.ipynb`
* Package predictions as required

For the system description paper:

* Document datasets, preprocessing, models, results, error analysis, and ablation studies
* Use the provided LaTeX template

---

## 📌 Notes

* This README will evolve as we integrate advanced models (Hugging Face Transformers, rerankers).
* DVC remote must be configured before pulling or pushing large files.
* Google Colab environment resets, so make sure to `git pull` and `dvc pull` before each session.

---

## 🔗 References

* CLEF2025 CheckThat: [https://checkthat.gitlab.io/clef2025/](https://checkthat.gitlab.io/clef2025/)
* GitLab Repo: [https://gitlab.com/checkthat\_lab/clef2025-checkthat-lab](https://gitlab.com/checkthat_lab/clef2025-checkthat-lab)
* Codalab: [https://codalab.lisn.upsaclay.fr/competitions/22359](https://codalab.lisn.upsaclay.fr/competitions/22359)







# CLEF2025 - Subtask4a: Scientific Web Discourse Detection

Este repositorio contiene los experimentos y resultados obtenidos en el reto CLEF2025 Subtask4a, orientado a la detección de discurso científico en Twitter.  
El objetivo principal es maximizar el macro-averaged F1-score en una tarea de clasificación multietiqueta.

## 📦 Estructura del repositorio

- `baselines.ipynb` → Notebook base entregado por los organizadores.
- `predictions.csv` → Archivo generado para enviar al leaderboard.
- `metrics.json` → Archivo con métricas en formato JSON.
- `metrics.csv` → Archivo con métricas en formato CSV.
- `README.md` → Este documento.

---

## 📈 Tabla de resultados por experimento

| Experimento             | Modelo Base                       | Macro F1 | Cat1 F1 | Cat2 F1 | Cat3 F1 | Umbral        | LR    | Épocas | Notas                       |
|-------------------------|-----------------------------------|----------|---------|---------|---------|--------------|-------|--------|-----------------------------|
| Baseline RoBERTa       | cardiffnlp/twitter-roberta-base-2022-154m |          |         |         |         | >0           | 2e-5  | 10     | Baseline original           |
| Fase 1 DeBERTa         | microsoft/deberta-v3-base         |          |         |         |         | >0           | 2e-5  | 10     | Cambio modelo base         |
| Fase 2 Threshold Tuning| microsoft/deberta-v3-base         |          |         |         |         | Optimizado   | 2e-5  | 10     | Ajuste de umbral           |
| Fase 3 Fine-tuning     | microsoft/deberta-v3-base         |          |         |         |         | Optimizado   | 3e-5  | 10     | Ajuste hiperparámetros     |
| Fase 4 Class Weights   | microsoft/deberta-v3-base         |          |         |         |         | Optimizado   | 3e-5  | 10     | Pesos clase minoritaria    |
| Fase 5 Augmentation    | microsoft/deberta-v3-base         |          |         |         |         | Optimizado   | 3e-5  | 10     | Back-translation           |
| Fase 6 Ensemble        | DeBERTa + RoBERTa ensemble       |          |         |         |         | Optimizado   | 3e-5  | 10     | Promedio de modelos        |

---

## 📋 Notas generales

- **Dataset:** 1229 tweets (train), 137 (dev), 240 (test)
- **Tarea:** Clasificación multietiqueta (cat1, cat2, cat3)
- **Métrica objetivo:** macro-averaged F1-score
- **Formato de entrega:** predictions.csv con columnas [index, cat1_pred, cat2_pred, cat3_pred]

---

## 🚀 Cómo ejecutar el pipeline

1. Entrenar modelo → se genera `predictions.csv`  
2. Calcular métricas → se generan `metrics.json` y `metrics.csv`  
3. Actualizar esta tabla con los resultados  
4. Subir `predictions.csv` al leaderboard  
5. Guardar resultados del leaderboard aquí

---

## ✅ Checklist de fases completadas

- [ ] Baseline RoBERTa
- [ ] Fase 1: DeBERTa
- [ ] Fase 2: Threshold Tuning
- [ ] Fase 3: Fine-tuning Hiperparámetros
- [ ] Fase 4: Class Weights
- [ ] Fase 5: Data Augmentation
- [ ] Fase 6: Ensemble Models

---

## 📌 Créditos

- Desarrollado por: [Tu Nombre o Equipo]  
- Para el reto CLEF2025 CheckThat Lab  
- Contacto: [tu-email@dominio.com]

