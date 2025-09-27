"""
Predictor 293
Generated on: 2025-09-09 21:37:20
Accuracy: 48.60%
"""


# PREDICTOR 293 - Accuracy: 48.60%
# Correct predictions: 4860/10000 (48.60%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C > 50:
            return 2
        else:
            if D < 40:
                return 1
            else:
                return 4
    else:
        if C > 50:
            if E < 20:
                return 4
            else:
                return 1
        else:
            if E < 20:
                if B > 70:
                    return 1
                elif A > 50:
                    return 1
                else:
                    return 3
            else:
                if D > 90:
                    return 1
                elif E > 90:
                    return 4
                elif B < 40 and A > 90:
                    return 4
                elif D < 10:
                    if E > 80:
                        return 1
                    else:
                        return 3
                else:
                    return 3