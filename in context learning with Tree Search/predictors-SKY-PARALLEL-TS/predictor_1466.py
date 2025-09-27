"""
Predictor 1466
Generated on: 2025-09-10 02:31:46
Accuracy: 49.40%
"""


# PREDICTOR 1466 - Accuracy: 49.40%
# Correct predictions: 4940/10000 (49.40%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (A > 80 and C < 20 and D > 80) or (C < 20 and D > 80):
        return 4
    elif B > 85 or (E >= 70 and C < 50):
        return 2
    elif (A > 90 and B < 15) or (D < 15 and C > 40) or (A > 50 and C < 50 and D > 70) or (C < 10 and E < 60) or (B > 80 and C > 85 and D > 80) or (A < 40 and B > 90 and D > 90) or (A > 70 and B < 20 and C < 30):
        return 3
    else:
        return 1