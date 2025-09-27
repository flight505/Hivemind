"""
Predictor 291
Generated on: 2025-09-09 21:35:39
Accuracy: 47.28%
"""


# PREDICTOR 291 - Accuracy: 47.28%
# Correct predictions: 4728/10000 (47.28%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                return 1
            else:
                if E < 20:
                    return 4
                elif E > 60 and D < 80:
                    return 2
                else:
                    return 4
        else:
            return 2
    else:
        if C >= 50:
            if E < 20:
                return 4
            elif E > 70 and D <= 40:
                if A > 50 or B > 65:
                    return 4
                else:
                    return 2
            else:
                return 1
        else:
            if E < 20:
                if D > 50:
                    return 1
                else:
                    return 3
            else:
                if E > 70:
                    if C < 10:
                        return 2
                    else:
                        return 4
                elif D < 50 and E > 60:
                    if C < 30:
                        return 4
                    else:
                        return 1
                else:
                    return 3