"""
Predictor 1266
Generated on: 2025-09-10 01:54:58
Accuracy: 51.33%
"""


# PREDICTOR 1266 - Accuracy: 51.33%
# Correct predictions: 5133/10000 (51.33%)

def predict_output(A, B, C, D, E):
    total = A + B + C + D + E
    avg = total / 5
    if (A < 15 and B > 60 and D > 70) or (C < 15 and D > 80):
        return 4
    elif (B > 80 and C > 70) or (B > 70 and E > 80 and A < 50):
        return 2
    elif (A > 70 and B < 20) or (A > 40 and C < 30 and D > 60):
        return 3
    elif avg > 50 and E < 30:
        return 1
    else:
        return 1