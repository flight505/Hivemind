"""
Predictor 6
Generated on: 2025-09-09 17:08:25
Accuracy: 49.02%
"""


# PREDICTOR 6 - Accuracy: 49.02%
# Correct predictions: 4902/10000 (49.02%)

def predict_output(A, B, C, D, E):
    if E > 90:
        return 4
    if C >= 75:
        if A > 50 or E > 80:
            return 1
        else:
            return 2
    if A < 5 and C > 65:
        return 4
    if B < 20:
        if C < 20:
            return 3
        else:
            if E < 20:
                return 4
            else:
                if C > 70:
                    return 4
                elif A > 70:
                    return 4
                elif D < 15:
                    return 3
                elif A < 10:
                    return 2
                else:
                    return 1
    if C < 40:
        if D > 50 or (E >= 60 and A < 50) or B > 30:
            return 1
        else:
            if C > 30:
                return 4
            else:
                return 3
    else:
        if B > 50 and C > 50 and D < 30 and E < 50:
            return 4
        if B < 30 and D < 30 and C < 50:
            return 4
        if C < 50 and B > 50 and D < 60 and E < 50:
            return 2
        if B > 50 and D > 65 and C < 40:
            return 3
        else:
            return 1