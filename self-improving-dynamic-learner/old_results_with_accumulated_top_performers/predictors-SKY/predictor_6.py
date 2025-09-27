"""
Predictor 6
Generated on: 2025-09-09 03:40:02
Accuracy: 53.23%
"""


# PREDICTOR 6 - Accuracy: 53.23%
# Correct predictions: 5323/10000 (53.23%)

def predict_output(A, B, C, D, E):
    if E > 90 and D < 40:
        return 4
    if C < 15:
        if E > 60:
            return 4
        elif B > 50:
            return 1
        else:
            return 3
    if C > 70:
        if B > 60:
            if A >= 50:
                return 1
            else:
                if E < 30 and D < 20:
                    return 4
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
        if A > 50 and C < 25:
            return 4
        elif A > 40 and E > 50:
            return 4
        elif D < 20 and E < 20:
            return 3
        elif E > 60:
            return 2
        elif B > 50 and E < 40:
            return 3
        else:
            return 1
    else:
        if E < 15 and A > 40:
            return 4
        if B > 60:
            if A > 70 and C < 50:
                return 2
            elif C > 60:
                if A < 50:
                    return 2
                else:
                    return 1
            else:
                return 3
        elif B < 20:
            if E > 80:
                return 1
            else:
                return 3
        elif D >= 90:
            return 3
        elif A > 70 and B < 40 and E > 70:
            return 3
        else:
            return 1