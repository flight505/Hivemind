"""
Predictor 83
Generated on: 2025-09-09 23:27:20
Accuracy: 57.14%
"""


# PREDICTOR 83 - Accuracy: 57.14%
# Correct predictions: 5714/10000 (57.14%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 55) or (C <= 25 and E > 70) or (B < 20 and C > 60 and D < 35) or (B > 90 and E > 90) or (A > 90 and D > 70) or (C > 70 and D < 25 and E < 25 and A < 50 and B > 40) or (A > 80 and B < 10 and D > 70 and E < 10):
        return 4
    if (B > 85 and C > 80) or (B > 70 and D < 20 and A < 50 and E > 40) or (B > 90 and C > 70) or (B > 90 and D > 90) or (C > 60 and E > 80 and B > 50):
        return 2
    if (A > 50 and C < 50 and D > 70 and B > 40) or (A < 50 and D < 25 and E < 20 and B < 80) or (D < 15 and C > 40 and B < 80) or (C <= 10 and E < 60 and B < 80):
        return 3
    else:
        return 1