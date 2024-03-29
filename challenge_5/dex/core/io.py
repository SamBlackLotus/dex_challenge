import os
from datetime import datetime
from typing import Dict


break_line: str = (" " * 80) + "\n"


def client_helper() -> str:
    """
    This function prints the client helper in the CLI.

    Returns
    -------
    helper_msg:
        The client helper message.
    """

    helper_msg: str = """
    Hello! Welcome to the Monster Dex.

    Here you can choose between the following options, that are:

    --trivia

    If you choose trivia we'll show you some interesting  information
    about the pokemon, or digimon list you provided, notice that this
    option only works with one file at time, so inform just one list
    for each time you use this option.

    For the next two options notice we'll need two players, each player
    will need to provide a list, since the functions work with comparisons:

    --info

    We'll show you some comparative information about the two players
    pokemon, or digimon lists.

    --battle

    The two players will challenge each other, using their three strongest
    pokemon or digimon, where the first monster to fall decides
    the winner and we'll show you the battle results.

    """
    return helper_msg


def client_usage() -> str:
    """
    This function prints the client usage in the CLI.

    Returns
    -------
    client_usage_msg:
        The client usage message.
    """
    client_usage_msg: str = """
    CLI usage examples:

    HELPER
    > python3 dex/main.py --help

    TRIVIA
    > python3 dex/main.py --trivia ../data/pokemon/json/pokemons_1.json --id 1
    > python3 dex/main.py --trivia ../data/digimon/json/digimons_1.json --id 1

    INFO
    > python3 dex/main.py --player1 ../data/pokemon/json/pokemons_1.json
    --player2 ../data/pokemon/json/pokemons_2.json --id 1 --info
    > python3 dex/main.py --player1 ../data/digimon/json/digimons_1.json
    --player2 ../data/digimon/json/digimons_2.json --id 1 --info

    BATTLE
    > python3 dex/main.py --player1 ../data/pokemon/json/pokemons_1.json
    --player2 ../data/pokemon/json/pokemons_2.json --id 1 --battle
    > python3 dex/main.py --player1 ../data/digimon/json/digimons_1.json
    --player2 ../data/digimon/json/digimons_2.json --id 1 --battle
    
    In the Battle option, you will be asked how many monster will participate 
    in the battle, the archive size will be validated, if you informed a number
    bigger than the amount of monsters in the list, it will return a error.

    ATTENTION:

    Where you read <pokemons_1.json> or <pokemons_2.json>
    Notice that both lists don't need to be in the same format, here you
    can use more than one file format at the same time, like a json and a
    csv list at the same time, it will work as well.
    You can use the formats that best suits your needs:
    Example --> pokemons_1.json  pokemons_2.json
                pokemons_1.csv   pokemons_2.csv
                pokemons_1.xml   pokemons_2.xml
                pokemons_1.yaml  pokemons_2.yaml

    You can inform an pokemon list or a digimon list, when informing a digimon
    list and it will be identified by it's name, if there's digimon in the archive
    file, it will be considered a Digimon list, if there's pokemon in the archive
    file, it's gonna be considered a pokemon list.

    For all options you'll need to inform an id so the function can
    save the log in a text file, if you don't inform any id number it
    will be automatically set as 0. The id is a key name to make the file
    unique, making it possible have multiple files with different data
    across them.

    Before using the function you can choose what will be done with the
    information generated, answering the question that will be displayed:

    What do you prefer to do?

    [append|OVERWRITE]

    append -> This function will increment the file, keeping the
    information that already exists on the file and simply add
    the new one, to choose this type any of this:

    'a','A','Append','append','APPEND'

    OVERWRITE -> This option will delete the existing file and
    create a new one with the generated information, to choose
    this type any of this:

    'o','O','Overwrite','overwrite','OVERWRITE'.

    WARNING: If you don't choose an option, and just hit enter
    it will automatically use OVERWRITE option.
    """
    return client_usage_msg


