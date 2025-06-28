# 🧠 Alzheimer MRI Classification using AI

This project focuses on detecting Alzheimer's disease using MRI brain scans with the help of deep learning and machine learning models. Our best-performing model, based on the Google Vision Transformer (ViT), achieves high accuracy across multiple severity levels.

## 🚀 Live Demo

Try the deployed model on Hugging Face Spaces:  
🔗 [Click to Run the Model](https://huggingface.co/spaces/AhmadHakami/Alzheimer_image_classification)

---

## 🧩 About the Dataset

We used the **OASIS Alzheimer MRI Dataset**, available on Kaggle:  
🔗 [https://www.kaggle.com/datasets/sachinkumar413/alzheimer-mri-dataset](https://www.kaggle.com/datasets/sachinkumar413/alzheimer-mri-dataset)

The dataset contains brain MRI images divided into four classes:
- **Non Demented**
- **Very Mild Demented**
- **Mild Demented**
- **Moderate Demented**

We applied data cleaning and augmentation techniques to balance the classes.

---

## 🛠️ Project Pipeline

1. **Understand the Problem**  
2. **Exploratory Data Analysis (EDA) & Processing**  
3. **Modeling & Evaluation**  
4. **Deployment & Sharing**

---

## 🧪 Models Used

### ✅ Classical Machine Learning
- Support Vector Machine (SVM)
- Gradient Boosting
- Naive Bayes

### ✅ Deep Learning
- Convolutional Neural Network (CNN)
- AlexNet (Transfer Learning)

### ✅ Vision Transformers (ViT)
- Google Base
- Microsoft Base
- Google Large + PEFT (Parameter-Efficient Fine-Tuning)

---

## 🏆 Best Model

- **Google Base ViT**
  - Achieved high precision, recall, and F1-score across all classes.
  - Trained using TensorBoard for monitoring.

| Class               | Precision | Recall | F1-score |
|--------------------|-----------|--------|----------|
| Non Demented       | 0.94      | 0.95   | 0.94     |
| Very Mild Demented | 1.00      | 1.00   | 1.00     |
| Mild Demented      | 0.91      | 0.93   | 0.92     |
| Moderate Demented  | 0.97      | 0.94   | 0.96     |

---

## 📊 Tools and Packages

- Python, NumPy, Pandas, Matplotlib, Seaborn
- Scikit-learn
- TensorFlow & Keras
- Transformers (Hugging Face)
- PEFT (for efficient fine-tuning)
- OpenCV
- Google Colab & TensorBoard

---

## 📁 Project Structure

```bash
.
├── notebooks/               # All modeling notebooks
├── models scores/          # Evaluation images & confusion matrices
├── results_confidence/     # Confidence values for each model
├── dataframes/             # Processed CSV data
├── augmentation/           # Data augmentation scripts
└── README.md               # Project description

