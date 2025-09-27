"""
Predictor 33
Generated on: 2025-09-09 19:16:43
Accuracy: 47.62%
"""


# PREDICTOR 33 - Accuracy: 47.62%
# Correct predictions: 4762/10000 (47.62%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D + E < 50:
                return 1
            else:
                return 4
        else:
            if D > 80:
                return 1
            else:
                return 2
    else:
        if C > 50:
            if D > 50:
                return 1
            elif E > 50:
                if D < 20:
                    return 2
                else:
                    return 1
            else:
                return 4
        else:
            if E < 20:
                if B < 30:
                    return 1
                else:
                    return 4
            else:
                if B >= 70:
                    return 4
                else:
                    if D >= 50:
                        if C >= 35:
                            return 1
                        else:
                            return 3
                    else:
                        if B > 50:
                            return 1
                        elif C > 25:
                            return 2
                        else:
                            return 3