from playground import Playground
from tictoctoe import TicTacToe

playground: Playground = Playground()
tictoctoe: TicTacToe = TicTacToe(playground.screen)

tictoctoe.player()

playground.screen.mainloop()
