"""
Predictor 1243
Generated on: 2025-09-10 01:52:29
Accuracy: 48.96%
"""


# PREDICTOR 1243 - Accuracy: 48.96%
# Correct predictions: 4896/10000 (48.96%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or (C < 15 and D > 60) or (C < 25 and E > 65) or (A > 50 and B < 20 and E > 80) or (B > 70 and A < 30 and C > 60) or (C > 80 and D < 30) or (A > 90 and E > 80) or (D > 80 and B > 50) or (A > 70 and B < 20 and C < 30)):
        return 4
    elif ((B > 85 and C > 80) or (D < 20 and E > 40 and A < 50) or (B > 70 and E < 25) or (E > 90 and A < 40) or (B > 90 and C < 50)):
        return 2
    elif ((A > 70 and D > 70 and C < 45) or (A > 70 and B < 15 and C < 5) or (D > 90 and E < 10) or (B > 80 and C > 85) or (A > 40 and D > 80 and C < 50)):
        return 3
    else:
        return 1