"""
Predictor 298
Generated on: 2025-09-09 21:39:25
Accuracy: 37.00%
"""


# PREDICTOR 298 - Accuracy: 37.00%
# Correct predictions: 3700/10000 (37.00%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C >= 50:
            return 2
        else:
            if D > 90 and E > 80:
                return 3
            elif E < 20:
                if D > 50:
                    return 4
                else:
                    return 1
            else:
                return 4
    else:
        if C > 50:
            if D > 50 and E > 50:
                return 1
            elif E < 20:
                return 4
            else:
                return 3
        else:
            if E < 20:
                if D > 50:
                    return 1
                else:
                    if B > 60:
                        if D < 10:
                            return 3
                        else:
                            return 1
                    else:
                        return 3
            else:
                if D > 50:
                    if B < 20:
                        return 1
                    else:
                        return 3
                else:
                    if B >= 70:
                        return 1
                    elif E > 50 and D < 30:
                        return 4
                    elif A > 90:
                        return 1
                    else:
                        return 3