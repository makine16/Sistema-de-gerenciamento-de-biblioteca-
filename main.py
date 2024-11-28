from classe import Leitor

leitor1 = Leitor('Lucas')
leitor1.livro('Os tres mosqueteiros')
leitor1.emprestimo("11.09")
leitor1.devolucao("01.10")
leitor1.verificar_prazo()

leitor2 = Leitor('Mária')
leitor2.livro('Dom Casmurro')
leitor2.emprestimo("20.09")
leitor2.devolucao("15.10")
leitor2.verificar_prazo()

print(leitor1)
print()
print(leitor2)
