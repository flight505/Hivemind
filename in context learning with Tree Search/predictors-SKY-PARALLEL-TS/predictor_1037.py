"""
Predictor 1037
Generated on: 2025-09-10 01:20:29
Accuracy: 53.37%
"""


# PREDICTOR 1037 - Accuracy: 53.37%
# Correct predictions: 5337/10000 (53.37%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (40 < A < 50 and B > 60 and C < 20 and D > 50 and E > 50) or (A > 95 and B > 40 and C > 55 and D < 40 and E > 80) or (A < 30 and B > 80 and C < 20 and D > 75 and E < 50):
        return 4
    elif (A > 90 and E < 10) or (B > 85 and C > 80):
        return 2
    elif (B < 10 and D > 80) or (A > 50 and B < 5 and C < 20 and D < 25 and E > 40) or (A > 90 and B < 35 and C < 45 and D > 90 and E < 60):
        return 3
    else:
        return 1