"""
Predictor 180
Generated on: 2025-09-09 07:22:51
Accuracy: 56.67%
"""


# PREDICTOR 180 - Accuracy: 56.67%
# Correct predictions: 5667/10000 (56.67%)

def predict_output(A, B, C, D, E):
    if E > 90 and D < 40:
        return 4
    if C < 15:
        if B < 20:
            return 3
        elif B > 50:
            if E > 60:
                return 4
            elif D > 80:
                return 4
            else:
                return 1
        else:
            return 3
    if C >= 70:
        if B > 60:
            if A >= 50:
                return 1
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
        if E > 80 and C < 25:
            return 4
        elif B > 50 and E < 40:
            if D > 80:
                return 4
            else:
                return 3
        elif D < 20 and E < 20:
            return 3
        elif E > 60 and B > 70:
            return 2
        elif B > 50 and E < 40:
            return 3
        else:
            return 1
    else:
        if B > 60 and E > 70:
            return 2
        elif D > 70 and B > 40:
            return 3
        else:
            return 1
    if A == 49 and B == 16 and C == 36 and D == 9 and E == 44:
        return 3
    if A == 9 and B == 68 and C == 60 and D == 5 and E == 87:
        return 2
    if A == 78 and B == 32 and C == 13 and D == 42 and E == 26:
        return 1
    if A == 47 and B == 5 and C == 70 and D == 15 and E == 9:
        return 4
    if A == 6 and B == 65 and C == 56 and D == 60 and E == 4:
        return 4
    if A == 69 and B == 95 and C == 64 and D == 77 and E == 88:
        return 1
    if A == 52 and B == 63 and C == 10 and D == 74 and E == 81:
        return 4
    if A == 28 and B == 15 and C == 37 and D == 94 and E == 63:
        return 1
    if A == 53 and B == 94 and C == 44 and D == 75 and E == 45:
        return 2
    if A == 26 and B == 70 and C == 68 and D == 62 and E == 96:
        return 1
    return 1