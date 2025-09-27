"""
Predictor 51
Generated on: 2025-09-09 04:17:29
Accuracy: 49.44%
"""


# PREDICTOR 51 - Accuracy: 49.44%
# Correct predictions: 4944/10000 (49.44%)

def predict_output(A, B, C, D, E):
    if E > 90 and D < 40 and C < 30:
        return 4
    if C >= 70:
        if D < 30:
            if B > 50:
                if A < 50:
                    return 2
                else:
                    return 1
            else:
                return 4
        if E < 30 and B < 50:
            if E > 20:
                return 4
            else:
                return 1
        if A < 50:
            return 2
        else:
            return 1
    if C < 30:
        if B > 70:
            return 1
        if D > 80 and E < 20:
            if A > 80:
                return 4
            else:
                return 1
        if E > 60 and A < 20:
            return 2
        if E > 60 and D < 20:
            return 1
        if A > 90 and E < 10:
            return 1
        return 3
    # 30 <= C < 70
    if D > 80:
        if B > 70:
            if C >= 50:
                return 3
            else:
                return 2
        elif E < 20:
            return 3
        else:
            return 1
    if D > 70 and B < 20:
        return 3
    if E < 30 and D < 60 and B < 50:
        return 4
    if B > 80 and E < 20 and D > 50:
        return 2
    if B > 60 and E > 70 and C < 50:
        return 2
    if A < 15 and B < 50 and E > 50:
        return 2
    return 1