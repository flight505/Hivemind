"""
Predictor 41
Generated on: 2025-09-09 23:21:45
Accuracy: 50.85%
"""


# PREDICTOR 41 - Accuracy: 50.85%
# Correct predictions: 5085/10000 (50.85%)

def predict_output(A, B, C, D, E):
    if (B - A > 60 and E > 10) or (D - C > 60) or (C > 75 and E < 5):
        return 4
    elif (A > 70 and B < 30 and E > 20) or (C < 10 and D > 60 and A < 15) or (B > 90 and E > 80):
        return 3
    elif B > 80 and E < 10 and A < 50:
        return 2
    else:
        return 1