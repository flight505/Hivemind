"""
Predictor 297
Generated on: 2025-09-09 21:39:25
Accuracy: 39.30%
"""


# PREDICTOR 297 - Accuracy: 39.30%
# Correct predictions: 3930/10000 (39.30%)

def predict_output(A, B, C, D, E):
    if B >= 75:
        if C < 40:
            if D > 90 and E > 80:
                return 3
            elif D < 40 and E < 40:
                return 1
            else:
                return 4
        else:
            if D > 80 and E > 70:
                return 1
            else:
                return 2
    else:
        if C > 50:
            if E < 20:
                return 4
            elif D > 50 and E > 50:
                return 1
            else:
                return 3
        else:
            if E < 20:
                if D > 50:
                    return 1
                else:
                    if A > 50 and B > 60:
                        return 1
                    else:
                        return 3
            else:
                if D > 60:
                    if E > 50:
                        if B < 25:
                            return 1
                        else:
                            return 3
                    else:
                        return 3
                else:
                    if E > 50:
                        return 4
                    else:
                        if C < 5:
                            return 1
                        else:
                            return 3