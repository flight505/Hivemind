"""
Predictor 299
Generated on: 2025-09-09 21:39:25
Accuracy: 40.33%
"""


# PREDICTOR 299 - Accuracy: 40.33%
# Correct predictions: 4033/10000 (40.33%)

def predict_output(A, B, C, D, E):
    if B >= 70:
        if C >= 50:
            if D + E > 150:
                return 1
            else:
                return 2
        else:
            if D > 90 and E > 80:
                return 3
            elif D < 40:
                return 1
            else:
                return 4
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
                if D > 50 or (A > 70 and B > 30):
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
                        if C < 10:
                            return 1
                        else:
                            return 3