"""
Predictor 258
Generated on: 2025-09-09 21:22:33
Accuracy: 50.91%
"""


# PREDICTOR 258 - Accuracy: 50.91%
# Correct predictions: 5091/10000 (50.91%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if E < 20:
                return 4 if D >= 50 else 1
            else:
                return 4 if C + E < 70 else 2
        else:
            return 1 if E < 30 or A > 50 else 2
    else:
        if C > 50:
            sum_ade = A + D + E
            if sum_ade > 120 or B > 40:
                return 1
            else:
                return 4 if E > 60 else 3
        else:
            if E < 20:
                return 1 if D > 40 else 4
            elif E > 80:
                return 4
            else:
                if A + C > 100:
                    return 1
                elif D < 20:
                    return 3
                else:
                    return 3 if B < 30 else 2