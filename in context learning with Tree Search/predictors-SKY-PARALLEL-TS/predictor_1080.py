"""
Predictor 1080
Generated on: 2025-09-10 01:28:10
Accuracy: 51.36%
"""


# PREDICTOR 1080 - Accuracy: 51.36%
# Correct predictions: 5136/10000 (51.36%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 60 and E > 80) or (B > 90 and E > 80):
        return 4
    elif (C < 15 and D > 60):
        return 3
    elif (D > 90 and B < 20) or (C < 10 and D > 60):
        return 3
    elif (B > 70 and C > 70) or (B > 90 and E < 5) or (E > 90 and A < 5):
        return 2
    else:
        return 1