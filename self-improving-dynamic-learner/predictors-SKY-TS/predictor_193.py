"""
Predictor 193
Generated on: 2025-09-09 20:54:12
Accuracy: 47.79%
"""


# PREDICTOR 193 - Accuracy: 47.79%
# Correct predictions: 4779/10000 (47.79%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                return 1
            else:
                if E > 60:
                    return 1
                elif A > 40 and E < 25:
                    return 2
                else:
                    return 4
        else:
            if D < 50 or A < 30:
                return 1
            else:
                return 2
    else:
        if C > 50:
            if E < 20:
                if D > 50:
                    return 1
                else:
                    return 4
            else:
                if D < 30 and E > 40:
                    return 4
                elif D < 20 or A < 10:
                    return 3
                else:
                    return 1
        else:
            if E < 20:
                if D < 50:
                    return 4
                else:
                    return 1
            else:
                if A < 50 and C < 10:
                    return 4
                elif A > 80 and D < 25 and E > 70:
                    return 4
                elif D < 20 and E > 60 and A < 20:
                    return 2
                elif D < 40 and E < 35:
                    return 1
                elif D > 50 and E > 50 and A < 60:
                    return 1
                else:
                    return 3