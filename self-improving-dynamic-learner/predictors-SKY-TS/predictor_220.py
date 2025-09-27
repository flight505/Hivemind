"""
Predictor 220
Generated on: 2025-09-09 21:03:09
Accuracy: 48.97%
"""


# PREDICTOR 220 - Accuracy: 48.97%
# Correct predictions: 4897/10000 (48.97%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40 and E < 20:
                return 1
            else:
                return 4
        else:
            if D < 50:
                if E > 70:
                    return 4
                else:
                    return 1
            else:
                return 2
    else:
        if C >= 50:
            if D > 50 or E > 50:
                return 1
            else:
                return 4
        else:
            if E < 20:
                if A > 60:
                    return 1
                elif B >= 60:
                    return 4
                else:
                    return 3
            else:
                if B >= 70:
                    return 4
                elif C > 40:
                    return 4
                elif A < 20:
                    return 1
                else:
                    return 3