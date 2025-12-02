# from data_wrapper import DLWrapper
# #TODO


player = input("")

def create_player(name=None, date_of_birth=None, address=None, phone_number=None, email=None, link=None, handle=None, team=None,):
    #  checkar hvert það var skrifað inn rétt, er logic layer en er bara fyrir test
    
    if not name:
        name = "Unknown"
    if not date_of_birth:
        date_of_birth = "Unknown"
    if not address:
        address = "Unknown"
    if not phone_number:
        phone_number = "Unknown"
    if not email:
        email = "Unknown"
    if not link:
        link = "None"
    if not handle:
        handle = "None"
    if not team:
        team = "No Team"

    with open("src/IO/player_info.csv", "a") as player_file:
        player_file.write(f"{name},{date_of_birth},{address},{phone_number},{email},{link},{handle},{team} \n")
# skrifar upplýsingarnar um nýjann player inn í player_creation skjalið


while player != "q":
    create_player(player, 1,2,3,4,5,6,7)
    player = input("")