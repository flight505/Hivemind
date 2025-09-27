"""
Predictor 429
Generated on: 2025-09-10 00:02:23
Accuracy: 44.87%
"""


# PREDICTOR 429 - Accuracy: 44.87%
# Correct predictions: 4487/10000 (44.87%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90 and E > 80) or (E > 80 and D > 50 and B > 60):
        return 4
    elif (B > 85 and C > 80 and A < 50) or (A > 90 and E < 10):
        return 2
    elif (A < 20 and B > 70 and D < 25 and E < 30) or (A < C and D > 70) or (A > 90 and B < 10 and C < 15 and D > 90) or (A + B + C + D + E < 100):
        return 3
    else:
        return 1