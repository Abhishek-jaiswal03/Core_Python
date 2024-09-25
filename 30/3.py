x = int(input("Enter the number of players you want to enter: "))
d1 = {}
for e in range(x):
    N = input(f"Enter the name of player {e + 1}: ")
    match_played = int(input("Enter the matches played: "))
    total_runs = int(input("Enter total runs: "))
    half_centuries = int(input("Enter half-centuries: "))
    centuries = int(input("Enter the number of centuries: "))
    
    d1[N] = (match_played, total_runs, half_centuries, centuries)

print(d1)
