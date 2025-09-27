"""
Predictor 129
Generated on: 2025-09-09 20:17:06
Accuracy: 47.02%
"""


# PREDICTOR 129 - Accuracy: 47.02%
# Correct predictions: 4702/10000 (47.02%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                return 1
            else:
                if A > 80:
                    return 2
                elif E > 80:
                    return 1
                else:
                    return 4
        else:
            return 2
    else:
        if C > 50:
            if E < 20:
                return 4
            else:
                if D < 20:
                    return 3
                elif B > 65:
                    return 2
                else:
                    return 1
        else:
            if E < 20:
                return 1
            else:
                if B > 30 and C > 20 and E < 70 and D < 60:
                    return 1
                elif D > 70:
                    return 3
                elif E > 60:
                    return 4
                else:
                    return 3