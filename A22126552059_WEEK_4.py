import streamlit as st
import numpy as np

# Initialize the board with empty strings
if 'board' not in st.session_state:
    st.session_state.board = np.full((3, 3), '', dtype=str)

# Initialize the current player
if 'current_player' not in st.session_state:
    st.session_state.current_player = 'X'

# Initialize the winner
if 'winner' not in st.session_state:
    st.session_state.winner = None

# Reset the board
def reset_board():
    st.session_state.board = np.full((3, 3), '', dtype=str)
    st.session_state.current_player = 'X'
    st.session_state.winner = None

# Check if there is a winner or if the game is a draw
def check_winner():
    board = st.session_state.board
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i, :] == st.session_state.current_player) or all(board[:, i] == st.session_state.current_player):
            return st.session_state.current_player
    if all(np.diag(board) == st.session_state.current_player) or all(np.diag(np.fliplr(board)) == st.session_state.current_player):
        return st.session_state.current_player
    if '' not in board:
        return 'Draw'
    return None

# Handle a player's move
def make_move(row, col):
    if st.session_state.board[row, col] == '' and st.session_state.winner is None:
        st.session_state.board[row, col] = st.session_state.current_player
        st.session_state.winner = check_winner()
        if st.session_state.winner is None:
            st.session_state.current_player = 'O' if st.session_state.current_player == 'X' else 'X'

# Display the game board
st.title("Tic Tac Toe")
st.write("Current Player: ", st.session_state.current_player)
if st.session_state.winner:
    if st.session_state.winner == 'Draw':
        st.write("The game is a draw!")
    else:
        st.write(f"Player {st.session_state.winner} wins!")

# Create the Tic Tac Toe grid
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        with cols[j]:
            cell_text = st.session_state.board[i, j]
            cell_color = "lightgreen" if cell_text == "X" else "lightblue" if cell_text == "O" else "white"
            if st.button(cell_text or ' ', key=f"{i}-{j}", help=f"Click to place {st.session_state.current_player}",
                         on_click=make_move, args=(i, j)):
                pass
            st.write(f'<div style="background-color:{cell_color};border-radius:5px;padding:20px;color:black;text-align:center;">{cell_text}</div>', unsafe_allow_html=True)

# Reset button
if st.button('Reset Game'):
    reset_board()
