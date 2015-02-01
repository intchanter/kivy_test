from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock

in_game = True
players = ['X', 'O']
current_player = False
board = [None] * 9
root = None
winning_directions = [
        [1, 3, 4],
        [3],
        [3, 2],
        [1],
        [],
        [],
        [1],
        [],
        [],
]

class TicTacToeApp(App):
    def build(self):
        global root
        root = Builder.load_file('ttt.kv')
        return root

def new_game(self, root):
    global in_game
    global current_player
    board_widget = root.ids.board
    for square_num in range(len(board)):
        board[square_num] = None
        board_widget.children[square_num].text = ''
        board_widget.children[square_num].background_color = [0.25, 0, 0.25, 1]
    in_game = True
    current_player = False
    root.ids.status.text = 'Turn: {}'.format(players[current_player])

def check_winner(root):
    global in_game
    open_squares = 0
    board_widget = root.ids.board
    for square in range(len(board)):
        player = board[square]
        if player is None:
            open_squares += 1
            continue
        for direction in winning_directions[square]:
            if (player == board[square + direction]
                    and player == board[square + 2 * direction]):
                in_game = False
                for button_number in (square,
                        square + direction,
                        square + 2 * direction):
                    # The next line is to work around the children being in
                    # reverse order from the .kv file.
                    # This is apparentnly deliberate behavior, optimized for
                    # touch dispatch?
                    kids = list(reversed(board_widget.children))
                    kids[button_number].background_color = [1, 0, 1, 1]
                root.ids.status.text = '{} wins!'.format(players[player])
    if open_squares < 1:
        root.ids.status.text = 'Tie!'
        in_game = False

def press(button, root):
    global current_player
    if not in_game:
        return
    square = button.square
    if board[square] is not None:
        return
    button.text = players[current_player]
    board[square] = current_player
    current_player = not current_player
    root.ids.status.text = 'Turn: {}'.format(players[current_player])
    check_winner(root)

if __name__ == '__main__':
    app = TicTacToeApp()
    app.run()
