"""
Predictor 30
Generated on: 2025-09-09 19:14:13
Accuracy: 52.23%
"""


# PREDICTOR 30 - Accuracy: 52.23%
# Correct predictions: 5223/10000 (52.23%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                return 1
            else:
                return 4
        else:
            return 2
    else:
        if C > 50:
            if E < 20:
                if D > 60:
                    return 1
                else:
                    return 4
            else:
                return 1
        else:
            if E < 20:
                if D > 60:
                    return 1
                else:
                    return 3
            else:
                if E > 90:
                    return 4
                elif A < 50 and D > 60 and C > 15:
                    return 1
                else:
                    return 3