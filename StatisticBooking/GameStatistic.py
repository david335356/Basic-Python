import sqlite3
conn = sqlite3.connect('gameStatistics.db')

VIEW = 1
ADD = 2
DELETE= 3
QUIT = 4

def createTable():
    conn.execute('''CREATE TABLE if not exists GAMESTATS
(name TEXT PRIMARY KEY NOT NULL,
wins INT NOT NULL,
losses INT NOT NULL,
ties INT NOT NULL);''')
    print("table has been created")

def addPlayerStats():
    name = input("Enter player's name: ")
    wins = input("Enter player's win count: ")
    losses = input("Enter player's loss count: ")
    ties = input("Enter player's tie countl ")
    
    sql = "INSERT INTO GAMESTATS (name, wins, losses, ties) VALUES (?, ?, ?, ?)"
    conn.execute(sql, (name, wins, losses, ties))
    
    conn.commit()
    print(name, "has been added to the stats.")
    

def viewStats():
    print()
    print("PLAYER STATS")
    print("----------------------------------------------------------------------")

    cursor = conn.execute('SELECT name, wins, losses, ties FROM GAMESTATS ORDER BY name')
    print("{:15}{:>10}{:>10}{:>10}{:>15}".format("Name", "Wins", "Losses", "Ties ", "Total Games"))

    for row in cursor:
            print("{:15}{:>10}{:>10}{:>10}{:>15}".format(row[0],row[1],row[2],row[3], row[1]+row[2]+row[3]))         
    

def deleteStats():
    removalPlayer = input("Enter a players name to delete player statistics.")
    sql = "DELETE FROM GAMESTATS WHERE name=?"
    conn.execute(sql,(removalPlayer,))
    conn.commit()
    print("Player", removalPlayer , "has been taken off the record")
    cursor = conn.execute('SELECT name, wins, losses, ties FROM GAMESTATS')
    for row in cursor:
            print("{:15}{:>10}{:>10}{:>10}{:>15}".format(row[0],row[1],row[2],row[3], row[1]+row[2]+row[3]))         
    

def get_menu_choice():
    print()
    print("1)View Player")
    print("2)Add player")
    print("3)Delete Player")
    print("4)Quit")
    print()
    choice = int(input("Enter a choice 1-4."))
    while choice < VIEW or choice >QUIT:
        choice = int(input("Enter a valid choice"))
    return choice

def exitStats():
    conn.close()
    print("Records has been closed")
    
def main():
    choice = 0
    while choice != QUIT:
            
        choice = get_menu_choice()
        if choice == VIEW:
            viewStats()
        elif choice == ADD:
            addPlayerStats()
        elif choice == DELETE:
            deleteStats()
    if choice == QUIT:
        exitStats()


createTable()
main()
