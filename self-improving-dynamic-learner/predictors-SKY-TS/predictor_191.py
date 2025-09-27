"""
Predictor 191
Generated on: 2025-09-09 20:50:39
Accuracy: 47.18%
"""


# PREDICTOR 191 - Accuracy: 47.18%
# Correct predictions: 4718/10000 (47.18%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                if E > 50:
                    return 4
                else:
                    return 1
            else:
                if E < 20:
                    if A < 30:
                        return 1
                    else:
                        return 4
                else:
                    if D > 80:
                        return 2
                    else:
                        return 4
        else:
            if D < 50:
                return 1
            else:
                if E < 20:
                    return 1
                elif D > 90:
                    if E > 70:
                        return 1
                    else:
                        return 3
                elif D < 30:
                    return 4
                else:
                    return 2
    else:
        if C >= 50:
            if D < 50:
                if A > 50:
                    return 3
                else:
                    return 4
            else:
                if E > 80:
                    return 1
                else:
                    return 1
        else:
            if E > 70:
                if B < 50:
                    return 4
                else:
                    return 2
            elif B > 60 and C > 40:
                return 2
            elif A > 50 and E < 50:
                return 1
            else:
                return 3