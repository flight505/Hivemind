"""
Predictor 1083
Generated on: 2025-09-10 01:28:10
Accuracy: 51.64%
"""


# PREDICTOR 1083 - Accuracy: 51.64%
# Correct predictions: 5164/10000 (51.64%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (B > 90 and E > 80):
        return 4
    elif (B >= 70 and C > 75) or (E > 90 and A < 5) or (B > 90 and E < 5):
        return 2
    elif (C < 15 and D > 70 and E < 50) or (D > 90 and B < 20):
        return 3
    else:
        return 1