from datetime import datetime, timedelta

class Leitor():
    def __init__(self, nome):
        self.nome = nome

    def livro(self,livros):
        self.livros= livros

    def emprestimo(self,data_emp):
        self.data_emp = datetime.strptime(data_emp, "%d.%m")

    def devolucao(self, data_dev):
        self.data_dev = datetime.strptime(data_dev, "%d.%m")

    def verificar_prazo(self):
        data_limite = self.data_emp + timedelta(days=20)
        if hasattr(self,'data_dev'):
            if self.data_dev > data_limite:
                return f"O livro'{self.livros}' foi devolvido com atraso em {self.data_dev.strftime('%d.%m')}! Prazo era até {data_limite.strftime('%d.%m')}."
            else:
                return f"O livro'{self.livros}' foi devolvido no prazo em {self.data_dev.strftime('%d.%m')}."
        else:
            return f"O livro'{self.livros}' ainda não devolvido.O prazo é até {data_limite.strftime('%d.%m')}."

    def __str__(self):
       prazo_status = self.verificar_prazo()
       return f"Nome do leitor: {self.nome}\n" \
              f"Nome do livro: {self.livros}\n" \
              f"Data de empréstimo: {self.data_emp.strftime('%d.%m')}\n" \
              f"Data de devolução: {self.data_dev.strftime('%d.%m') if hasattr(self, 'data_dev') else 'Ainda não devolvido'}\n" \
              f"{prazo_status}"
