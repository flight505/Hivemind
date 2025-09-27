"""
Predictor 312
Generated on: 2025-09-09 21:44:46
Accuracy: 42.91%
"""


# PREDICTOR 312 - Accuracy: 42.91%
# Correct predictions: 4291/10000 (42.91%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C >= 50:
            if D < 40:
                return 1
            else:
                return 2
        else:
            if D < 30:
                return 1
            elif A > 60:
                return 3
            else:
                return 4
    else:
        if C >= 50:
            if E > 50:
                return 1
            elif E > 20:
                return 3
            else:
                return 4
        else:
            if E < 20:
                if D > 50:
                    return 1
                else:
                    return 3
            else:
                if D > 50:
                    if A < 20:
                        return 1
                    else:
                        return 3
                else:
                    if E > 60 and D < 40:
                        return 2
                    elif D < 20 and E > 30:
                        return 3
                    else:
                        return 4