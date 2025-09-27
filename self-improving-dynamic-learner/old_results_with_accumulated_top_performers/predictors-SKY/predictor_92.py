"""
Predictor 92
Generated on: 2025-09-09 05:02:36
Accuracy: 42.75%
"""


# PREDICTOR 92 - Accuracy: 42.75%
# Correct predictions: 4275/10000 (42.75%)

def predict_output(A, B, C, D, E):
    if E > 90 and D < 40:
        return 4
    if C < 15 and B < 20:
        return 3
    if C > 60:
        if B > 60:
            if D < 20:
                if A >= 50:
                    return 1
                else:
                    return 2
            else:
                if E < 60:
                    return 3
                else:
                    return 2
        else:
            if D < 20 and E > 60:
                if A >= 50:
                    return 2
                else:
                    return 4
            else:
                return 1
    if 40 < C < 60 and B > 60 and A >= 50:
        return 2
    if C < 25 and B > 80:
        if E > 80:
            return 3
        else:
            return 1
    if D > 80:
        return 1
    if C < 40:
        return 3
    else:
        return 1