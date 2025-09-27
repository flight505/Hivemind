"""
Predictor 1139
Generated on: 2025-09-10 01:35:54
Accuracy: 40.01%
"""


# PREDICTOR 1139 - Accuracy: 40.01%
# Correct predictions: 4001/10000 (40.01%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (B < 35 and C > 35 and A > 60) or (B < 25 and C > 90):
        return 4
    elif B > 80:
        return 2
    elif (C > 70 and D > 80) or (D > 90) or (A < 5 and C < 15):
        return 3
    else:
        return 1