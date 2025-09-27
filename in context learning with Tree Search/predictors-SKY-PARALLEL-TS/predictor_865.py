"""
Predictor 865
Generated on: 2025-09-10 00:58:03
Accuracy: 54.14%
"""


# PREDICTOR 865 - Accuracy: 54.14%
# Correct predictions: 5414/10000 (54.14%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10) or (B > 80 and D < 30) or (C > 85 and E < 10) or (C < 20 and D > 80) or (C < 15 and D > 90):
        return 4
    elif (B > 80 and C > 89) or (B > 75 and D > 60 and C < 40):
        return 2
    elif (A < 10 and B > 90 and E < 20) or (A < 5 and C > 80 and D < 10 and E < 10):
        return 3
    else:
        return 1