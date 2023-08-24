import sys

from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLineEdit, QApplication, QLabel, QPushButton


class CalculadoraAreaCubo(QMainWindow):
    def __init__(self):
        super().__init__()

        # Config título da janela
        self.setWindowTitle("Calculadora de área para cubos.")

        # Cria o widget principal dentro da janela
        widget_principal = QWidget()
        # Define que o widget ficará centralizado na janela
        self.setCentralWidget(widget_principal)
        # Cria layout para o widget principal
        layout = QVBoxLayout()
        widget_principal.setLayout(layout)
        # Insere os campos para interação com o usuário
        self.txt_largura = QLineEdit()
        self.txt_altura = QLineEdit()
        self.txt_comprimento = QLineEdit()
        # Adiciona os widgets acima ao layout
        layout.addWidget(QLabel('Largura'))
        layout.addWidget(self.txt_largura)
        layout.addWidget(QLabel('Altura'))
        layout.addWidget(self.txt_altura)
        layout.addWidget(QLabel('Comprimento'))
        layout.addWidget(self.txt_comprimento)
        # Cria botão e informa o deste botão
        self.btn_calcular = QPushButton("Calcular área")
        # Adiciona botão (somente a instância, não o método) ao layout
        layout.addWidget(self.btn_calcular)
        # Adiciona resultado ao layout
        self.lbl_resultado = QLabel('Área do cubo: ')
        layout.addWidget(self.lbl_resultado)

        self.btn_calcular.clicked.connect(self.calcular_area)

    def calcular_area(self):
        # Captura os dados de input e passa para variáveis usando a função text
        try:
            largura = float(self.txt_largura.text())
        except ValueError:
            self.lbl_resultado.setText(f'O valor da largura não é valido')
        try:
            altura = float(self.txt_altura.text())
        except ValueError:
            self.lbl_resultado.setText(f'O valor da largura não é valido')
        try:
            comprimento = float(self.txt_comprimento.text())
        except ValueError:
            self.lbl_resultado.setText(f'O valor da largura não é valido')

        area = largura * altura * comprimento

        self.lbl_resultado.setText(f'A área do cubo é {area}')


if __name__ == '__main__':
    # Cria uma app de QT(QApplication)
    app = QApplication(sys.argv)
    # Cria a instância da calculadora
    calculadora = CalculadoraAreaCubo()
    # Exibe a tela do aplicativo
    calculadora.show()
    # Inicia o loop de eventos da aplicação e espera até que a janela seja fechada
    sys.exit(app.exec())
