"""
Predictor 108
Generated on: 2025-09-09 20:03:05
Accuracy: 48.78%
"""


# PREDICTOR 108 - Accuracy: 48.78%
# Correct predictions: 4878/10000 (48.78%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C >= 50:
            return 2
        else:
            if D < 30:
                return 1
            else:
                return 4
    elif B >= 70:
        if C >= 50:
            return 2
        else:
            if D < 30:
                return 1
            elif E < 20:
                return 3
            else:
                return 1
    else:
        if C >= 50:
            if E < 20:
                return 4
            else:
                return 1
        else:
            if E < 20:
                return 1
            elif E > 50:
                if A > 80:
                    return 3
                else:
                    return 1
            else:
                return 3