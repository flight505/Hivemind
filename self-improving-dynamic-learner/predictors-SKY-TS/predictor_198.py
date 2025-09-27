"""
Predictor 198
Generated on: 2025-09-09 20:55:47
Accuracy: 48.40%
"""


# PREDICTOR 198 - Accuracy: 48.40%
# Correct predictions: 4840/10000 (48.40%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                return 1
            else:
                return 4
        else:
            if E < 40:
                return 1
            else:
                return 2
    else:
        if C > 50:
            if E < 20:
                if A > 50:
                    return 1
                else:
                    return 4
            else:
                return 1
        else:
            if D > 50 and E < 40:
                if B < 30:
                    return 1
                elif C > 30:
                    return 4
                else:
                    if B > 55:
                        return 3
                    else:
                        return 4
            elif D > 50 and E > 80:
                return 2
            else:
                return 3