"""
Predictor 80
Generated on: 2025-09-09 04:46:23
Accuracy: 37.35%
"""


# PREDICTOR 80 - Accuracy: 37.35%
# Correct predictions: 3735/10000 (37.35%)

def predict_output(A, B, C, D, E):
    if C < 15:
        if B < 40 and E > 60:
            if A < 20:
                return 2
            else:
                return 4
        elif B > 50:
            if E > 60:
                if A < 20:
                    return 2
                else:
                    return 4
            elif E < 20:
                if D < 20:
                    return 3
                else:
                    return 1
            else:
                return 1
        else:
            if C < 10 and E > 50:
                return 4
            else:
                return 3
    elif C > 70:
        if C > 80:
            return 4
        if B > 60:
            if A >= 50:
                return 1
            else:
                if E < 30 and D < 20:
                    return 4
                elif D > 50 and E > 90:
                    return 3
                elif E < 20:
                    return 4
                elif A < 20:
                    if B > 80:
                        return 2
                    else:
                        return 1
                elif E > 90 and D > 60:
                    return 1
                else:
                    return 2
        else:
            return 4
    elif 40 <= C < 70:
        if C > 55 and B < 30:
            return 1
        elif E > 80:
            return 4
        elif B > 75:
            return 4
        elif D > 50:
            return 3
        else:
            return 1
    elif C < 40:
        if A > 50 and C < 25 and E > 80 and B > 20:
            return 4
        elif A > 40 and E > 50 and C < 30 and B > 20 and D < 50:
            return 4
        elif C < 25 and E > 70 and B > 20:
            return 4
        elif D > 90 and C < 25:
            if E > 80:
                return 1
            else:
                return 4
        elif B > 50 and E < 40:
            if E < 10 and D < 20:
                return 1
            else:
                if D > 80:
                    return 4
                elif D > 70:
                    return 3
                elif A > 50:
                    return 1
                else:
                    return 4
        elif C < 20 and D < 10 and E > 60:
            return 4
        elif C < 35 and D < 25 and A < 60 and B < 50:
            return 3
        elif C > 30 and C < 40 and D > 90:
            if B > 60:
                return 1
            else:
                return 3
        elif D > 60 and E < 10:
            return 4
        elif D < 20 and E < 20:
            return 3
        elif E > 60 and B > 70:
            return 2
        elif A > 60 and B < 50 and E > 70:
            return 3
        elif B > 90 and E > 90:
            return 1
        elif E > 80 and C < 30 and B > 30:
            return 4
        elif E > 60 and D < 10:
            return 4
        else:
            return 1
    else:
        return 1