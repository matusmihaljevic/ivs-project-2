"""
Implementácia syntaktického analyzátora pre kalkulačku. 
Analyzátor rozdelí string obsahujúci matematický výraz podľa regexu na jednotlivé slová, zapíše do post-fix notácie a spracuje.

@file parse.py
@brief Syntaktický analyzátor pre kalkulačku
@author Matúš Mihaljevič
"""

import re
from calc import *

precedence = {'+': 1, '-': 1, 'u-': 5, '*': 2, '/': 2, '^': 3, '//': 3, 'ln': 4, 'log': 4, '√': 4, '!': 4}
e = 2.718281828459045
pi = 3.141592653589795


def _split_expression(expression: str) -> list:
    """
    Rozdelí string obsahujúci matematický výraz podľa regexu na jednotlivé slová.
    Vyčlení špeciálne slová ako ln a log.
    Odmocninu očakáva ako binárnu operáciu index√základ. Napr. 3√64 == 4.
    Logaritmus očakáva v tvare log(základ, argument).

    @brief Rozdelí výraz na slová
    @param expression Matematický výraz na spracovanie
    @return Pole slov rozdelených podľa regexu
    """    
    words = re.findall(r'(?<!\d)\d*\.?\d+|\(|\)|//|log|ln|e|pi|[+*/-]|√|\S|!(?=\d)', expression) 
    
    unary_operators_to_delete = []                
    for i in range(len(words)):
        if words[i] in ['-','+']:
            if (i == 0) or (words[i-1] in precedence and words[i-1] != '!') or (words[i-1] == '(') or (words[i-1] == ','):
                if words[i] == '-':
                    words[i] = 'u-'
                else:
                    unary_operators_to_delete.append(i)  
  
    for i in range(len(words) - 1):
        if words[i] == 'u-' and words[i+1] == 'u-':
            unary_operators_to_delete.extend([i, i+1])  
            
    for idx in sorted(unary_operators_to_delete, reverse=True):
        del words[idx]                
    
    return words


def _parse(words: list) -> list:
    """
    Prechádza pole slov, operandy castuje na float a následne hneď zapisuje do @queue.
    Operátory na základe priority buď vymení alebo ponechá poradie a následne tiež zapíše do @queue.
    Samotné zátvorky už do @queue nezapisuje, spracuje operátory v ich vnútri.
    
    @brief Zapíše rozdelený zoznam do post-fix notácie
    @param words Pole slov rozdelených podľa regexu
    @return Pole operandov a operácií zapísané do post-fix notácie
    """
    queue = []
    operator_stack = []
        
    for word in words:        
        if (word.startswith('-') and word[1:].replace('.', '').isdigit()) or (word[0] != '-' and word.replace('.', '').isdigit()):
            if '.' in word:
                queue.append(float(word))
            else:
                queue.append(int(word))
        elif word in precedence:
            while (operator_stack and precedence.get(operator_stack[-1], 0) >= precedence.get(word, 0)):
                queue.append(operator_stack.pop())
            operator_stack.append(word)
        elif word == '(':
            operator_stack.append(word)
        elif word == ')':
            while operator_stack[-1] != '(':
                queue.append(operator_stack.pop())
            nested_expression = operator_stack.pop()
            queue += _parse(_split_expression(nested_expression[1:-1]))    
        elif word == 'e':
            queue.append(e)   
        elif word == 'pi':
            queue.append(pi)
        elif word == ',':
            continue
        else:            
            raise SyntaxError("Nepovolený znak")

             
    while operator_stack:
        queue.append(operator_stack.pop())
      
    return queue


def evaluate(expression: str) -> float:
    """
    Prechádza post-fix pole @parsed_words a pridáva postupne operandy na @evaluation_stack.
    Ak narazí na operáciu, vykoná túto operáciu na operandoch na @evaluation_stack.
    Výsledok operácie zapíše na začiatok @evaluation_stack a pokračuje v prechádzaní @parsed_words
    
    @brief Vyrieši matematický výraz
    @param expression Matematický výraz na spracovanie
    @return Výsledok matematického výrazu
    @raise SyntaxError pri nedostatku operandov 
    @see _split_expression
    @see _parse
    """
    try:
        words = _split_expression(expression)
        parsed_words = _parse(words)

        evaluation_stack = []

        for parsed_word in parsed_words:
            if isinstance(parsed_word, float) or isinstance(parsed_word, int):
                evaluation_stack.append(parsed_word)
                
            elif parsed_word == 'u-':
                if len(evaluation_stack) < 1:
                    raise SyntaxError("Nedostatok operandov pre {}".format(parsed_word))
                operand = evaluation_stack.pop()
                evaluation_stack.append(-operand)
                
            elif parsed_word in ['ln', '!']:
                if len(evaluation_stack) < 1:
                    raise SyntaxError("Nedostatok operandov pre funkciu \'{}\'" .format(parsed_word))
                operand = evaluation_stack.pop()
                if parsed_word == 'ln':
                    evaluation_stack.append(ln(operand))
                if parsed_word == '!':
                    evaluation_stack.append(fact(operand))
                    
            elif parsed_word in ['+', '-', '*', '/', '^', '//', '√', 'log']:
                if len(evaluation_stack) < 2:
                    raise SyntaxError("Nedostatok operandov pre operáciu \'{}\'" .format(parsed_word))
                b = evaluation_stack.pop()
                a = evaluation_stack.pop()
                if parsed_word == 'log':
                    evaluation_stack.append(log(a, b))
                elif parsed_word == '+':
                    evaluation_stack.append(add(a, b))
                elif parsed_word == '-':
                    evaluation_stack.append(sub(a, b))
                elif parsed_word == '*':
                    evaluation_stack.append(mult(a, b))
                elif parsed_word == '/':
                    evaluation_stack.append(div(a, b))
                elif parsed_word == '//':
                    evaluation_stack.append(int_div(a, b))
                elif parsed_word == '^':
                    evaluation_stack.append(pow(a, b))
                elif parsed_word == '√':
                    evaluation_stack.append(root(b, a))
                    
            elif isinstance(parsed_word, list):
                # Rekurzívne vyhodnotenie vnoreného výrazu
                evaluation_stack.append(evaluate(' '.join(parsed_word)))
                            
        return float(evaluation_stack[0])
    except (ValueError, ZeroDivisionError, SyntaxError) as e:
        return str(e)    