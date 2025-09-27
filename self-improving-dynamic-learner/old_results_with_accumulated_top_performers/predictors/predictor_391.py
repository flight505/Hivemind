"""
Predictor 391
Generated on: 2025-09-09 11:02:01
Accuracy: 51.20%
"""


# PREDICTOR 391 - Accuracy: 51.20%
# Correct predictions: 5120/10000 (51.20%)

def predict_output(A, B, C, D, E):
    if B < 25 and C < 25:
        return 3
    elif A <= 30 and B > 60 and C > 60:
        return 2
    elif E > 80:
        return 4
    elif B > 60 or D > 70:
        return 1
    else:
        return 1