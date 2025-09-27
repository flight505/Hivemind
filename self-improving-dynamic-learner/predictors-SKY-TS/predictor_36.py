"""
Predictor 36
Generated on: 2025-09-09 19:16:43
Accuracy: 47.68%
"""


# PREDICTOR 36 - Accuracy: 47.68%
# Correct predictions: 4768/10000 (47.68%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                return 1
            else:
                return 4
        else:
            if D > 80 or E > 80:
                return 1
            else:
                return 2
    else:
        if C > 50:
            if E < 30:
                return 4
            else:
                if D < 10:
                    return 2
                else:
                    return 1
        else:
            if E < 20:
                if D > 80:
                    return 4
                else:
                    return 1
            else:
                if D > 70:
                    if E > 90 or (C > 40 and E < 40):
                        return 1
                    else:
                        return 3
                elif E > 50 and D < 30:
                    if A > 40:
                        return 1
                    else:
                        return 2
                elif B >= 75 and C < 20:
                    return 4
                else:
                    return 3