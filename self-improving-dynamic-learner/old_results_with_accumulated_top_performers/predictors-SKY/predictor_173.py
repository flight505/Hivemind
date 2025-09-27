"""
Predictor 173
Generated on: 2025-09-09 07:12:10
Accuracy: 47.40%
"""


# PREDICTOR 173 - Accuracy: 47.40%
# Correct predictions: 4740/10000 (47.40%)

def predict_output(A, B, C, D, E):
    if E > 90 and D < 40:
        return 4
    if C < 15:
        if B < 20:
            return 3
        elif B > 50:
            if D > 80:
                return 4
            elif E > 60:
                return 4
            else:
                return 1
        else:
            if A > 80 and D > 50:
                return 4
            else:
                return 3
    if C >= 70:
        if C > 80 and (B > 50 or E > 50):
            return 4
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
        if C > 50:
            if B > 80 or E > 80:
                return 4
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
        elif C > 20 and B < 40 and E < 40 and D < 40:
            return 3
        else:
            return 1
    else:
        if B > 60 and E > 70:
            if A >= 50:
                return 1
            else:
                return 2
        elif D > 70 and B > 40:
            return 3
        else:
            return 1