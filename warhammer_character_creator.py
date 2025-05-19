from random import randint, choice
from typing_extensions import Annotated
from rich.console import Console
from rich.table import Table
from rich import print
from itertools import cycle
from talents import Talent
import typer


app = typer.Typer()


RANDOM_TALENTS = [
    # Main Stats Section
    Talent("Warrior Born", "+5 Weapon Skill"),
    Talent("Marksman", "+5 Ballistic Skill"),
    Talent("Very Strong", "+5 Strength"),
    Talent("Very Resilient", "+5 Toughness"),
    Talent("Sharp", "+5 Initiative"),
    Talent("Lightning Reflexes", "+5 Agility"),
    Talent("Nimble Fingered", "+5 Dexterity"),
    Talent("Savvy", "+5 Intelligence"),
    Talent("Coolheaded", "+5 Willpower"),
    Talent("Suave", "+5 Fellowship"),

    # Additional Stats Section
    Talent("Flee!", "+1 Movement when Fleeing"),
    Talent("Hardy", "Additional Wounds"),
    Talent("Luck", "+1 Fortune Point"),

    # Resistance Section
    Talent("Pure Soul", "More resistant to mutations"),
    Talent("Resistance (Corruption)", "Auto-pass on first Resist(Corruption) test"),
    Talent("Resistance (Disease)", "Auto-pass on first Resist(Disease) test"),
    Talent("Resistance (Poison)", "Auto-pass on first Resist(Poison) test"),
    Talent("Resistance (Every Weather)", "Auto-pass on first Resist(Every Weather) test"),

    # Roleplay Section
    Talent("Read/Write"),
    Talent("Noble Blood", "Higher Status if dressed"),
    Talent("Attractive", "Better charming"),
    Talent("Mimic", "You can replicate accent"),
    Talent("Animal Affinity", "Animals feel calm around you"),
    Talent("Artistic", "You can make precise sketches"),
    Talent("Craftsman", "Enhanced Trade(Any)"),
    Talent("Perfect Pitch", "Enhanced Entertain(Sing) and Tonal Languages"),

    # Body Enhancement Section
    Talent("Acute Sense", "Enhanced chosen sense"),
    Talent("Ambidextrous"),
    Talent("Night Vision"),
    Talent("Sixth Sense", "Sense danger"),
    Talent("Sturdy", "You can carry more encumbrance"),
    
    # Useless Section
    # Talent("Linguistics", "You can learn languages by exposure"),
    # Talent("Orientation"),
    # Talent("Strong Legs", "Better Leaping"),
    # Talent("Super Numerate"),
]
COLORS = ["cyan", "magenta", "green", "red", "yellow"]
NUMBER_OF_STATS = 10
NUMBER_OF_STATS_SET = 3
MIN_VALUE_OF_STATS_SET = 100
MAX_VALUE_OF_STATS_SET = 130
ADDITIONAL_COST_FOR_STATS = {
    20: 22,
    19: 20,
}
POINT_BUY = 105
SHOW_STAT_VALUES = False
NUMBER_OF_RANDOM_TALENTS = 3
STARTING_EXP = 300


def get_set_of_stats():
    result = []
    while compute_value_of_stats(result) < MIN_VALUE_OF_STATS_SET or compute_value_of_stats(result) > MAX_VALUE_OF_STATS_SET:
        result = []
        for _ in range(NUMBER_OF_STATS):
            result.append(randint(1, 10) + randint(1, 10))
    return result


def compute_value_of_stats(stats):
    return sum([stat if stat not in ADDITIONAL_COST_FOR_STATS else ADDITIONAL_COST_FOR_STATS[stat] for stat in stats])


def print_intro():
    print(f"[bold][red]Character Creation")


def print_point_buy_info():
    print(f"Choose one of the above (you can rearrange stats) or make a point-buy with sum of {POINT_BUY} points (4-18 per stat).")


def print_race_info():
    print(f"- You can either choose a race or pick a random one. Either way there no additional experience.")


def print_career_info():
    print(f"- You can either choose a career or pick a random one. Either way there no additional experience.")


def print_star_sign_info():
    print(f"- You can either choose a star sign or pick a random one. Either way there no additional experience.")


def print_starting_exp():
    print(f"Starting experience is [red]{STARTING_EXP}[/red].")


def get_table_with_stats():
    stats_blocks = [sorted(get_set_of_stats(), key=lambda x: -x) for _ in range(NUMBER_OF_STATS_SET)]
    colors = cycle(COLORS)
    
    table = Table(title="Stats")

    for i in range(len(stats_blocks)):
        table.add_column(f"STATS SET {i + 1}", justify="center", style=next(colors))

    for i in range(NUMBER_OF_STATS):
        values = [str(stats[i]) for stats in stats_blocks]
        table.add_row(*values)

    sum_values = [f"SUM: {sum(stats)}" for stats in stats_blocks]
    table.add_row(*sum_values)

    if SHOW_STAT_VALUES:
        sum_values = [f"VALUE: {compute_value_of_stats(stats)}" for stats in stats_blocks]
        table.add_row(*sum_values)

    console = Console()
    console.print(table)
    print_point_buy_info()


def get_random_talent(num=1):
    first_talent = choice(RANDOM_TALENTS)
    RANDOM_TALENTS.remove(first_talent)

    second_talent = choice(RANDOM_TALENTS)
    RANDOM_TALENTS.remove(second_talent)

    print(f"Random Talent {num}: {first_talent.full_name} or {second_talent.full_name}")


def remove_used_talents(used_talents):
    if not used_talents:
        return
    detected_talents = detect_talents(used_talents)

    for detected_talent in detected_talents:
        RANDOM_TALENTS.remove(detected_talent)

    print(f"Detected Removed talents: {[talent.full_name for talent in detected_talents]}")


def detect_talents(used_talents):
    talents = [talent.strip() for talent in used_talents.split(",")]

    detected_talents = []
    for talent in talents:
        for random_talent in RANDOM_TALENTS:
            if talent.lower() in random_talent.full_name.lower():
                detected_talents.append(random_talent)
                break
    return detected_talents


def get_random_talents():
    for i in range(NUMBER_OF_RANDOM_TALENTS):
        get_random_talent(i + 1)


@app.command(help="Generate stats.")
def main(used_talents: Annotated[str, typer.Option(help="Already used talents. Add then with commas.")] = ""):
    print()
    print_intro()
    print()

    print_race_info()
    print_career_info()
    print_star_sign_info()
    print()

    get_table_with_stats()
    print()
    remove_used_talents(used_talents)
    print()
    get_random_talents()
    print()
    print_starting_exp()
    print()


if __name__ == "__main__":
    app()
