"""
Predictor 143
Generated on: 2025-09-09 20:24:26
Accuracy: 49.75%
"""


# PREDICTOR 143 - Accuracy: 49.75%
# Correct predictions: 4975/10000 (49.75%)

def predict_output(A, B, C, D, E):
    if B >= 70:
        if C > 50:
            if D > 30 and E > 30 and A < 50:
                return 2
            else:
                return 1
        else:
            if D < 30:
                if E < 20:
                    return 1
                else:
                    return 4
            else:
                return 4
    else:
        if C > 50:
            if D > 40:
                return 1
            elif E > 50:
                return 2
            else:
                if A > 20 and E < 20:
                    return 4
                else:
                    return 3
        else:
            if E < 20:
                if D > 50:
                    if A > 50 or B > 20:
                        return 1
                    else:
                        return 3
                else:
                    return 3
            else:
                if D > 60 and E > 40:
                    return 1
                else:
                    return 3