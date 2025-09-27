"""
Predictor 4
Generated on: 2025-09-09 03:36:11
Accuracy: 45.88%
"""


# PREDICTOR 4 - Accuracy: 45.88%
# Correct predictions: 4588/10000 (45.88%)

def predict_output(A, B, C, D, E):
    if E > 90:
        return 4
    elif B > 60 and C > 70:
        return 2
    elif C < 15:
        if E > 60:
            return 4
        elif B < 30:
            return 3
        else:
            return 1
    else:
        if B > 60 and C < 70:
            return 2
        elif 30 <= C < 50 and A > 50:
            return 3
        else:
            return 1