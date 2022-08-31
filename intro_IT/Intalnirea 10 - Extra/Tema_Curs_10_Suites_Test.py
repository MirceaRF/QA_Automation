from Tema_Curs_10_Alerts import Alerts
from Tema_curs_10_webform import WebForm
from Tema_curs_9 import Login
import unittest  #  am importat toata libraria unittest
import HtmlTestRunner


class TestSuite(unittest.TestCase): # pentru ca am importat toata libraria este nevoie sa specificam in fata clasei TestCase

    # libraria din care sa fie extrasa
                                        # Daca importam doar libraria, sistemul va avea doar adresa de identificare a librariei,
                                                         # nu si a clasei TestCase
                                       # Suita de teste = un set de teste care pot fi rulate in acelasi timp
    def test_suite(self):  # numele metodei este predefinit si NU trebuie schimbat
        teste_de_rulat = unittest.TestSuite() # am creat un obiect al clasei TestSuite
        # prin obiectul teste_de_rulat vom accesa metoda addTests
        # metoda addTests primeste ca si parametru o lista de teste care se doreste a fi executate
        # lista de teste va fi separata prin virgula

        # teste_de_rulat.addTests([]) metoda add tests, apelata fara parametru

        teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(WebForm),
            unittest.defaultTestLoader.loadTestsFromTestCase(Login)
        ])

        runner = HtmlTestRunner.HTMLTestRunner\
        (
            combine_reports=True,
            report_title='TestReport',
            report_name='Smoke Test Result'
        )

        runner.run(teste_de_rulat)
