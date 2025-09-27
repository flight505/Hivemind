"""
Predictor 935
Generated on: 2025-09-10 01:07:55
Accuracy: 54.29%
"""


# PREDICTOR 935 - Accuracy: 54.29%
# Correct predictions: 5429/10000 (54.29%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (E > 60 and (B < 20 or (C < 26 and B < 60))):
        return 4
    elif B > 85 and E > 70:
        return 2
    elif (A > 40 and C < 40 and D > 80) or (A < 15 and C < 15 and D > 40) or (A > 50 and B < 30 and E < 15) or (A > 50 and B < 10 and D < 5):
        return 3
    else:
        return 1