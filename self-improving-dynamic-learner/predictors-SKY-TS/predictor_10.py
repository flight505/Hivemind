"""
Predictor 10
Generated on: 2025-09-09 19:00:54
Accuracy: 43.91%
"""


# PREDICTOR 10 - Accuracy: 43.91%
# Correct predictions: 4391/10000 (43.91%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D <= 35:
                return 1
            else:
                return 4
        else:
            if D < 50:
                return 1
            elif D < 80:
                if B - C > 20:
                    return 2
                else:
                    return 3
            else:
                return 3
    else:
        if C > 50:
            if E < 20:
                if D < 25:
                    return 4
                else:
                    return 1
            else:
                if A + B >= 120:
                    return 2
                else:
                    return 1
        else:
            if E < 20:
                return 1
            else:
                if D > 50 or C < 20:
                    return 3
                else:
                    if D < 40:
                        return 4
                    else:
                        return 1