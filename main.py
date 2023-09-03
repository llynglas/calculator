from parseit import Parser
import expression
import sys

def main():
    parser = Parser()
    
    print(parser.parse("1+2+a").tree_view())
    print(parser.parse("1+2+a").evaluate())
    print(parser.parse("a--a").tree_view())
    print(parser.parse("a--a").evaluate())
    print(parser.parse("one").tree_view())
    print(parser.parse("one").evaluate())
    print(parser.parse("one+a-b").tree_view())
    print(parser.parse("one+a-b").evaluate())
    
    #if expression != None:
        #print(expression.evaluate())
        
if __name__ == '__main__':
    sys.exit(main())  