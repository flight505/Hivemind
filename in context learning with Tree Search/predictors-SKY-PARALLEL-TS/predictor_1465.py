"""
Predictor 1465
Generated on: 2025-09-10 02:31:46
Accuracy: 47.01%
"""


# PREDICTOR 1465 - Accuracy: 47.01%
# Correct predictions: 4701/10000 (47.01%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (B < 20 and C > 80) or (D > 90 and E > 80) or (C < 20 and D > 80):
        return 4
    elif (B > 90) or (E > 70 and B > 80) or (B > 80 and C > 40 and D > 70) or (E > 70 and D < 25 and B < 40) or (B > 85 and E > 65) or (B > 90 and E < 40) or (E > 70 and A < 50 and B < 40):
        return 2
    elif (A > 90 and B < 15) or (D < 15 and C > 40) or (A > 50 and C < 50 and D > 70) or (C < 10 and E < 60) or (B > 80 and C > 85 and D > 80) or (A < 40 and B > 90 and D > 90) or (A > 70 and B < 20 and C < 30):
        return 3
    else:
        return 1