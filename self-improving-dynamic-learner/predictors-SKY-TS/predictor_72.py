"""
Predictor 72
Generated on: 2025-09-09 19:43:32
Accuracy: 49.66%
"""


# PREDICTOR 72 - Accuracy: 49.66%
# Correct predictions: 4966/10000 (49.66%)

def predict_output(A, B, C, D, E):
    if B >= 75:
        if C >= 50:
            if A > 60:
                return 1
            elif E < 40:
                return 3
            else:
                return 2
        else:
            if D < 40:
                return 1
            else:
                return 4
    else:
        if C >= 50:
            if D < 40:
                return 4
            else:
                return 1
        else:
            if D > 50:
                if E > 70:
                    if A > 50:
                        return 4
                    else:
                        return 3
                elif A > 90 and D > 80:
                    return 4
                elif B > 60 and D > 55 and E > 65:
                    return 4
                elif B < 20:
                    return 1
                else:
                    return 3
            else:
                if B < 20 and D < 20 and E > 55:
                    return 4
                elif B > 60 and D < 30 and E > 50:
                    return 1
                else:
                    return 3