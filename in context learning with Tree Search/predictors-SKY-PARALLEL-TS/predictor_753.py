"""
Predictor 753
Generated on: 2025-09-10 00:44:16
Accuracy: 57.53%
"""


# PREDICTOR 753 - Accuracy: 57.53%
# Correct predictions: 5753/10000 (57.53%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 80 and E > 80) or (D < 10 and E > 70) or (A > 50 and B < 30 and C < 35 and D < 5 and E > 70) or (A > 90 and B > 70 and C < 10 and D > 50) or (A > 50 and B < 10 and C > 30 and D < 20 and E > 80):
        return 4
    elif (B > 85 and C > 80 and A < 60) or (B > 70 and D < 20 and A < 50 and E > 40 and C > 50):
        return 2
    elif (A > 50 and C < 50 and D > 70 and B > 40) or (C < 10 and D > 70 and E < 60):
        return 3
    else:
        return 1