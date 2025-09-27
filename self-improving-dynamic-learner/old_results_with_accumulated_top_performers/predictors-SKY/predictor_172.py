"""
Predictor 172
Generated on: 2025-09-09 07:11:16
Accuracy: 56.65%
"""


# PREDICTOR 172 - Accuracy: 56.65%
# Correct predictions: 5665/10000 (56.65%)

def predict_output(A, B, C, D, E):
    if E > 90 and D < 40:
        return 4
    if C < 15:
        if B < 20:
            return 3
        elif B > 50:
            if E > 60:
                return 4
            elif D > 80:
                return 4
            else:
                return 1
        else:
            return 3
    if C >= 70:
        if B > 60:
            if A >= 50:
                return 1
            else:
                if E < 20:
                    return 4
                elif D > 90:
                    return 3
                else:
                    return 2
        else:
            if D < 20:
                if E > 50:
                    return 1
                else:
                    return 3
            else:
                return 1
    if C < 40:
        if E > 80 and C < 25:
            return 4
        elif B > 80 and E > 90:
            return 2
        elif B > 50 and E < 40:
            if D > 80:
                return 4
            else:
                return 3
        elif D < 20 and E < 20:
            return 3
        elif B > 70 and E > 60:
            return 2
        else:
            return 1
    else:
        if B > 60 and E > 70:
            return 2
        elif D > 70 and B > 40:
            return 3
        else:
            return 1