# TODO: data_to_be_saved is a str
def data_saver(
    data_to_be_saved: str,
    monster_type: str,
    id_number: str,
) -> None:
    """
    This function creates a .txt file that stores the generated
    information.

    Parameters
    ----------
    saved_data:
        The information generated by one of the given commands.

    archive_type:
        The command selected by the user that will compose the
        file name and specify what kind it is.

    id_number:
        The id provided by the user, in case its not provided
        it will be filled with 0.

    """

    if os.path.exists(f"{id_number}_{monster_type}.txt"):
        user_choice: str = input(
            f"File {id_number}_{monster_type}.txt already exists, "
            + "what do you prefer to do? [append|OVERWRITE] : "
        )

        if (
            user_choice.lower() == "o"
            or user_choice.lower() == "overwrite"
            or user_choice == ""
        ):
            os.remove(f"{id_number}_{monster_type}.txt")

            print("File Overwritten successfully!")

            with open(f"{id_number}_{monster_type}.txt", "w") as target:
                target.write(data_to_be_saved)

        elif user_choice.lower() == "a" or user_choice.lower() == "append":
            with open(f"{id_number}_{monster_type}.txt", "a") as target:
                target.write(data_to_be_saved)
                print("New entry added to the file successfully!")
        else:
            print(user_choice)
            print(f"WARNING: Invalid Input.\n{client_usage()}")
            quit()

    else:
        with open(f"{id_number}_{monster_type}.txt", "w") as target:
            target.write(data_to_be_saved)


def show_pokemon_trivia(pokemons_info: Dict[str, str], id_number: str) -> None:
    """
    This function will print a message in the CLI.

    Parameters
    ----------
    pokemons_info:
        Bring the treated variables which will be used to answer
        the questions

    id_number:
        The id provided by the user, in case its not provided
        it will be filled with 0.

    """
    datenow = datetime.now()
    msg = break_line
    msg += "reported generated on: " + datenow.isoformat() + (" " * 31) + "\n"
    msg += break_line
    msg += ("=" * 29) + " Welcome to the Dex! " + ("=" * 30) + "\n"
    msg += break_line
    msg += "Here we have some useful information gathered from the list you provided us:    \n"
    msg += break_line
    msg += "1. How many pokemons there is in this list:" + (" " * 37) + "\n"
    msg += (
        (" " * 4)
        + "> "
        + pokemons_info["total_trivia"]
        + " pokemons"
        + (" " * (25 - len(pokemons_info["total_trivia"])))
        + "\n"
    )
    msg += break_line
    msg += "2. The pokemon with the highest HP point is:" + (" " * 36) + "\n"
    msg += (
        (" " * 4)
        + ">"
        + pokemons_info["hp_trivia_name"]
        + " with "
        + pokemons_info["hp_trivia_points"]
        + " HP points"
        + (
            " "
            * (
                (59 - len(pokemons_info["hp_trivia_name"]))
                - len(pokemons_info["hp_trivia_points"])
            )
        )
        + "\n"
    )
    msg += break_line
    msg += "3. Which one has the strongest attack:" + (" " * 42) + "\n"
    msg += (
        (" " * 4)
        + ">"
        + pokemons_info["atk_trivia_name"]
        + " with "
        + pokemons_info["atk_trivia_points"]
        + " attack points."
        + (
            " "
            * (
                (54 - len(pokemons_info["atk_trivia_name"]))
                - len(pokemons_info["atk_trivia_points"])
            )
        )
        + "\n"
    )
    msg += break_line
    msg += "4. Which one has the strongest defense:" + (" " * 41) + "\n"
    msg += (
        (" " * 4)
        + ">"
        + pokemons_info["def_trivia_name"]
        + " with "
        + pokemons_info["def_trivia_points"]
        + " defense points."
        + (
            " "
            * (
                (53 - len(pokemons_info["def_trivia_name"]))
                - len(pokemons_info["def_trivia_points"])
            )
        )
        + "\n"
    )
    msg += break_line
    msg += "5. Which one is the fastest:" + (" " * 52) + "\n"
    msg += (
        (" " * 4)
        + ">"
        + pokemons_info["spd_trivia_name"]
        + " with "
        + pokemons_info["spd_trivia_points"]
        + " speed points."
        + (
            " "
            * (
                (55 - len(pokemons_info["spd_trivia_name"]))
                - len(pokemons_info["spd_trivia_points"])
            )
        )
        + "\n"
    )
    msg += break_line
    msg += "Thanks for using this Dex!" + (" " * 50) + "\n"
    msg += break_line
    msg += break_line
    msg += break_line

    print(msg.format(**pokemons_info))

    data_saver(msg, "pokemon-trivia", id_number)


