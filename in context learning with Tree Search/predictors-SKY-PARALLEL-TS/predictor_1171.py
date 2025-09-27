"""
Predictor 1171
Generated on: 2025-09-10 01:39:40
Accuracy: 53.64%
"""


# PREDICTOR 1171 - Accuracy: 53.64%
# Correct predictions: 5364/10000 (53.64%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (C < 35 and D > 40 and E < 20 and B < 50) or (B > 90 and E > 90) or (B > 90 and C < 30) or (C < 30 and D > 70):
        return 4
    elif D < 5 and E > 70:
        return 2
    elif B < 10 and C > 70:
        return 3
    else:
        return 1