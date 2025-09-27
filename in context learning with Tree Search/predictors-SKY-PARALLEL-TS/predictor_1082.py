"""
Predictor 1082
Generated on: 2025-09-10 01:28:10
Accuracy: 50.61%
"""


# PREDICTOR 1082 - Accuracy: 50.61%
# Correct predictions: 5061/10000 (50.61%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 60 and E > 80) or (B > 90 and E > 80):
        return 4
    elif (C < 15 and D > 60) or (D > 90 and B < 20) or (C < 10 and D > 60) or (A > 80 and B < 20 and D > 90):
        return 3
    elif (B >= 70 and C > 70) or (B > 90 and E < 5) or (E > 90 and A < 5) or (A > 70 and B > 80 and C < 50):
        return 2
    else:
        return 1