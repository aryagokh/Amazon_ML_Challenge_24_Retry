import pandas as pd
from tqdm import tqdm

def calculate_f1_score(ground_truth_col, prediction_col):
    """
    Calculate the F1 score given two columns: ground truth and predictions.

    Args:
        ground_truth_col (pd.Series): Ground truth column with entity values.
        prediction_col (pd.Series): Predictions column from the model.

    Returns:
        dict: A dictionary containing True Positives, False Positives, 
              False Negatives, Precision, Recall, and F1-Score.
    """
    # Initialize Counters
    true_positive = 0
    false_positive = 0
    false_negative = 0

    # Iterate over the ground truth and predictions
    for gt, pred in tqdm(zip(ground_truth_col, prediction_col), total=len(ground_truth_col), desc="Calculating F1 Score"):
        if pred != "" and gt != "" and pred == gt:
            true_positive += 1
        elif pred != "" and gt != "" and pred != gt:
            false_positive += 1
        elif pred != "" and gt == "":
            false_positive += 1
        elif pred == "" and gt != "":
            false_negative += 1

    # Safely calculate Precision, Recall, and F1-Score with checks for zero division
    precision = true_positive / (true_positive + false_positive) if (true_positive + false_positive) > 0 else 0
    recall = true_positive / (true_positive + false_negative) if (true_positive + false_negative) > 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    # Return the results as a dictionary
    return {
        "True Positives": true_positive,
        "False Positives": false_positive,
        "False Negatives": false_negative,
        "Precision": precision,
        "Recall": recall,
        "F1-Score": f1_score
    }
