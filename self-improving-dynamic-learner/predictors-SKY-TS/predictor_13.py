"""
Predictor 13
Generated on: 2025-09-09 19:03:14
Accuracy: 42.35%
"""


# PREDICTOR 13 - Accuracy: 42.35%
# Correct predictions: 4235/10000 (42.35%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                return 1
            else:
                return 4
        else:
            if E < 20:
                return 1
            else:
                return 2
    else:
        if C > 50:
            if D < 40:
                if E < 70:
                    return 4
                else:
                    return 1
            else:
                if C >= 70:
                    return 1
                else:
                    return 3
        else:
            if D < 20 and C > 40:
                return 2
            elif B < 25:
                if D > 50 or E > 60:
                    return 1
                else:
                    return 3
            else:
                return 3