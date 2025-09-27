"""
Predictor 3
Generated on: 2025-09-09 03:35:23
Accuracy: 42.88%
"""


# PREDICTOR 3 - Accuracy: 42.88%
# Correct predictions: 4288/10000 (42.88%)

def predict_output(A, B, C, D, E):
    if C > 70:
        if B > 60:
            if A > 60:
                return 1
            else:
                if E > 50:
                    return 2
                else:
                    return 4
        else:
            return 3
    else:
        if E > 70 and C < 25:
            return 4
        elif C < 15:
            return 3
        elif A > 50 and B < 65 and C < 50:
            return 4
        else:
            return 1