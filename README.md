
# CLEF2025 CheckThat - Subtask4a: 

## 🏁 Project Overview

This repository contains the full pipeline the CLEF2025 CheckThat Lab, focusing on Task 4:

* **4a:** Scientific Web Discourse Detection (multilabel classification)

Este repositorio contiene los experimentos y resultados obtenidos en el reto CLEF2025 Subtask4a, orientado a la detección de discurso científico en Twitter.  
El objetivo principal es maximizar el macro-averaged F1-score en una tarea de clasificación multietiqueta.

---

## 📌 Objective

This notebook and codebase describe the **experimental approach** taken to develop a multi-label classification system for identifying scientific discourse in Twitter data. The model is built on top of `microsoft/deberta-v3-base` and optimized through a multi-phase strategy aimed at maximizing macro-averaged F1.

---

## 📋 Notas generales

- **Dataset:** 1229 tweets (train), 137 (dev), 240 (test)
- **Tarea:** Clasificación multietiqueta (cat1, cat2, cat3)
- **Métrica objetivo:** macro-averaged F1-score
- **Formato de entrega:** predictions.csv con columnas [index, cat1_pred, cat2_pred, cat3_pred]

---
## 🔬 Dataset

- `ct_train.tsv` – training set
- `ct_test.tsv` – test set for leaderboard submission
- Format: each tweet labeled across three binary categories (`cat1`, `cat2`, `cat3`)

---

## 🚀 How to Reproduce (in Colab)

1. Open [`clef2025_pipeline.ipynb`](notebooks/clef2025_pipeline.ipynb) in Google Colab.
2. Clone the official CLEF2025 CheckThat repository and extract the folder `task4/subtask_4a`.
3. Copy `ct_train.tsv` and `ct_test.tsv` into the `/data/` folder inside your working directory.
4. Execute the notebook sequentially through all six phases:
   - Baseline → Threshold Tuning → Fine-Tuning → Class Weights → Ensemble → Final Prediction.
5. The output file `predictions.csv` will be saved under `/predictions/` and is ready to be submitted to the leaderboard.

---

## 📂 Project Structure

```
clef2025_task4a/
├── data/
│ ├── ct_train.tsv
│ ├── ct_test.tsv
│ └── thresholds.json
├── models/
│ └── final_model/
├── predictions/
│ └── predictions.csv
├── notebooks/
│ └── clef2025_pipeline.ipynb
```
---

## ⚙️ Phases Overview

| Phase | Description                          | Output                        |
|-------|--------------------------------------|-------------------------------|
| 1     | Baseline training (DeBERTa-v3-base)  | `cv_preds`                    |
| 2     | Threshold tuning (PR curve)          | `thresholds.json`             |
| 3     | Fine-tuning (lr, epochs search)      | `best_macro_f1`, config       |
| 4     | Training with class weights          | `macro_f1_class_weights`      |
| 5     | Ensemble of models (soft voting)     | `macro_f1_ensemble`           |
| 6     | Final training + test prediction     | `predictions.csv`             |

---

## 🧪 Results Summary

| Model           | Macro F1 | Cat1 F1 | Cat2 F1 | Cat3 F1 | Notes                          |
|------------------|----------|---------|---------|---------|--------------------------------|
| Baseline         | 0.8021   | 0.79xx  | 0.76xx  | 0.83xx  | lr=2e-5, 10 epochs              |
| Fine-tuned       | 0.8143   | 0.81xx  | 0.78xx  | 0.84xx  | lr=2e-5, 12 epochs              |
| Class Weights    | 0.8195   | 0.82xx  | 0.79xx  | 0.85xx  | weights applied per class      |
| **Ensemble**     | **0.8274** | 0.83xx  | 0.80xx  | 0.85xx  | Averaged predictions (FT + CW) |

> Thresholds tuned per class via `precision_recall_curve` to optimize F1 individually.

---

## 💡 Thresholds Used

```json
{
  "cat1": 0.4607,
  "cat2": 0.6438,
  "cat3": 0.7325
}

---

## 🔗 References

* CLEF2025 CheckThat: [https://checkthat.gitlab.io/clef2025/](https://checkthat.gitlab.io/clef2025/)
* GitLab Repo: [https://gitlab.com/checkthat\_lab/clef2025-checkthat-lab](https://gitlab.com/checkthat_lab/clef2025-checkthat-lab)
* Codalab: [https://codalab.lisn.upsaclay.fr/competitions/22359](https://codalab.lisn.upsaclay.fr/competitions/22359)

---
## 📌 Créditos

- Desarrollado por: [Tu Nombre o Equipo]  
- Para el reto CLEF2025 CheckThat Lab  
- Contacto: [tu-email@dominio.com]


