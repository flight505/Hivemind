"""
Predictor 1190
Generated on: 2025-09-10 01:43:05
Accuracy: 54.12%
"""


# PREDICTOR 1190 - Accuracy: 54.12%
# Correct predictions: 5412/10000 (54.12%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (D > 60 and E < 15 and B < 30) or (B < 10 and D > 50 and E < 10):
        return 4
    elif (B > 70 and E > 90) or (B > 90 and C > 50):
        return 2
    elif (B < 10 and C < 10 and D > 80) or (C < 10 and D > 80 and E < 5) or (A < 20 and B > 40 and C < 20 and D > 40):
        return 3
    else:
        return 1