"""
Predictor 966
Generated on: 2025-09-10 01:09:35
Accuracy: 51.57%
"""


# PREDICTOR 966 - Accuracy: 51.57%
# Correct predictions: 5157/10000 (51.57%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and E < 20) or (D > 90 and B > 50) or (C > 60 and E < 10):
        return 4
    elif (B > 90) or (E > 90 and D < 20 and C < 60):
        return 2
    elif A > 50 and C < 5:
        return 3
    else:
        return 1