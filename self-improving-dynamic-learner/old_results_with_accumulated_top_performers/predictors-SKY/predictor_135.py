"""
Predictor 135
Generated on: 2025-09-09 05:55:11
Accuracy: 59.48%
"""


# PREDICTOR 135 - Accuracy: 59.48%
# Correct predictions: 5948/10000 (59.48%)

def predict_output(A, B, C, D, E):
    if E > 90 and D < 40:
        return 4
    if C < 15:
        if B > 50:
            if E > 60:
                if A < 20:
                    return 2
                else:
                    return 4
            elif E < 20 and C < 10 and E > 10:
                return 3
            elif E < 20:
                return 1
            else:
                if A > 50:
                    return 1
                else:
                    return 3
        else:
            if D > 80 and E > 60 and B < 25:
                return 4
            elif D > 90 and E < 20:
                return 1
            elif E > 50:
                return 4
            else:
                return 3
    if C >= 70:
        if B > 60:
            if A >= 50:
                if D > 90 and E < 50:
                    return 3
                else:
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
                else:
                    return 2
        else:
            if D < 20:
                if B < 20:
                    if A >= 50:
                        return 4
                    else:
                        return 3
                elif E > 50:
                    if C < 85:
                        return 1
                    else:
                        return 2
                else:
                    if C > 85 and E < 40:
                        return 4
                    else:
                        return 3
            else:
                if E < 40 and B < 30:
                    return 4
                else:
                    return 1
    if C < 40:
        if A > 50 and C < 25 and E > 80 and B > 20:
            return 4
        elif A > 40 and E > 50 and C < 30 and B > 20 and B < 60:
            return 4
        elif C < 25 and E > 70 and B > 20 and B < 90:
            return 4
        elif B > 90:
            return 2
        elif C > 25 and E > 70 and B > 70 and A > 40:
            return 2
        elif A > 70 and B > 60 and E < 60:
            return 2
        else:
            return 1
    else:
        if C > 55 and D < 30:
            return 4
        elif E < 30 and B < 50:
            return 4
        else:
            if B > 60 and D > 70:
                return 3
            if C < 50 and D > 70 and E > 10 and B > 40:
                return 3
            elif B < 20:
                if C > 50 and A < 50 and D < 50:
                    return 4
                else:
                    return 1
            elif D >= 90 and B > 60:
                return 3
            elif A > 70 and B < 40 and E > 70:
                return 3
            else:
                return 1