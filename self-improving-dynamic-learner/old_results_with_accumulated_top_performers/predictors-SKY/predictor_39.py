"""
Predictor 39
Generated on: 2025-09-09 04:08:06
Accuracy: 61.13%
"""


# PREDICTOR 39 - Accuracy: 61.13%
# Correct predictions: 6113/10000 (61.13%)

def predict_output(A, B, C, D, E):
    if E > 90 and D < 40 and C < 30:
        return 4
    if C < 15:
        if B < 40 and E > 60:
            return 4
        elif B > 50:
            return 1
        else:
            return 3
    if 15 <= C < 40:
        if C > 35 and D < 30 and E > 45:
            return 4
        if E < 20 and D < 30 and C > 30:
            return 3
        if D > 90:
            if B > 50:
                return 2
            else:
                return 1
        if D > 90 and E > 50:
            return 3
        if E > 80 and (C < 30 or D < 20):
            return 4
        if D < 10 and E > 70:
            return 4
        if E < 20 and D < 20 and A < 50:
            return 3
        if B > 60 and E > 70 and C < 40:
            return 2
        if E > 50 and B < 40 and D < 30 and C < 40 and A < 20:
            return 2
        else:
            return 1
    if C >= 70:
        if B > 60:
            if A >= 50:
                return 1
            else:
                if D > 90:
                    return 3
                if E < 30 and D < 20:
                    return 4
                elif E < 20:
                    return 2
                elif A < 20:
                    return 1
                elif A <= 25 and D > 70:
                    return 1
                else:
                    return 2
        else:
            if D < 20:
                if E < 30:
                    return 4
                else:
                    return 2
            else:
                return 1
    # For 40 <= C < 70
    if E > 80 and D < 30:
        return 4
    if B > 60 and D > 90 and E > 80:
        return 3
    elif B > 80 and C < 45:
        return 2
    elif E < 30 and A < 30 and C > 50:
        return 4
    elif A > 80 and B < 20 and D > 70:
        return 3
    else:
        return 1