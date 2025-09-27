"""
Predictor 1131
Generated on: 2025-09-10 01:35:54
Accuracy: 54.99%
"""


# PREDICTOR 1131 - Accuracy: 54.99%
# Correct predictions: 5499/10000 (54.99%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 80) or (A > 80 and E > 55) or (B > 80 and C < 5) or (C > 60 and E < 40 and A < 50):
        return 4
    elif (A > 80 and B < 20 and C > 90) or (B > 70 and C > 90) or (A < 10 and B > 60 and D < 5 and E > 70) or (B > 90 and E > 80):
        return 2
    elif (A > 50 and C < 50 and D > 70 and B > 40) or (C <= 10 and E < 60 and B < 50) or (A > 60 and B < 20 and C < 20):
        return 3
    else:
        return 1