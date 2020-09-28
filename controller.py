from functools import partial
ERROR_MSG = 'ERROR'


class Controller:
#"""Controller for calculator."""
    def __init__(self, model, view):
        #"""Controller initializer."""
        self._evaluate = model
        self._view 	   = view
        # Connect signals and slots
        self._connectSignals()


        def _buildExpression(self, sub_exp):
        #"""Build expression."""
        if self._view.getDisplayText() == ERROR_MSG:
            self._view.clearDisplay()

        expression = self._view.getDisplayText() + sub_exp  1+2
        self._view.setDisplayText(expression)


        def _connectSignals(self):
        #"""Connect signals and slots."""
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'=', 'C'}:
                btn.clicked.connect(partial(self._buildExpression, btnText))


         def _calculateResult(self):
        #"""Evaluate expressions."""
        result = self._evaluate(expression=self._view.getDisplayText())
        self._view.setDisplayText(result)

        self._view.buttons['='].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttons['C'].clicked.connect(self._view.clearDisplay)