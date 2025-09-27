"""
Predictor 806
Generated on: 2025-09-10 00:50:43
Accuracy: 50.85%
"""


# PREDICTOR 806 - Accuracy: 50.85%
# Correct predictions: 5085/10000 (50.85%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 20 and D > 90) or (B < 30 and C > 60) or (A > 70 and B < 20) or (C > 90 and E < 15) or (B > 90 and C < 35 and D > 50):
        return 4
    elif (B > 90 and C > 70 and D > 50) or (B > 85 and E < 10):
        return 2
    elif (A > 50 and C < 50 and D > 70 and B > 40) or (A > 90 and B < 10 and D > 90):
        return 3
    else:
        return 1