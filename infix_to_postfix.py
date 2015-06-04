from stack import Stack
import re
from bracket_pairs import are_brackets_paired

class InfixExpression:
    def __init__(self, expression):
        self.__validate_length(expression)
        self.__validate_brackets(expression)
        self.__validate_characters(expression)
        self.expression = expression
        self.tokens = self.__parse_tokens(expression)
        self.__validate_operators(self.tokens)
    def to_postfix(self):
        return " ".join(self.__to_postfix_tokens())
    def evaluate(self):
        for character in self.expression:
            if character not in "+-*/() 0123456789":
                raise EvaluationCharactersError()
        tokens = self.__to_postfix_tokens()
        operands = Stack()
        for token in tokens:
            if token not in "+-*/":
                operands.push(float(token))
                continue
            operand2 = operands.pop()
            operand1 = operands.pop()
            if token == "+":
                operands.push(operand1 + operand2)
            elif token == "-":
                operands.push(operand1 - operand2)
            elif token == "*":
                operands.push(operand1 * operand2)
            elif token == "/":
                operands.push(operand1 / operand2)
        return operands.pop()
    def __to_postfix_tokens(self):
        postfix_expression = []
        operators = Stack()
        for token in self.tokens:
            if token not in "+-*/()":
                postfix_expression.append(token)
                continue
            if token == "(":
                operators.push(token)
            elif token == ")":
                while not operators.is_empty() and operators.peek() != "(":
                    postfix_expression.append(operators.pop())
                if not operators.is_empty():
                    operators.pop() # Pops the "("
            elif token in "+-":
                while not operators.is_empty() and operators.peek() in "+-*/":
                    postfix_expression.append(operators.pop())
                operators.push(token)
            elif token in "*/":
                while not operators.is_empty() and operators.peek() in "*/":
                    postfix_expression.append(operators.pop())
                operators.push(token)
        while not operators.is_empty():
            postfix_expression.append(operators.pop())
        return postfix_expression
    def __is_acceptable(self, character):
        asciii = ord(character)
        is_lower_case = asciii >= ord('a') and asciii <= ord('z')
        is_upper_case = asciii >= ord('A') and asciii <= ord('Z')
        is_digit = asciii >= ord('0') and asciii <= ord('9')
        is_underscore = asciii == ord('_')
        return is_lower_case or is_upper_case or is_digit or is_underscore
    def __parse_tokens(self, expression):
        tokens = []
        i = 0
        while i < len(expression):
            character = expression[i]
            if character == ' ':
                while character == ' ' and i < len(expression):
                    i += 1
                    if i < len(expression):
                        character = expression[i]
                continue
            if character in "+-*/()":
                tokens.append(character)
                i += 1
                continue
            if self.__is_acceptable(character):
                token = ""
                while self.__is_acceptable(character) and i < len(expression):
                    token += character
                    i += 1
                    if i < len(expression):
                        character = expression[i]
                tokens.append(token)
                continue
            raise InvalidInfixExpressionError()
        return tokens
    def __validate_length(self, expression):
        if len(expression) < 1:
            raise InvalidInfixExpressionError()
    def __validate_characters(self, expression):
        valid_characters = re.compile("^[a-zA-Z0-9_\s\+\*\-\/\(\)]+$")
        if not valid_characters.match(expression):
            raise InvalidInfixExpressionError()
    def __validate_operators(self, tokens):
        last_read = '+' # To make sure that a '(' or a variable comes first
        for token in tokens:
            if token == ' ':
                continue
            if token == '(':
                if last_read not in "+-*/(":
                    raise InvalidInfixExpressionError()
            elif token == ')':
                if last_read in "+-*/(":
                    raise InvalidInfixExpressionError()
            elif token in "+-*/":
                if last_read in "+-*/(":
                    raise InvalidInfixExpressionError()
            last_read = token
    def __validate_brackets(self, expression):
        if not are_brackets_paired(expression):
            raise InvalidInfixExpressionError()

class InvalidInfixExpressionError(Exception):
    pass

class EvaluationCharactersError(Exception):
    pass

import unittest
class InfixExpressionTest(unittest.TestCase):
    def test_to_postfix_invalid_expressions(self):
        # Invalid length
        with self.assertRaises(InvalidInfixExpressionError):
            InfixExpression("")
        # Invalid brackets
        with self.assertRaises(InvalidInfixExpressionError):
            InfixExpression("())(")
        # Invalid characters
        with self.assertRaises(InvalidInfixExpressionError):
            InfixExpression("abc. + 23 - 19 *()")
        # Invalid operators
        with self.assertRaises(InvalidInfixExpressionError):
            InfixExpression("+ 23 - 19 * ()")
    def test_to_postfix_valid_expressions(self):
        # Test 1
        infix_expression = InfixExpression("x * y / (5 * z) + 10")
        expected = "x y * 5 z * / 10 +"
        actual = infix_expression.to_postfix()
        self.assertEqual(expected, actual)
        # Test 2
        infix_expression = InfixExpression("(4+8)*(6-5)/((3-2)*(2+2)) ")
        expected = "4 8 + 6 5 - * 3 2 - 2 2 + * /"
        actual = infix_expression.to_postfix()
        self.assertEqual(expected, actual)
        # Test 3
        infix_expression = InfixExpression("4+8/7*8")
        expected = "4 8 7 / 8 * +"
        actual = infix_expression.to_postfix()
        self.assertEqual(expected, actual)
    def test_evaluate_invalid_expressions(self):
        infix_expression = InfixExpression("x * y / (5 * z) + 10")
        with self.assertRaises(EvaluationCharactersError):
            infix_expression.evaluate()
    def test_evaluate_valid_expressions(self):
        infix_expression = InfixExpression("(4+8)*(6-5)/((3-2)*(2+2)) ")
        expected = 3
        actual = infix_expression.evaluate()
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