def show_digimon_trivia(digimon_info: Dict[str, str], id_number: str) -> None:
    """
    This function will print a message about in the CLI.

    Parameters
    ----------
    digimon_info:
        Bring the treated variables which will be used to answer
        the questions

    id_number:
        The id provided by the user, in case its not provided
        it will be filled with 0.

    """

    datenow = datetime.now()
    msg = break_line
    msg += "reported generated on: " + datenow.isoformat() + (" " * 31) + "\n"
    msg += break_line
    msg += ("=" * 29) + " Welcome to the Dex! " + ("=" * 30) + "\n"
    msg += break_line
    msg += "Here we have some useful information gathered from the list you provided us:    \n"
    msg += break_line
    msg += "1. How many Digimon there is in this list:" + (" " * 37) + "\n"
    msg += (
        (" " * 4)
        + "> "
        + digimon_info["total_trivia"]
        + " digimon"
        + (" " * (25 - len(digimon_info["total_trivia"])))
        + "\n"
    )
    msg += break_line
    msg += "2. How many different stages a digimon have?" + (" " * 36) + "\n"
    msg += (
        (" " * 4)
        + "> In this list we have "
        + digimon_info["stages_sum"]
        + " stages of digimon, they're "
        + " ".join(digimon_info["digimon_stages"])
        + "\n"
    )
    msg += break_line
    msg += "3. How many digimon in each stage there are?" + (" " * 36) + "\n"
    msg += (
        (" " * 4)
        + "> "
        + "Baby: "
        + digimon_info["total_baby"]
        + " digimon"
        + (" " * (60 - len(digimon_info["total_baby"])))
        + "\n"
    )
    msg += (
        (" " * 4)
        + "> "
        + "Rookie: "
        + digimon_info["total_rookie"]
        + " digimon"
        + (" " * (58 - len(digimon_info["total_rookie"])))
        + "\n"
    )
    msg += (
        (" " * 4)
        + "> "
        + "Champion: "
        + digimon_info["total_champion"]
        + " digimon"
        + (" " * (56 - len(digimon_info["total_champion"])))
        + "\n"
    )
    msg += (
        (" " * 4)
        + "> "
        + "Ultimate: "
        + digimon_info["total_ultimate"]
        + " digimon"
        + (" " * (56 - len(digimon_info["total_ultimate"])))
        + "\n"
    )
    msg += (
        (" " * 4)
        + "> "
        + "Mega: "
        + digimon_info["total_mega"]
        + " digimon"
        + (" " * (60 - len(digimon_info["total_mega"])))
        + "\n"
    )
    msg += (
        (" " * 4)
        + "> "
        + "Ultra: "
        + digimon_info["total_ultra"]
        + " digimon"
        + (" " * (59 - len(digimon_info["total_ultra"])))
        + "\n"
    )
    msg += break_line
    msg += (
        "4. The strongest digimon in each stage based on the Atk attribute is:"
        + (" " * 11)
        + "\n"
    )
    msg += (
        (" " * 4)
        + "> "
        + "Baby: "
        + digimon_info["baby_strongest"]
        + ", "
        + digimon_info["baby_attack"]
        + (
            " "
            * (
                65
                - len(digimon_info["baby_strongest"])
                - len(digimon_info["baby_attack"])
            )
        )
        + "\n"
    )
    msg += (
        (" " * 4)
        + "> "
        + "Rookie: "
        + digimon_info["rookie_strongest"]
        + ", "
        + digimon_info["rookie_attack"]
        + (
            " "
            * (
                63
                - len(digimon_info["rookie_strongest"])
                - len(digimon_info["rookie_attack"])
            )
        )
        + "\n"
    )
    msg += (
        (" " * 4)
        + "> "
        + "Champion: "
        + digimon_info["champion_strongest"]
        + ", "
        + digimon_info["champion_attack"]
        + (
            " "
            * (
                61
                - len(digimon_info["champion_strongest"])
                - len(digimon_info["champion_attack"])
            )
        )
        + "\n"
    )
    msg += (
        (" " * 4)
        + "> "
        + "Ultimate: "
        + digimon_info["ultimate_strongest"]
        + ", "
        + digimon_info["ultimate_attack"]
        + (
            " "
            * (
                61
                - len(digimon_info["ultimate_strongest"])
                - len(digimon_info["ultimate_attack"])
            )
        )
        + "\n"
    )
    msg += (
        (" " * 4)
        + "> "
        + "Mega: "
        + digimon_info["mega_strongest"]
        + ", "
        + digimon_info["mega_attack"]
        + (
            " "
            * (
                63
                - len(digimon_info["mega_strongest"])
                - len(digimon_info["mega_attack"])
            )
        )
        + "\n"
    )
    msg += (
        (" " * 4)
        + "> "
        + "Ultra: "
        + digimon_info["ultra_strongest"]
        + ", "
        + digimon_info["ultra_attack"]
        + (
            " "
            * (
                64
                - len(digimon_info["ultra_strongest"])
                - len(digimon_info["ultra_attack"])
            )
        )
        + "\n"
    )
    msg += break_line
    msg += "5. How many different types of digimon there is?" + (" " * 32) + "\n"
    msg += (
        (" " * 4)
        + "> In this list we have "
        + digimon_info["types_sum"]
        + " types of digimon, they're "
        + " ".join(digimon_info["digimon_types"])
        + "\n"
    )
    msg += break_line
    msg += "6. How many digimon in each type there is:" + (" " * 38) + "\n"
    msg += (
        (" " * 4)
        + "> "
        + "Data: "
        + digimon_info["total_data"]
        + (" " * (68 - len(digimon_info["total_data"])))
        + "\n"
    )
    msg += (
        (" " * 4)
        + "> "
        + "Vaccine: "
        + digimon_info["total_vaccine"]
        + (" " * (65 - len(digimon_info["total_vaccine"])))
        + "\n"
    )
    msg += (
        (" " * 4)
        + "> "
        + "Virus: "
        + digimon_info["total_virus"]
        + (" " * (67 - len(digimon_info["total_virus"])))
        + "\n"
    )
    msg += (
        (" " * 4)
        + "> "
        + "Free: "
        + digimon_info["total_free"]
        + (" " * (68 - len(digimon_info["total_free"])))
        + "\n"
    )
    msg += break_line
    msg += (
        "7. The strongest digimon in each type based on the Atk attribute is:"
        + (" " * 11)
        + "\n"
    )
    msg += (
        (" " * 4)
        + "> "
        + "Data: "
        + digimon_info["data_strongest"]
        + ", "
        + digimon_info["data_attack"]
        + (
            " "
            * (
                65
                - len(digimon_info["data_strongest"])
                - len(digimon_info["data_attack"])
            )
        )
        + "\n"
    )
    msg += (
        (" " * 4)
        + "> "
        + "Vaccine: "
        + digimon_info["vaccine_strongest"]
        + ", "
        + digimon_info["vaccine_attack"]
        + (
            " "
            * (
                63
                - len(digimon_info["vaccine_strongest"])
                - len(digimon_info["vaccine_attack"])
            )
        )
        + "\n"
    )
    msg += (
        (" " * 4)
        + "> "
        + "Virus: "
        + digimon_info["virus_strongest"]
        + ", "
        + digimon_info["virus_attack"]
        + (
            " "
            * (
                61
                - len(digimon_info["virus_strongest"])
                - len(digimon_info["virus_attack"])
            )
        )
        + "\n"
    )
    msg += (
        (" " * 4)
        + "> "
        + "Free: "
        + digimon_info["free_strongest"]
        + ", "
        + digimon_info["free_attack"]
        + (
            " "
            * (
                61
                - len(digimon_info["free_strongest"])
                - len(digimon_info["free_attack"])
            )
        )
        + "\n"
    )
    msg += break_line
    msg += (
        "8. Which is the weakest digimon of all, based on the Atk attribute is:"
        + (" " * 10)
        + "\n"
    )
    msg += (
        (" " * 4)
        + "> "
        + digimon_info["lowest_atk_name"]
        + ", on "
        + digimon_info["lowest_atk_stage"]
        + " stage, "
        + digimon_info["lowest_atk_type"]
        + " type."
        + "\n"
    )
    msg += break_line
    msg += (
        "9. Which is the strongest digimon of all, based on the Atk attribute is:"
        + (" " * 8)
        + "\n"
    )
    msg += (
        (" " * 4)
        + "> "
        + digimon_info["highest_atk_name"]
        + ", on "
        + digimon_info["highest_atk_stage"]
        + " stage, "
        + digimon_info["highest_atk_type"]
        + " type."
        + "\n"
    )
    msg += break_line
    msg += "Thanks for using this Dex!" + (" " * 50) + "\n"
    msg += break_line
    msg += break_line
    msg += break_line

    print(msg.format(**digimon_info))

    data_saver(msg, "digimon-trivia", id_number)


