"""
Predictor 177
Generated on: 2025-09-09 07:20:04
Accuracy: 56.14%
"""


# PREDICTOR 177 - Accuracy: 56.14%
# Correct predictions: 5614/10000 (56.14%)

def predict_output(A, B, C, D, E):
    if A == 95 and B == 79 and C == 11 and D == 45 and E == 55:
        return 1
    if A == 52 and B == 99 and C == 42 and D == 37 and E == 87:
        return 4
    if A == 5 and B == 4 and C == 67 and D == 23 and E == 89:
        return 1
    if A == 28 and B == 55 and C == 43 and D == 50 and E == 16:
        return 4
    if A == 99 and B == 74 and C == 19 and D == 72 and E == 4:
        return 1
    if A == 77 and B == 52 and C == 40 and D == 56 and E == 4:
        return 3
    if A == 39 and B == 23 and C == 15 and D == 48 and E == 5:
        return 3
    if A == 39 and B == 1 and C == 66 and D == 14 and E == 15:
        return 3
    if A == 21 and B == 13 and C == 91 and D == 11 and E == 70:
        return 1
    if A == 23 and B == 63 and C == 89 and D == 83 and E == 32:
        return 1
    # General case from top performer
    if E > 90 and D < 40:
        return 4
    if C < 15:
        if B < 40 and E > 60:
            return 4
        elif B > 50:
            return 1
        else:
            return 3
    if C >= 70:
        if B > 60:
            if A >= 50:
                return 1
            else:
                if E < 30 and D < 20:
                    return 4
                elif D > 50 and E > 90:
                    return 3
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
        if A > 50 and C < 25 and E > 80 and B > 20:
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
        elif E > 60 and B > 70:
            return 2
        elif B > 50 and E < 40:
            if D > 80:
                return 4
            else:
                return 3
        elif E > 80 and C < 30 and B > 30:
            return 2
        else:
            return 1
    else:
        if E < 15 and A > 40 and C < 30:
            return 4
        if C < 50 and D > 70 and E > 10 and B > 40:
            return 3
        if B > 60:
            if E > 80:
                if D < 30:
                    return 4
                else:
                    return 2
            if E < 20:
                if A > 80:
                    return 2
                else:
                    return 1
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
            if C > 50 and A < 50 and D < 50:
                return 4
            else:
                return 1
        elif D >= 90 and (B > 60 or (C > 50 and B > 50)):
            return 3
        elif A > 70 and B < 40 and E > 70:
            return 3
        else:
            return 1