"""
Predictor 5
Generated on: 2025-09-09 17:07:15
Accuracy: 45.57%
"""


# PREDICTOR 5 - Accuracy: 45.57%
# Correct predictions: 4557/10000 (45.57%)

def predict_output(A, B, C, D, E):
    if E > 90:
        return 4
    if C >= 75:
        if B > 60:
            return 2
        elif B < 20:
            if E < 20:
                return 4
            else:
                return 1
        else:
            return 1
    if A < 5 and C > 65:
        return 4
    if B < 20:
        if C < 20:
            return 3
        else:
            if E < 20:
                return 4
            else:
                if C > 70:
                    return 4
                elif A < 10:
                    return 2
                else:
                    return 1
    if C < 40:
        if D > 50 or (E >= 60 and A < 50):
            return 1
        else:
            if C > 30:
                return 4
            else:
                return 3
    else:
        if B < 30 and D < 30 and C < 50:
            return 4
        if C < 50 and B > 50 and D < 60 and E < 50:
            return 2
        if B > 50 and D > 65:
            if A < 50:
                return 3
            else:
                return 1
        else:
            return 1