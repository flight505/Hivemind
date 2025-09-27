"""
Predictor 71
Generated on: 2025-09-09 19:43:32
Accuracy: 54.48%
"""


# PREDICTOR 71 - Accuracy: 54.48%
# Correct predictions: 5448/10000 (54.48%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C >= 50:
            if E < 40:
                return 3
            elif A > 60:
                return 1
            else:
                return 2
        else:
            if D < 40:
                return 1
            else:
                return 4
    else:
        if C >= 50:
            if D + E > 100 or A > 70:
                return 1
            else:
                return 4
        else:
            if D > 50:
                if E < 30:
                    return 1
                else:
                    if C < 25 and B > 55:
                        return 4
                    else:
                        return 3
            else:
                if B >= 65:
                    return 1
                elif E > 50:
                    return 4
                elif E < 20:
                    return 1
                else:
                    return 3