# Cancer Classification Report

## Evaluation Metrics
| Model | Accuracy | Precision | Recall | F1 Score | Training Time |
|-------|----------|-----------|--------|----------|---------------|
| Custom KNN | 0.9561 | 0.9773 | 0.9149 | 0.9451 | 0.0020 |
| Custom NaiveBayes | 0.9298 | 0.9149 | 0.9149 | 0.9149 | 0.0024 |
| Logistic Regression | 0.9561 | 1.0000 | 0.8936 | 0.9438 | 0.0049 |
| Gradient Boosting | 0.9825 | 0.9787 | 0.9787 | 0.9787 | 0.0268 |
| XGBoost | 0.9561 | 0.9565 | 0.9362 | 0.9462 | 0.0206 |


## Cross-Validation Scores

| Model | Cross-Validation Score |
|-------|-----------------------|
| Custom KNN | 0.9491 (+/- 0.0380) |
| Custom NaiveBayes | 0.9332 (+/- 0.0291) |
| Logistic Regression | 0.9367 (+/- 0.0274) |
| Gradient Boosting | 0.9404 (+/- 0.0353) |
| XGBoost | 0.9561 (+/- 0.0335) |

---
## Classification Reports

### **Custom KNN**

Best Params for Custom KNN model:
- {'feature_selection__k': 8, 'pca__n_components': 5}

![ROC Curve for Custom KNN](./figures/roc_curve_Custom_KNN.png)

![Precision-Recall Curve for Custom KNN](./figures/precision_recall_curve_Custom_KNN.png)

### **Custom NaiveBayes**

### Best Params for Custom NaiveBayes model

- {'feature_selection__k': 7, 'pca__n_components': 3}


![ROC Curve for Custom NaiveBayes](./figures/roc_curve_Custom_NaiveBayes.png)

![Precision-Recall Curve for Custom NaiveBayes](./figures/precision_recall_curve_Custom_NaiveBayes.png)


### **Logistic Regression**
### Best Params for Logistic Regression model
- {'classifier__C': 0.02, 'classifier__penalty': 'l2', 'feature_selection__k': 10, 'pca__n_components': 4}

![ROC Curve for Logistic Regression](./figures/roc_curve_Logistic_Regression.png)

![Precision-Recall Curve for Logistic Regression](./figures/precision_recall_curve_Logistic_Regression.png)

### **Gradient Boosting**
### Best Params for Gradient Boosting model

- {'classifier__learning_rate': 1, 'classifier__n_estimators': 20, 'feature_selection__k': 7, 'pca__n_components': 6}

![ROC Curve for Gradient Boosting](./figures/roc_curve_Gradient_Boosting.png)

![Precision-Recall Curve for Gradient Boosting](./figures/precision_recall_curve_Gradient_Boosting.png)

### **XGBoost**

### Best Params for XGBoost model

- {'classifier__learning_rate': 0.2, 'classifier__max_depth': 5, 'classifier__n_estimators': 20, 'feature_selection__k': 7, 'pca__n_components': 5}

![ROC Curve for XGBoost](./figures/roc_curve_XGBoost.png)

![Precision-Recall Curve for XGBoost](./figures/precision_recall_curve_XGBoost.png)