def show_battle_winner(battle_result: Dict[str, str], id_number: str) -> None:
    """
    This function will print a message in the CLI.

    Parameters
    ----------
    battle_result:
        Bring the treated variables which will be used to answer
        the questions


    id_number:
        The id provided by the user, in case its not provided
        it will be filled with 0.

    """
    datenow = datetime.now()
    battle_msg = break_line
    battle_msg += "reported generated on: " + datenow.isoformat() + (" " * 31) + "\n"
    battle_msg += break_line
    battle_msg += "" + (("=" * 32) + " MONSTER BATTLE " + ("=" * 32) + "\n")
    battle_msg += break_line
    battle_msg += " " + ("=" * 78) + " \n"
    battle_msg += "|" + (" " * 30) + "+++++ RESULT +++++" + (" " * 30) + "|\n"
    battle_msg += " " + ("=" * 78) + " \n"
    battle_msg += "|" + (" " * 25) + ("-" * 28) + (" " * 25) + "|\n"
    battle_msg += "|" + (" " * 34) + "--Winner--" + (" " * 34) + "|\n"
    battle_msg += (
        "|" + (" " * 35) + "Player " + str(battle_result["winner"]) + (" " * 35) + "|\n"
    )
    battle_msg += "|" + (" " * 25) + ("-" * 28) + (" " * 25) + "|\n"
    battle_msg += "|" + (" " * 34) + "--Rounds--" + (" " * 34) + "|\n"
    battle_msg += (
        "|"
        + (" " * (38 - (len(str(battle_result["rounds"])) // 2)))
        + str(battle_result["rounds"])
        + (" " * (39 - (len(str(battle_result["rounds"])) // 2)))
        + "|\n"
    )
    battle_msg += "|" + (" " * 25) + ("-" * 28) + (" " * 25) + "|\n"
    battle_msg += "|" + (" " * 26) + "--First monster to fall--" + (" " * 27) + "|\n"
    battle_msg += (
        "|"
        + (" " * (38 - (len(battle_result["loser_monster"]) // 2)))
        + battle_result["loser_monster"]
        + (" " * (39 - (len(battle_result["loser_monster"]) // 2)))
        + "|\n"
    )
    battle_msg += " " + ("=" * 78) + " \n"
    battle_msg += break_line
    battle_msg += break_line
    battle_msg += break_line

    print(battle_msg.format(**battle_result))

    data_saver(battle_msg, "battle", id_number)


def show_info_pokemon(
    monster_dict_p1: Dict[str, str],
    monster_dict_p2: Dict[str, str],
    process_monster: Dict[str, str],
    id_number: str,
    monster_type1: str,
) -> None:
    """
    This function will print a message in the CLI.

    Parameters
    ----------
    process_monster:
        Bring the treated variables which will be used to answer
        the questions

    id_number:
        The id provided by the user, in case its not provided
        it will be filled with 0.

    """
    total_monster = str(len(monster_dict_p1))
    total_monster2 = str(len(monster_dict_p2))
    datenow = datetime.now()
    msg = break_line
    msg += "reported generated on: " + datenow.isoformat() + (" " * 31) + "\n"
    msg += break_line
    msg += " " + (("=" * 32) + " POKEMON INFO " + ("=" * 32) + " \n")
    msg += (
        "|" + (" " * 18) + "| PLAYER 1" + (" " * 20) + "| PLAYER 2" + (" " * 20) + "|\n"
    )
    msg += "|" + ("-" * 18) + "|" + ("-" * 29) + "|" + ("-" * 29) + "|\n"
    msg += (
        "|Pokemons"
        + (" " * 10)
        + "| "
        + total_monster
        + (" " * (28 - len(total_monster)))
        + "| "
        + total_monster2
        + (" " * (28 - len(total_monster2)))
        + "|\n"
    )
    msg += (
        "|Strongest Pokémon"
        + " | "
        + process_monster["strongest_monster_player1_info"]
        + (" " * (28 - len(process_monster["strongest_monster_player1_info"])))
        + "| "
        + process_monster["strongest_monster_player2_info"]
        + (" " * (28 - len(process_monster["strongest_monster_player2_info"])))
        + "|\n"
    )
    msg += (
        "|Legendary"
        + (" " * 9)
        + "| "
        + process_monster["stg_or_legend_player1_info"]
        + (" " * (28 - len(process_monster["stg_or_legend_player1_info"])))
        + "| "
        + process_monster["stg_or_legend_player2_info"]
        + (" " * (28 - len(process_monster["stg_or_legend_player2_info"])))
        + "|\n"
    )
    msg += (
        "|Repeated Pokemons"
        + " | "
        + process_monster["repeated_monster_info"]
        + (" " * (58 - len(process_monster["repeated_monster_info"])))
        + "|\n"
    )
    msg += (
        "|Different Pokemons"
        + "| "
        + process_monster["different_monster_info"]
        + (" " * (58 - len(process_monster["different_monster_info"])))
        + "|\n"
    )
    msg += "|" + ("-" * 18) + "|" + ("-" * 59) + "|\n"
    msg += " " + (("=" * 78) + " \n")
    msg += break_line

    print(msg.format(**process_monster))

    data_saver(msg, "info", id_number)


def show_info_digimon(
    process_monster: Dict[str, str], id_number: str, monster_type1: str
) -> None:
    """
    This function will print a message in the CLI.

    Parameters
    ----------
    process_monster:
        Bring the treated variables which will be used to answer
        the questions

    id_number:
        The id provided by the user, in case its not provided
        it will be filled with 0.

    """
    datenow = datetime.now()
    msg = break_line
    msg += "reported generated on: " + datenow.isoformat() + (" " * 31) + "\n"
    msg += break_line
    msg += " " + (("=" * 32) + " DIGIMON INFO " + ("=" * 32) + " \n")
    msg += (
        "|" + (" " * 18) + "| PLAYER 1" + (" " * 20) + "| PLAYER 2" + (" " * 20) + "|\n"
    )
    msg += "|" + ("-" * 18) + "|" + ("-" * 29) + "|" + ("-" * 29) + "|\n"
    msg += (
        "|Digimons"
        + (" " * 10)
        + "| "
        + process_monster["player1_total_monster_info"]
        + (" " * (28 - len(process_monster["player1_total_monster_info"])))
        + "| "
        + process_monster["player2_total_monster_info"]
        + (" " * (28 - len(process_monster["player2_total_monster_info"])))
        + "|\n"
    )
    msg += (
        "|Strongest Digimon"
        + " | "
        + process_monster["strongest_monster_player1_info"]
        + (" " * (28 - len(process_monster["strongest_monster_player1_info"])))
        + "| "
        + process_monster["strongest_monster_player2_info"]
        + (" " * (28 - len(process_monster["strongest_monster_player2_info"])))
        + "|\n"
    )
    msg += (
        "|Digimon Ultra"
        + (" " * 5)
        + "| "
        + process_monster["stg_or_legend_player1_info"]
        + (" " * (28 - len(process_monster["stg_or_legend_player1_info"])))
        + "| "
        + process_monster["stg_or_legend_player2_info"]
        + (" " * (28 - len(process_monster["stg_or_legend_player2_info"])))
        + "|\n"
    )
    msg += (
        "|Repeated Digimons"
        + " | "
        + process_monster["repeated_monster_info"]
        + (" " * (58 - len(process_monster["repeated_monster_info"])))
        + "|\n"
    )
    msg += (
        "|Different Digimons"
        + "| "
        + process_monster["different_monster_info"]
        + (" " * (58 - len(process_monster["different_monster_info"])))
        + "|\n"
    )
    msg += "|" + ("-" * 18) + "|" + ("-" * 59) + "|\n"
    msg += " " + (("=" * 78) + " \n")
    msg += break_line

    print(msg.format(**process_monster))

    data_saver(msg, "info", id_number)
