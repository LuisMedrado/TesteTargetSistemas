"""verificacao de ocorrencia da letra A"""
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

def count_letra(text):
    """função para contar as ocorrencias da letra"""
    # só de colocar o 'a' minusculo já conta as duas possibilidades: maiusculo ou minusculo
    count = text.lower().count('a')
    return count

class LetterChecker(QWidget):
    """telinha simples"""
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Contador de 'a'")
        self.setGeometry(100, 100, 300, 150)
        
        layout = QVBoxLayout()

        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Insira uma string")
        layout.addWidget(self.input_field)
        
        self.check_button = QPushButton("Contar 'a'", self)
        self.check_button.clicked.connect(self.check_letter)
        layout.addWidget(self.check_button)
        
        self.result_label = QLabel("", self)
        layout.addWidget(self.result_label)
        
        self.setLayout(layout)
    
    def check_letter(self):
        """funcao para checar se ha ocorrencia da letra"""
        user_input = self.input_field.text()
        
        count = count_letra(user_input)
        
        if count > 0:
            self.result_label.setText(f"A letra 'a' aparece {count} vez(es) na string.")
        else:
            self.result_label.setText("A letra 'a' não aparece na string.")
    

if __name__ == "__main__":
    app = QApplication([])
    window = LetterChecker()
    window.show()
    app.exec()

