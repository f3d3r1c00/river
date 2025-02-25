from .numeric_attribute_regression_observer import NumericAttributeRegressionObserver


class NumericAttributeRegressionTruncatedObserver(NumericAttributeRegressionObserver):
    """Truncated E-BST.

    Variation of E-BST that rounds the incoming feature values before passing them to the binary
    search tree (BS). By doing so, the attribute observer might reduce its processing time and
    memory usage since small variations in the input values will end up being mapped to the same
    BST node.

    Parameters
    ----------
    digits
        The number of decimal places used to round the input feature values.

    """

    def __init__(self, digits: int = 3):
        super().__init__()
        self.digits = digits

    def update(self, att_val, target_val, sample_weight):
        try:
            att_val = round(att_val, self.digits)
            super().update(att_val, target_val, sample_weight)
        except TypeError:  # feature value is None
            return

    def probability_of_attribute_value_given_class(self, att_val, class_val):
        raise NotImplementedError
