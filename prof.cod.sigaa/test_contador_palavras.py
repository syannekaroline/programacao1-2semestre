import unittest
from contador_palavras import clearText


class ContadorTestCase(unittest.TestCase):

    def testecleartext(self):
        clearedText = clearText('''Alo mundo.
        A' rápida raposa marrom    pula por cima do cão preguiçoso. **##



        dsd/ksks palavra-chave
        %$@ fim.  
        ''')
        self.assertEqual(clearedText, "alo mundo a' rápida raposa marrom pula por cima do cão preguiçoso dsd ksks palavra-chave fim", msg="clearText falhou")

if __name__ == '__main__':
    unittest.main()