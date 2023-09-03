
class Expression:
    variables = {'a': 42,'b': -999, 'one': 1}
    
    def __init__(self, lhs, operator, rhs):
        self.lhs = lhs
        self.rhs = rhs
        self.operator = operator
    
    def tree_view(self):
        return self.lhs.tree_view() + ' ' + self.operator + ' ' + self.rhs.tree_view()
        
    def evaluate(self):
        lhs = self.lhs.evaluate()
        rhs = self.rhs.evaluate()
        
        match self.operator:
            case '+':
                return lhs + rhs
            
            case '-':
                return lhs - rhs
            
            case '/':
                return lhs // rhs
            
            case '*':
                return lhs * rhs
            
            case _:
                raise ValueError('Unknown binary operator')
    
    
class UnaryExpression(Expression):
    def __init__(self, operator, rhs):
        self.rhs = rhs
        self.operator = operator
        
    def tree_view(self):
        return self.operator + ' ' + self.rhs.tree_view()
    
    def evaluate(self):
        rhs = self.rhs.evaluate()
        
        match self.operator:
            case '+':
                return rhs
            
            case '-':
                return -rhs
            
            case _:
                raise ValueError('Unknown unary operator')
    
class NumericExpression(Expression):
    def __init__(self, value):
        self.value = value
        
    def tree_view(self):
        return str(self.value)
    
    def evaluate(self):
        return self.value    
    
class VariableExpression(Expression):
    def __init__(self, variable):
        self.variable = variable
        
    def tree_view(self):
        return self.variable
    
    def evaluate(self):
        if self.variable in Expression.variables:
            return Expression.variables[self.variable]
        else:
            raise ValueError('Undefined variable ' + self.variable)
    
class UnaryOperatorExpression(Expression):
    def __init__(self, operator, rhs):
        self.operator = operator
        self.rhs = rhs
        
    def tree_view(self):
        return self.operator + self.rhs.tree_view()
    
    def evaluate(self):
        if self.operator == '-':
            return - self.rhs.evaluate()
        else:
            raise ValueError('Unknown unary operator')