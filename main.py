from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.app import App
from kivymd.app import MDApp

KV = """
BoxLayout:
    orientation: 'vertical'
    MDLabel:
        id: label
        text: 'Tic Tac Toe'
        halign: 'center'
        font_style: 'H4'
        size_hint_y: 0.2

    GridLayout:
        id: grid
        cols: 3
        rows: 3

    MDRaisedButton:
        text: 'Reset'
        pos_hint: {'center_x': 0.5}
        size_hint_y: 0.2
        on_release: app.reset_board()
"""

class TicTacToeApp(MDApp):
    def build(self):
        self.title = "Tic Tac Toe"
        self.current_player = 'X'
        self.board = [['' for _ in range(3)] for _ in range(3)]
        return Builder.load_string(KV)

    def on_start(self):
        self.reset_board()

    def reset_board(self):
        grid = self.root.ids.grid
        grid.clear_widgets()
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.root.ids.label.text = 'Tic Tac Toe'

        for row in range(3):
            for col in range(3):
                button = Button(font_size=32, on_press=self.make_move)
                button.row, button.col = row, col
                grid.add_widget(button)

    def make_move(self, button):
        if button.text == '' and not self.check_winner():
            button.text = self.current_player
            self.board[button.row][button.col] = self.current_player
            if self.check_winner():
                self.root.ids.label.text = f'{self.current_player} Wins!'
            elif all(cell for row in self.board for cell in row):
                self.root.ids.label.text = 'Draw!'
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        for line in self.board + list(zip(*self.board)):
            if line.count(line[0]) == 3 and line[0] != '':
                return True

        if all(self.board[i][i] == self.current_player for i in range(3)) or \
           all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True

        return False

if __name__ == '__main__':
    TicTacToeApp().run()