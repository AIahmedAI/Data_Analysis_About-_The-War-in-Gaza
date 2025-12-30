#!/usr/bin/env python3
"""
Snakes and Ladders Game (السلم والتعبان)
A classic board game implemented in Python
"""

import random


class SnakesAndLadders:
    def __init__(self, num_players=2):
        # Define snakes: head -> tail (moving down)
        self.snakes = {
            16: 6,
            47: 26,
            49: 11,
            56: 53,
            62: 19,
            64: 60,
            87: 24,
            93: 73,
            95: 75,
            98: 78
        }
        
        # Define ladders: bottom -> top (moving up)
        self.ladders = {
            1: 38,
            4: 14,
            9: 31,
            21: 42,
            28: 84,
            36: 44,
            51: 67,
            71: 91,
            80: 100
        }
        
        self.num_players = num_players
        self.players = {f"Player {i+1}": {"position": 0, "finished": False} for i in range(num_players)}
        self.current_player_index = 0
        self.winner = None
        
    def roll_dice(self):
        """Roll a six-sided dice"""
        return random.randint(1, 6)
    
    def move_player(self, player_name):
        """Move a player based on dice roll and check for snakes/ladders"""
        if self.players[player_name]["finished"]:
            return  # Player has already finished
        
        dice_roll = self.roll_dice()
        print(f"{player_name} rolled a {dice_roll}")
        
        new_position = self.players[player_name]["position"] + dice_roll
        
        # Can't move beyond 100
        if new_position > 100:
            print(f"{player_name} can't move beyond position 100. Staying at position {self.players[player_name]['position']}")
            return
        
        self.players[player_name]["position"] = new_position
        print(f"{player_name} moved to position {new_position}")
        
        # Check for snakes
        if new_position in self.snakes:
            snake_tail = self.snakes[new_position]
            self.players[player_name]["position"] = snake_tail
            print(f"🐍 Oh no! {player_name} got bitten by a snake and slid down from {new_position} to {snake_tail}")
        
        # Check for ladders
        elif new_position in self.ladders:
            ladder_top = self.ladders[new_position]
            self.players[player_name]["position"] = ladder_top
            print(f"🪜 Great! {player_name} climbed a ladder from {new_position} to {ladder_top}")
        
        # Check if player reached 100
        if new_position == 100:
            self.players[player_name]["finished"] = True
            self.winner = player_name
            print(f"🎉 Congratulations! {player_name} has won the game!")
    
    def display_board(self):
        """Display the current positions of all players on the board"""
        print("\n" + "="*50)
        print("CURRENT BOARD STATUS")
        print("="*50)
        for player, data in self.players.items():
            if not data["finished"]:
                print(f"{player}: Position {data['position']}")
            else:
                print(f"{player}: FINISHED (Position 100)")
        print("="*50 + "\n")
    
    def get_next_player(self):
        """Get the next active player"""
        while True:
            current_player = f"Player {self.current_player_index % self.num_players + 1}"
            if not self.players[current_player]["finished"]:
                return current_player
            self.current_player_index += 1
            
            # Check if all players except one have finished
            finished_players = sum(1 for p in self.players.values() if p["finished"])
            if finished_players >= self.num_players - 1:
                return None  # Game over
    
    def play(self):
        """Main game loop"""
        print("🐍 Welcome to Snakes and Ladders (السلم والتعبان)! 🪜")
        print(f"Number of players: {self.num_players}")
        print("Objective: Reach position 100 to win!")
        print("Snakes: ", list(self.snakes.keys()))
        print("Ladders: ", list(self.ladders.keys()))
        print("-" * 50)
        
        while self.winner is None:
            current_player = self.get_next_player()
            if current_player is None:
                break  # Game over
            
            input(f"{current_player}'s turn. Press Enter to roll the dice...")
            self.move_player(current_player)
            
            if self.winner is None:  # Only show board if game is not over
                self.display_board()
            
            self.current_player_index += 1
        
        print("\n🏆 GAME OVER! 🏆")
        if self.winner:
            print(f"The winner is {self.winner}!")


def main():
    print("Welcome to Snakes and Ladders (السلم والتعبان)")
    
    while True:
        try:
            num_players = int(input("Enter number of players (2-4): "))
            if 2 <= num_players <= 4:
                break
            else:
                print("Please enter a number between 2 and 4.")
        except ValueError:
            print("Please enter a valid number.")
    
    game = SnakesAndLadders(num_players)
    game.play()
    
    play_again = input("\nWould you like to play again? (y/n): ")
    if play_again.lower() == 'y':
        main()


if __name__ == "__main__":
    main()