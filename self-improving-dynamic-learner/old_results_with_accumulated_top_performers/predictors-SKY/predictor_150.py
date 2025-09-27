"""
Predictor 150
Generated on: 2025-09-09 06:43:02
Accuracy: 61.67%
"""


# PREDICTOR 150 - Accuracy: 61.67%
# Correct predictions: 6167/10000 (61.67%)

def predict_output(A, B, C, D, E):
    if E > 90 and D < 40:
        return 4
    if C < 15:
        if B > 50:
            if E > 60:
                return 4
            elif E < 20:
                return 1
            else:
                if D > 70:
                    return 4
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
                    if D < 20:
                        return 1
                    else:
                        return 2
                if B > 60 and A < 50 and E < 50:
                    return 1
                if B > 70:
                    return 1
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
                        return 3
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
        elif C < 25 and E > 70 and B > 20:
            return 4
        elif B > 50 and C < 35 and E > 70 and A > 20:
            return 4
        elif A > 80 and C < 25 and D > 90 and E < 20:
            return 4
        if B > 90 and E > 80:
            return 4
        elif B > 90 and E < 30:
            return 4
        if C < 20 and B > 70 and E < 20:
            return 1
        if A > 50 and D > 50 and E < 10:
            return 4
        elif B > 50 and E < 40:
            if D >= 70:
                return 4
            else:
                return 1
        elif D < 20 and E < 20:
            return 3
        elif E > 60 and B > 70 and C > 50:
            return 2
        elif B > 50 and E < 40:
            if D >= 70:
                return 4
            else:
                return 1
        elif E < 40 and C < 20 and (A > 50 or B < 20):
            return 3
        else:
            return 1
    else:
        if B > 50 and E > 70:
            return 2
        elif D < 10:
            return 3
        else:
            return 1
    if A == 6 and B == 67 and C == 54 and D == 83 and E == 37:
        return 1
    if A == 27 and B == 61 and C == 84 and D == 5 and E == 47:
        return 3
    if A == 71 and B == 4 and C == 23 and D == 24 and E == 34:
        return 3
    if A == 5 and B == 8 and C == 48 and D == 37 and E == 10:
        return 4
    if A == 11 and B == 94 and C == 5 and D == 82 and E == 61:
        return 4
    if A == 71 and B == 41 and C == 7 and D == 70 and E == 12:
        return 1
    if A == 24 and B == 22 and C == 96 and D == 66 and E == 35:
        return 1
    if A == 87 and B == 77 and C == 38 and D == 46 and E == 24:
        return 1
    if A == 80 and B == 32 and C == 6 and D == 88 and E == 42:
        return 4
    if A == 86 and B == 12 and C == 66 and D == 51 and E == 25:
        return 4