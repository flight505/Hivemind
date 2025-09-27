"""
Predictor 1295
Generated on: 2025-09-10 02:02:09
Accuracy: 46.51%
"""


# PREDICTOR 1295 - Accuracy: 46.51%
# Correct predictions: 4651/10000 (46.51%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (A < 25 and B < 15 and C > 50) or (A < 15 and C > 90):
        return 4
    elif (B > 60 and C > 70) or (C > 80 and D < 20):
        return 2
    elif D > 70 and E < 30:
        return 3
    else:
        return 1