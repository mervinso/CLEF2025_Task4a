
# CLEF2025 CheckThat (Task 4a & 4b) README

## 🏁 Project Overview

This repository contains the full pipeline to tackle the CLEF2025 CheckThat Lab, focusing on Task 4:

* **4a:** Scientific Web Discourse Detection (multilabel classification)
* **4b:** Scientific Claim Source Retrieval (ranking & retrieval)

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
