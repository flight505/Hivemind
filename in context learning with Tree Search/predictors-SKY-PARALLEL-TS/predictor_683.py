"""
Predictor 683
Generated on: 2025-09-10 00:34:06
Accuracy: 45.43%
"""


# PREDICTOR 683 - Accuracy: 45.43%
# Correct predictions: 4543/10000 (45.43%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 80) or (C > 90 and B < 30) or (C < 15 and B > 70):
        return 4
    elif (B > 80) or (A > 90 and E > 60) or (A < 10 and B > 60 and E > 50):
        return 2
    elif (B < 15 and A > 50) or (E < 10 and C > 25 and B > 30):
        return 3
    else:
        return 1