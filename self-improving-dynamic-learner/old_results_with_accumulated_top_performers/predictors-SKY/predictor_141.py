"""
Predictor 141
Generated on: 2025-09-09 06:23:29
Accuracy: 41.56%
"""


# PREDICTOR 141 - Accuracy: 41.56%
# Correct predictions: 4156/10000 (41.56%)

def predict_output(A, B, C, D, E):
    if E > 90 and D < 40 and C < 40:
        return 4
    if C >= 70:
        if B > 60 and A >= 50:
            return 1
        elif B < 30 and D < 30 and E > 50:
            return 4
        elif B < 50 and E < 30:
            if A > 80:
                return 1
            else:
                return 4
        else:
            return 2
    if C < 40:
        if B > 50:
            if E > 70:
                return 2
            elif E < 20:
                return 3
            else:
                return 1
        if E > 80:
            if D > 20:
                return 4
            else:
                return 1
        if E > 60 and B < 20:
            return 2
        if D > 90 and E < 20 and C > 15:
            return 1
        return 3
    # 40 <= C < 70
    if B > 60:
        if E > 80:
            if A >= 50 and D > 80:
                return 3
            else:
                return 1
        if E < 20:
            if A > 80:
                return 2
            else:
                return 1
        if A > 70 and C < 50:
            return 2
        elif C > 60:
            if A < 50:
                if D < 10:
                    return 1
                else:
                    return 2
            else:
                return 1
        else:
            if D < 20:
                return 1
            else:
                return 3
    elif B < 20:
        if C > 50 and A < 50 and D < 50:
            return 4
        else:
            return 1
    else:
        if E < 30 and C > 50 and A < 30:
            return 4
        else:
            return 1