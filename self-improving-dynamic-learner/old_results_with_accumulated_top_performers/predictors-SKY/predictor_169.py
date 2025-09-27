"""
Predictor 169
Generated on: 2025-09-09 07:07:38
Accuracy: 56.62%
"""


# PREDICTOR 169 - Accuracy: 56.62%
# Correct predictions: 5662/10000 (56.62%)

def predict_output(A, B, C, D, E):
    if E > 90 and D < 40 and C < 40:
        return 4
    if C < 15:
        if B < 40 and E > 60:
            return 4
        elif B > 50:
            if C < 10:
                return 3
            else:
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
                elif D > 50 and E > 90:
                    return 3
                elif E < 20:
                    return 4
                elif A < 20:
                    return 1
                else:
                    return 2
        else:
            if D < 20:
                if B < 20:
                    return 2
                elif E > 50:
                    return 1
                else:
                    return 3
            else:
                if E < 40 and B < 30:
                    return 4
                else:
                    return 1
    if C < 40:
        if A > 50 and C < 25:
            if A > 70 and C < 20:
                return 3
            elif E > 80 and B > 20:
                return 4
            else:
                return 4
        elif A > 40 and E > 50 and C < 30 and B > 20:
            return 4
        elif C < 25 and E > 70 and B > 20:
            return 4
        elif C < 35 and D < 25 and A < 60 and B < 50:
            return 3
        elif C > 30 and C < 40 and D > 90:
            return 3
        elif D > 60 and E < 10:
            return 4
        elif D < 20 and E < 20:
            return 3
        elif E > 60 and B > 70 and C < 30:
            return 2
        elif B > 70 and E < 40:
            return 1
        elif C > 40 and C < 50:
            return 3
        elif D > 50 and E < 10:
            return 4
        elif C > 35 and D < 50:
            return 4
        else:
            return 1
    else:
        if B > 60:
            if A >= 50:
                return 1
            else:
                if C > 60:
                    if C > 80 and A < 5:
                        return 4
                    elif D < 40:
                        return 1
                    else:
                        return 2
                else:
                    return 1
        elif 35 < C < 45 and B < 50 and D > 50 and E < 70:
            return 3
        elif E > 80:
            return 4
        else:
            return 1