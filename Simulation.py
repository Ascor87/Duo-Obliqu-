"""
Duo Obliqué - Balance Simulation
Ein taktisches Zweispielerspiel auf dem klassischen Solitär-Brett.
Lizenz: CC BY 4.0
"""

import random

def get_board():
    """
    Erstellt das klassische 33-Loch Solitär-Brett.
    0: Leer, 1: Spieler 1, 2: Spieler 2, -1: Ungültiges Feld
    """
    board = [[-1]*7 for _ in range(7)]
    valid_coords = [
        (0,2),(0,3),(0,4),
        (1,2),(1,3),(1,4),
        (2,0),(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),
        (3,0),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),
        (4,0),(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),
        (5,2),(5,3),(5,4),
        (6,2),(6,3),(6,4)
    ]
    for r, c in valid_coords: 
        board[r][c] = 0
    
    # Startaufstellung (180 Grad gespiegeltes L)
    p1_coords = [(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,0),(2,1),(2,2),(3,0),(3,1),(4,0),(4,1),(4,2)]
    p2_coords = [(6,4),(6,3),(6,2),(5,4),(5,3),(5,2),(4,6),(4,5),(4,4),(3,6),(3,5),(2,6),(2,5),(2,4)]
    
    for r, c in p1_coords: board[r][c] = 1
    for r, c in p2_coords: board[r][c] = 2
    board[3][3] = 0 # Das Zentrum bleibt zu Beginn leer
    
    return board

def get_moves(board, player):
    """Ermittelt alle orthogonalen Sprünge für einen Spieler."""
    moves = []
    for r in range(7):
        for c in range(7):
            if board[r][c] == player:
                for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nr, nc = r + dr, c + dc       # Übersprungenes Feld
                    fr, fc = r + 2*dr, c + 2*dc   # Zielfeld
                    
                    if 0 <= fr < 7 and 0 <= fc < 7:
                        # Übersprungenes Feld muss besetzt sein (1 oder 2), Zielfeld muss leer sein (0)
                        if board[nr][nc] in [1, 2] and board[fr][fc] == 0:
                            moves.append(((r,c), (nr,nc), (fr,fc)))
    return moves

def simulate_game():
    """Simuliert eine einzelne Partie inkl. Pie-Rule und optionalen Kettensprüngen."""
    board = get_board()
    turns = 0
    chain_jumps = 0
    
    # 1. Zug von Spieler 1
    p1_moves = get_moves(board, 1)
    if not p1_moves: return None
    move = random.choice(p1_moves)
    board[move[0][0]][move[0][1]] = 0 # Startfeld leeren
    board[move[1][0]][move[1][1]] = 0 # Übersprungene Murmel entfernen (egal welche Farbe)
    board[move[2][0]][move[2][1]] = 1 # Zielfeld belegen
    turns += 1
    
    # 2. Pie Rule (Tauschregel): P2 entscheidet (hier in der Simulation 50/50 Chance)
    current_p1, current_p2 = 1, 2
    if random.choice([True, False]):
        current_p1, current_p2 = 2, 1
        
    turn = 2 # P2 ist am Zug
    consecutive_passes = 0
    
    while consecutive_passes < 2:
        curr_player = current_p1 if turn == 1 else current_p2
        moves = get_moves(board, curr_player)
        
        if not moves:
            consecutive_passes += 1 # Spieler muss aussetzen
        else:
            consecutive_passes = 0
            # Erster Sprung
            move = random.choice(moves)
            board[move[0][0]][move[0][1]] = 0
            board[move[1][0]][move[1][1]] = 0
            board[move[2][0]][move[2][1]] = curr_player
            
            # Optionaler zweiter Sprung (Kettensprung)
            # Darf nicht auf das ursprüngliche Startfeld zurückführen
            second_moves = [m for m in get_moves(board, curr_player) if m[0] == move[2] and m[2] != move[0]]
            if second_moves and random.choice([True, False]):
                m2 = random.choice(second_moves)
                board[m2[0][0]][m2[0][1]] = 0
                board[m2[1][0]][m2[1][1]] = 0
                board[m2[2][0]][m2[2][1]] = curr_player
                chain_jumps += 1
            turns += 1
        
        turn = 3 - turn # Spielerwechsel (1->2, 2->1)
        
    # Abrechnung
    p1_count = sum(row.count(current_p1) for row in board)
    p2_count = sum(row.count(current_p2) for row in board)
    return {"p1": p1_count, "p2": p2_count, "turns": turns, "chains": chain_jumps}

if __name__ == "__main__":
    num_games = 175
    print(f"Starte Simulation von {num_games} Partien Duo Obliqué...\n")
    
    results = [simulate_game() for _ in range(num_games)]
    
    p1_wins = sum(1 for r in results if r["p1"] > r["p2"])
    p2_wins = sum(1 for r in results if r["p1"] < r["p2"])
    draws = sum(1 for r in results if r["p1"] == r["p2"])
    
    avg_turns = sum(r["turns"] for r in results) / num_games
    avg_chains = sum(r["chains"] for r in results) / num_games
    avg_marbles = sum(r["p1"] + r["p2"] for r in results) / num_games
    
    print("-" * 30)
    print(f"Ergebnisse ({num_games} Partien):")
    print("-" * 30)
    print(f"Siege Spieler 1:  {p1_wins} ({(p1_wins/num_games)*100:.1f}%)")
    print(f"Siege Spieler 2:  {p2_wins} ({(p2_wins/num_games)*100:.1f}%)")
    print(f"Unentschieden:    {draws} ({(draws/num_games)*100:.1f}%)\n")
    print(f"Ø Züge/Partie:    {avg_turns:.1f}")
    print(f"Ø Kettensprünge:  {avg_chains:.1f}")
    print(f"Ø Übrige Murmeln: {avg_marbles:.1f}")
    print("-" * 30)
  
