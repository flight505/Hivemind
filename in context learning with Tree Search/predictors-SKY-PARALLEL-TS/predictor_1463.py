"""
Predictor 1463
Generated on: 2025-09-10 02:31:46
Accuracy: 56.36%
"""


# PREDICTOR 1463 - Accuracy: 56.36%
# Correct predictions: 5636/10000 (56.36%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 20 and D > 80) or (C < 10 and D < 10 and E > 50):
        return 4
    elif B >= 85 and D > 75 and E < 25:
        return 2
    elif 45 < A < 60 and C < 20 and D < 25:
        return 3
    else:
        return 1