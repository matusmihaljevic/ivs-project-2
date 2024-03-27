"""
Implementácia syntaktického analyzátora pre kalkulačku. 
Analyzátor rozdelí string obsahujúci matematický výraz podľa regexu na jednotlivé slová, zapíše do post-fix notácie a spracuje.

@file parser.py
@brief Syntaktický analyzátor pre kalkulačku
@author Matúš Mihaljevič
"""

import re
from calc import *

precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '//': 3, 'ln': 4, 'log': 4, '\\': 4}

def _split_expression(expression: str) -> list:
    """
    Rozdelí string obsahujúci matematický výraz podľa regexu na jednotlivé slová.
    Vyčlení špeciálne slová ako ln a log.
    Odmocninu očakáva ako binárnu operáciu základ\\index. Napr. 64\\3 == 4.
    Logaritmus očakáva v tvare log(základ, argument).
    
    @brief Rozdelí výraz na slová
    @param expression Matematický výraz na spracovanie
    @return Pole slov rozdelených podľa regexu
    """
    words = re.findall(r'\d*\.?\d+|\d+|ln|\(|\)|//|log|\(|\)|[+*/-]|\S', expression)
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
        if word.isdigit() or word.replace('.', '').isdigit():
            queue.append(float(word))
        elif word in precedence:
            #ak ma operator predchadzajuci vyssiu prioritu premiestni ho do queue a sucasny pridaj na koniec operator_stacku
            while (operator_stack and precedence.get(operator_stack[-1], 0) >= precedence.get(word, 0)): 
                queue.append(operator_stack.pop())
            operator_stack.append(word)
        elif word == '(':
            operator_stack.append(word)
        elif word == ')':
            while operator_stack[-1] != '(':
                queue.append(operator_stack.pop())
            operator_stack.pop()
    
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
    words = _split_expression(expression)
    parsed_words = _parse(words)

    evaluation_stack = []

    for parsed_word in parsed_words:
        if isinstance(parsed_word, float):
            evaluation_stack.append(parsed_word)
        elif parsed_word == 'ln':
            if len(evaluation_stack) < 1:
                raise SyntaxError("Nedostatok operandov pre funkciu ln(x)")
            operand = evaluation_stack.pop()
            evaluation_stack.append(ln(operand))
        elif parsed_word == 'log':
            if len(evaluation_stack) < 2:
                raise SyntaxError("Nedostatok operandov pre funkciu log(základ, argument)")
            b = evaluation_stack.pop()
            a = evaluation_stack.pop()
            evaluation_stack.append(log(a, b))
        elif parsed_word in ['+', '-', '*', '/', '^', '//', '\\']:
            if len(evaluation_stack) < 2:
                raise SyntaxError("Nedostatok operandov pre operáciu \'{}\'" .format(parsed_word))
            b = evaluation_stack.pop()
            a = evaluation_stack.pop()
            if parsed_word == '\\':
                evaluation_stack.append(root(a, b))
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
            
    return float(evaluation_stack[0])