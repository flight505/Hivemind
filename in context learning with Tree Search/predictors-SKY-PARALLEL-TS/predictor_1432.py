"""
Predictor 1432
Generated on: 2025-09-10 02:27:48
Accuracy: 49.17%
"""


# PREDICTOR 1432 - Accuracy: 49.17%
# Correct predictions: 4917/10000 (49.17%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (B > 80 and C < 20) or (C > 80 and (A < 20 or E < 10)) or (E < 10 and D > 50) or (A > 60 and B < 20 and C < 15):
        return 4
    elif (B > 85) or (E > 90) or (B > 80 and D > 80):
        return 2
    elif (A > 50 and D > 70 and C < 50) or (B < 50 and C < 10 and E < 60):
        return 3
    else:
        return 1