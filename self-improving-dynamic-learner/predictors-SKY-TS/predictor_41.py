"""
Predictor 41
Generated on: 2025-09-09 19:25:48
Accuracy: 53.72%
"""


# PREDICTOR 41 - Accuracy: 53.72%
# Correct predictions: 5372/10000 (53.72%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                if E > 30:
                    return 4
                else:
                    return 1
            else:
                if D + E > 100:
                    return 4
                else:
                    return 2
        else:
            if D < 50:
                return 1
            else:
                return 2
    else:
        if C > 50:
            if E < 20:
                return 4
            else:
                return 1
        else:
            if E < 20:
                if D > 50:
                    return 1
                else:
                    return 2
            else:
                if E > 80:
                    return 4
                elif E < 30:
                    return 1
                else:
                    if B < 30:
                        if D < 50:
                            if E > 60:
                                return 4
                            else:
                                return 3
                        else:
                            return 1
                    else:
                        if D > 50:
                            return 3
                        else:
                            return 1