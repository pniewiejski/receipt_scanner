"""
Assert functionalities - test whether image has been pre processed correctly
"""

def assert_area_ratio(before, after) -> bool:
    """
    `before` - image before preprocessing

    `after` - image after preprocessing

    Returns `True` if OK
    """
    # I know it's stupid,
    # but I do not have a better idea for the moment... 
    # maybe I'll refactor it later 
    RATIO = 0.1
    h1, w1, _ = before.shape
    h2, w2, _ = after.shape
    return (h2 * w2) / (h1 * w1) > RATIO
        