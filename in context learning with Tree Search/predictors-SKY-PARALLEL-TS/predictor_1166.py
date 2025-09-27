"""
Predictor 1166
Generated on: 2025-09-10 01:39:40
Accuracy: 39.85%
"""


# PREDICTOR 1166 - Accuracy: 39.85%
# Correct predictions: 3985/10000 (39.85%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and D > 20) or (C < 10 and D > 90) or (A > 80 and D < 30 and E > 70) or (B < 5 and E > 70) or (A > 70 and B < 15) or (C > 80 and D < 25 and E < 15):
        return 4
    elif (A > 90 and E < 10) or (B > 75 and C > 50):
        return 2
    elif (B < 10 and D > 80) or (A < 5 and B > 85 and D < 10) or (B < 30 and (C > 25 or D > 30)):
        return 3
    else:
        return 1