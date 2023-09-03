from expression import NumericExpression 

EOT = chr(0x0a)

class Tokenizer:
    
    def new_line(self, line):
        self.line = line + EOT
        self.line_length = len(self.line)
        self.index = 0
        
    def is_end(self, skip_whitespace = True):
        if skip_whitespace:
            self.skip_whitespace()
            
        return self.line[self.index] == EOT
    
    def mark(self):
        self.saved_index = self.index
        
    def restore(self):
        self.index = self.saved_index
        
    def skip_whitespace(self):
        while not self.is_end(skip_whitespace = False) and self.line[self.index].isspace():
            self.index += 1

    def is_character(self, expected_char):
        self.skip_whitespace()
        
        if self.is_end():
            return None
        
        if self.line[self.index] == expected_char:
            self.index += 1
            return expected_char
        else:
            return None
        
    def is_number(self):
        self.skip_whitespace()
        if self.line[self.index].isdigit():
            number = 0
            while not self.is_end() and self.line[self.index].isdigit():
                number *= 10
                number += ord(self.line[self.index]) - ord('0')
                self.index += 1
                
            return number
        
        return None
    
    def is_variable(self):
        variable = None
        self.skip_whitespace()
        if self.line[self.index].isalpha():
            start_index = self.index
            while True: 
                self.index += 1
                if not self.line[self.index].isalnum():
                    break
            
            variable = self.line[start_index:self.index]
            
        return variable
            
        
        