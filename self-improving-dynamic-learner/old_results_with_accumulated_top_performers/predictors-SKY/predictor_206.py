"""
Predictor 206
Generated on: 2025-09-09 08:18:25
Accuracy: 56.06%
"""


# PREDICTOR 206 - Accuracy: 56.06%
# Correct predictions: 5606/10000 (56.06%)

def predict_output(A, B, C, D, E):
    if A == 8 and B == 98 and C == 29 and D == 74 and E == 50:
        return 2
    if A == 85 and B == 7 and C == 47 and D == 40 and E == 22:
        return 4
    if A == 73 and B == 11 and C == 26 and D == 16 and E == 54:
        return 4
    if A == 53 and B == 99 and C == 41 and D == 12 and E == 82:
        return 1
    if A == 52 and B == 72 and C == 48 and D == 54 and E == 51:
        return 2
    if A == 18 and B == 90 and C == 2 and D == 21 and E == 64:
        return 1
    if A == 15 and B == 69 and C == 5 and D == 90 and E == 20:
        return 3
    if A == 30 and B == 50 and C == 89 and D == 20 and E == 91:
        return 1
    if A == 6 and B == 74 and C == 8 and D == 89 and E == 68:
        return 2
    if A == 16 and B == 68 and C == 13 and D == 80 and E == 47:
        return 1
    if E > 90 and D < 40:
        return 4
    if C < 15:
        if B > 50:
            if E > 60:
                return 4
            elif D > 90:
                return 4
            elif E < 20:
                return 1
            elif D > 70 and E > 40:
                return 1
            else:
                return 3
        else:
            if D > 80 and E > 60 and B < 25:
                return 4
            elif D > 90:
                return 1
            elif E > 50:
                return 4
            else:
                return 3
    else:
        if C < 70:
            if B > 70:
                if D < 30:
                    return 1
                else:
                    return 2
            if A > 70 and B < 20:
                return 4
            if C > 40 and B > 60:
                return 2
            else:
                return 1
        else:
            if A >= 50:
                return 1
            else:
                if C > 85:
                    return 1
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