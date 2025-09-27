"""
Predictor 174
Generated on: 2025-09-09 20:42:15
Accuracy: 53.36%
"""


# PREDICTOR 174 - Accuracy: 53.36%
# Correct predictions: 5336/10000 (53.36%)

def predict_output(A, B, C, D, E):
    m = max(A, B, C, D, E)
    if m == B:
        if C > 50:
            return 2
        elif max(D, E) > 50:
            return 4
        else:
            return 1
    elif m == C:
        if D >= 30:
            return 1
        else:
            if E > 50:
                return 1
            else:
                return 4
    elif m == D:
        if B > 80:
            if C > 50:
                return 1
            else:
                return 4
        elif B < 20:
            return 1
        else:
            if D > 80:
                if C < 20:
                    return 4
                else:
                    return 1
            else:
                return 3
    elif m == A:
        if D > 70:
            return 3
        else:
            return 1
    elif m == E:
        if E > 50:
            return 1
        else:
            return 3
    else:
        return 1