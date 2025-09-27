"""
Predictor 152
Generated on: 2025-09-09 06:44:11
Accuracy: 56.13%
"""


# PREDICTOR 152 - Accuracy: 56.13%
# Correct predictions: 5613/10000 (56.13%)

def predict_output(A, B, C, D, E):
    if E > 90 and D < 40:
        return 4
    if C < 15:
        if E > 80:
            if B > 60:
                return 1
            else:
                return 4
        if B < 20:
            return 3
        elif B > 50:
            if E > 60:
                return 4
            else:
                return 1
        else:
            return 3
    if C > 70:
        if B > 60:
            if A >= 50:
                return 1
            else:
                return 2
        else:
            if E < 10 and D > 60:
                return 4
            elif D < 20:
                if E > 50:
                    return 1
                else:
                    return 3
            else:
                return 1
    if C < 40:
        if E > 80 and C < 25 and B > 30:
            return 4
        elif D > 90 and C > 30:
            return 3
        elif B > 70 and C > 30:
            return 2
        elif B > 70 and E > 60:
            return 2
        elif B > 50 and E < 40:
            return 3
        else:
            return 1
    else:
        if B < 10 and E < 10 and C > 40:
            return 3
        if B > 60 and E > 70:
            if C < 60 and D < 40:
                return 4
            else:
                return 2
        elif D > 70 and B > 40:
            return 3
        else:
            return 1