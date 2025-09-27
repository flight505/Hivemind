"""
Predictor 738
Generated on: 2025-09-10 00:41:18
Accuracy: 48.07%
"""


# PREDICTOR 738 - Accuracy: 48.07%
# Correct predictions: 4807/10000 (48.07%)

def predict_output(A, B, C, D, E):
    if (B - A > 60) or (D - C > 80) or (E > 80 and C < 40) or (C > 80 and B < 20) or (B > 95 and A < 30) or (C < 10 and E > 60):
        return 4
    elif (A + B > 150) or (B > 70 and C > 70 and D > 50) or (A < 10 and E > 90):
        return 2
    elif (B + E > 150) or (A < 30 and B < 30 and E < 30) or (C > 50 and D < 20 and A < 30):
        return 3
    else:
        return 1