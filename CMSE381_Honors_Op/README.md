# Image Augmentation for Concrete Crack Detection

## Project Overview

This project is part of my **CMSE 381 Honors Project** and explores how different image augmentation techniques affect the performance of crack detection models on concrete images.

Concrete crack detection is an important problem in structural health monitoring, but available datasets are often limited or imbalanced. Image augmentation is commonly used to address this issue, but its impact is not always straightforward. This project evaluates whether augmentation actually improves model performance and which techniques are most effective.

---

## Project Goals

The main goals of this project are to:

* Study the effect of image augmentation on crack detection accuracy
* Compare model performance with and without augmentation
* Identify which augmentation techniques improve generalization
* Better understand best practices for training CNNs on infrastructure data

---

## Dataset

* **Dataset:** SDNET2018 Concrete Crack Dataset
* **Classes:** Cracked and Non-cracked images
* **Surface Types:** Concrete walls, decks, and pavements (depending on subset)

The SDNET2018 dataset contains tens of thousands of labeled images and is widely used in research on automated crack detection.

---

## Methods

### Image Augmentation

The following augmentation techniques were applied and evaluated:

* Horizontal and vertical flipping
* Image rotation
* Brightness adjustment
* Contrast variation

### Model

* Convolutional Neural Network (CNN)
* Train–test split for evaluation
* Evaluation metrics:

  * Accuracy
  * Precision
  * Recall
  * F1-score

---

## Results Summary

Overall, image augmentation improved model generalization, especially when moderate transformations such as flipping and rotation were applied. Some augmentation techniques provided more consistent benefits than others, while excessive augmentation led to diminishing returns.

Detailed experiments, visualizations, and discussions can be found in the Jupyter Notebook.

---

## Repository Structure

```text
├── CMSE381_Honors_Project.ipynb   # Main analysis notebook
├── README.md                     # Project documentation
└── data/                          # Dataset (not included due to size)
```

---

## How to Run the Project

1. Clone the repository
2. Install the required dependencies:

   ```bash
   pip install numpy pandas matplotlib seaborn scikit-learn tensorflow keras opencv-python
   ```
3. Open the notebook:

   ```bash
   jupyter notebook CMSE381_Honors_Project.ipynb
   ```
4. Run the cells in order

---

## Course Information

* **Course:** CMSE 381 – Foundations of Data Science
* **Project Type:** Honors Project
* **Institution:** Michigan State University
* **Date:** April 2025

---

## Author

**[Your Name]**
Data Science Major, Michigan State University

---

## Notes

This project was completed for academic purposes. The dataset is not included in the repository due to size constraints.

---

## Future Work

Possible extensions of this project include:

* Testing additional augmentation techniques
* Using transfer learning with pretrained CNN models
* Evaluating performance on real-world inspection images
