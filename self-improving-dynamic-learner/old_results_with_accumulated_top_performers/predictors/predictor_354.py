"""
Predictor 354
Generated on: 2025-09-09 09:28:11
Accuracy: 32.04%
"""


# PREDICTOR 354 - Accuracy: 32.04%
# Correct predictions: 3204/10000 (32.04%)

def predict_output(A, B, C, D, E):
    values = [A, B, C, D, E]
    if max(values) > 90:
        return 4
    min_val = min(values)
    min_pos = values.index(min_val) + 1  # 1-based position: 1=A, 2=B, 3=C, 4=D, 5=E
    if min_pos == 3:  # C is min
        return 3
    elif min_pos == 5:  # E is min
        return 1
    elif min_pos == 4:  # D is min
        if B > 70:
            return 1
        else:
            return 2
    elif min_pos == 1:  # A is min
        if C > 50:
            return 2
        else:
            return 1
    else:  # B is min
        return 1