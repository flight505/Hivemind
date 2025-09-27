"""
Predictor 76
Generated on: 2025-09-09 19:45:42
Accuracy: 52.49%
"""


# PREDICTOR 76 - Accuracy: 52.49%
# Correct predictions: 5249/10000 (52.49%)

def predict_output(A, B, C, D, E):
    if C > 50:
        if B >= 80:
            if D < 50:
                return 2
            else:
                if E <= 25 or A > 60:
                    return 1
                else:
                    return 2
        else:
            if E < 20:
                if B >= 70:
                    return 2
                else:
                    if A > 90 or D > 50:
                        return 1
                    else:
                        return 4
            else:
                if D < 20:
                    if A < 50:
                        return 2
                    else:
                        return 4
                else:
                    if B >= 75:
                        return 2
                    else:
                        return 1
    else:
        if B >= 80:
            if D < 40:
                if E > 50:
                    return 4
                else:
                    return 1
            else:
                if E < 20:
                    if A < 20:
                        return 1
                    else:
                        return 4
                elif E > 50:
                    return 4
                else:
                    return 2
        else:
            if E < 20:
                if D > 50:
                    if B > 50:
                        return 3
                    else:
                        return 1
                else:
                    return 3
            else:
                if D > 50:
                    if E <= 40:
                        return 1
                    elif B < 40:
                        return 3
                    else:
                        return 3
                elif E > 45 and D < 40:
                    return 4
                else:
                    if C > 20:
                        return 1
                    else:
                        return 3