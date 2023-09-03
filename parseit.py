from tokenizer import Tokenizer
from  expression import UnaryOperatorExpression, NumericExpression, Expression, VariableExpression

"""
term = ("+" | "-")+ (number | variable)
sum = term (("+" term) | ("-" term))*
expression = sum END
"""
    
class Parser:
    
    def __init__(self):
        self.tokenizer = Tokenizer()
        
    def parse(self, line):
        self.tokenizer.new_line(line)
        return self.expression()
        
    def term(self):
        self.tokenizer.mark()
        unary_operator = None
        expression = None
        
        # handle unary + or -     
        if self.tokenizer.is_character('-') != None:
            unary_operator = '-'
        elif self.tokenizer.is_character('+') != None:
            unary_operator = '+'
            
        # handle constant
        number = self.tokenizer.is_number()
        if number != None:
            expression = NumericExpression(number)
        else:    
            # handle variable
            variable = self.tokenizer.is_variable()
            if variable != None:
                expression =  VariableExpression(variable)
        
        if expression != None and unary_operator != None:
            return UnaryOperatorExpression(unary_operator, expression)
        
        elif expression != None:
            return expression

        self.tokenizer.restore()
        return None
            
    def sum(self):
        self.tokenizer.mark()
        
        lhs = self.term()
        if lhs == None:
            self.tokenizer.restore()
            return None
            
        # look for more terms
        while True:
            # we have a - or + sign
            operator = self.tokenizer.is_character('-')
            if operator == None:
                operator = self.tokenizer.is_character('+')
            
            if operator == None:     
                return lhs
            
            # we should have a term next
            rhs = self.term()
            if rhs == None:
                self.tokenizer.restore()
                return None
            
            # we now have a lhs <operator> rhs -- put into an expression and point lhs at it
            lhs = Expression(lhs, operator, rhs)
            
        return lhs
            
    def expression(self):
        self.tokenizer.mark()
        lhs = self.sum()
        
        # should have a sum followed by end of line
        if lhs == None or not self.tokenizer.is_end():
            self.tokenizer.restore()
            return None
        
        return lhs
