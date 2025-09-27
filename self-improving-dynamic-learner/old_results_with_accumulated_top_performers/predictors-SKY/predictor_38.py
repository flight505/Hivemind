"""
Predictor 38
Generated on: 2025-09-09 04:06:57
Accuracy: 58.37%
"""


# PREDICTOR 38 - Accuracy: 58.37%
# Correct predictions: 5837/10000 (58.37%)

def predict_output(A, B, C, D, E):
    if E > 90 and D < 40 and C < 30:
        return 4
    if C < 15:
        if E > 60:
            if B < 25:
                return 1
            else:
                return 4
        else:
            if B < 20:
                if D < 10:
                    return 1
                elif E > 50 and D > 50:
                    return 4
                else:
                    return 3
            elif B > 50:
                return 1
            else:
                if E > 50 and D > 50:
                    return 4
                else:
                    return 3
    if 15 <= C < 40:
        if D > 90:
            if B > 50:
                return 2
            else:
                return 1
        if D > 70 and E > 50:
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
                if B > 90 and C > 80:
                    return 1
                elif E > 50 and D > 70:
                    return 3
                elif E > 50:
                    return 2
                elif E < 30 and B > 70:
                    return 4
                elif D > 90:
                    return 1
                else:
                    return 3
        else:
            if D < 20 and E < 30:
                return 4
            else:
                return 1
    # For 40 <= C < 70
    if B < 20 and D > 50:
        return 3
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