"""
Predictor 161
Generated on: 2025-09-09 20:33:55
Accuracy: 36.95%
"""


# PREDICTOR 161 - Accuracy: 36.95%
# Correct predictions: 3695/10000 (36.95%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                return 1
            else:
                if E < 20:
                    if D > 80:
                        return 4
                    else:
                        return 2
                elif C < 20:
                    return 2
                else:
                    return 4
        else:
            if E < 20:
                return 4
            else:
                return 2
    else:
        if C > 50:
            if E < 50:
                return 4
            else:
                if B > 70:
                    return 3
                else:
                    return 1
        else:
            if E < 20:
                return 1
            else:
                if A > 80 and D < 40 and E < 30:
                    return 1
                else:
                    return 3