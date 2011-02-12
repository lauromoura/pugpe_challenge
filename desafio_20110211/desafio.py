"""
Desafio PUG-PE  
ID: 1
Semana: 11/02/2011

Problema:

    Dado uma lista de elementos, o objetivo eh converter esta lista em uma lista de sub-listas de elementos consecutivos duplicados. 
    >>> x = ['a','a','a','a','b','c','c','a','a','d','e','e','e','e']
    >>> ret = pack(x)
    >>> ret
    >>> [['a','a','a','a'],['b'],['c','c'],['a','a'],['d'],['e','e','e','e']]
    >>> x = ['a', 'b', 'c']
    >>> ret = pack(x)
    >>> ret 
    >>>[['a'], ['b'], ['c']]
    >>> x = []
    >>> ret = pack(x)
    >>> ret
    >>> []
     
  Seu trabalho eh construir essa lista de elementos.  Favor utilizar Testes usando doctest ou UnitTest para validar sua solucao.

"""

import unittest

def pack(items):
    import itertools
    return [list(v) for k, v in itertools.groupby(items)]

class Desafio1(unittest.TestCase):

    def test_pack_duplicates(self):
        sampleList = ['a','a','a','a','b','c','c','a','a','d','e','e','e','e']
        self.assertEqual([['a','a','a','a'],['b'],['c','c'],['a','a'],['d'],['e','e','e','e']],
                    pack(sampleList))

    def test_pack_empty(self):
        self.assertEqual([], pack([]))

    def test_pack_simple(self):
        self.assertEqual([['a'], ['b'], ['c']], pack(['a', 'b', 'c']))

if __name__ == '__main__':
    unittest.main()    
