from random import randint, choice
from typing_extensions import Annotated
from rich.console import Console
from rich.table import Table
from rich import print
from itertools import cycle
import typer


app = typer.Typer()


RANDOM_TALENTS = [
    "[cyan]Acute Sense[/cyan] [green](Enhanced chosen sense)[/green]",
    "[cyan]Ambidextrous[/cyan]",
    "[cyan]Animal Affinity[/cyan] [green](Animals feel calm around you)[/green]",
    "[cyan]Artistic[/cyan] [green](You can make precise sketches)[/green]",
    "[cyan]Attractive[/cyan] [green](Better charming)[/green]",
    "[cyan]Coolheaded[/cyan] [green](+5 Willpower)[/green]",
    "[cyan]Craftsman[/cyan] [green](Enhanced Trade(Any))[/green]",
    "[cyan]Flee![/cyan] [green](+1 Movement when Fleeing)[/green]",
    "[cyan]Hardy[/cyan] [green](Additional Wounds)[/green]",
    "[cyan]Lightning Reflexes[/cyan] [green](+5 Agility)[/green]",
    # "[cyan]Linguistics[/cyan] [green](You can learn languages by exposure)[/green]",
    "[cyan]Luck[/cyan] [green](+1 Fortune Point)[/green]",
    "[cyan]Marksman[/cyan] [green](+5 Ballistic Skill)[/green]",
    "[cyan]Mimic[/cyan] [green](You can replicate accent)[/green]",
    "[cyan]Night Vision[/cyan]",
    "[cyan]Nimble Fingered[/cyan] [green](+5 Dexterity)[/green]",
    "[cyan]Noble Blood[/cyan] [green](Higher Status if dressed)[/green]",
    # "[cyan]Orientation[/cyan]",
    "[cyan]Perfect Pitch[/cyan] [green](Enhanced Entertain(Sing) and Tonal Languages)[/green]",
    "[cyan]Pure Soul[/cyan] [green](More resistant to mutations)[/green]",
    "[cyan]Read/Write[/cyan]",
    "[cyan]Resistance (Corruption)[/cyan] [green](Auto-pass on first Resist(Corruption) test)[/green]",
    "[cyan]Resistance (Disease)[/cyan] [green](Auto-pass on first Resist(Disease) test)[/green]",
    "[cyan]Resistance (Poison)[/cyan] [green](Auto-pass on first Resist(Poison) test)[/green]",
    "[cyan]Resistance (Every Weather)[/cyan] [green](Auto-pass on first Resist(Every Weather) test)[/green]",
    "[cyan]Savvy[/cyan] [green](+5 Intelligence)[/green]",
    "[cyan]Sharp[/cyan] [green](+5 Initiative)[/green]",
    "[cyan]Sixth Sense[/cyan] [green](Sense danger)[/green]",
    # "[cyan]Strong Legs[/cyan] [green](Better Leaping)[/green]",
    "[cyan]Sturdy[/cyan] [green](You can carry more encumbrance)[/green]",
    "[cyan]Suave[/cyan] [green](+5 Fellowship)[/green]",
    # "[cyan]Super Numerate[/cyan]",
    "[cyan]Very Resilient[/cyan] [green](+5 Toughness)[/green]",
    "[cyan]Very Strong[/cyan] [green](+5 Strength)[/green]",
    "[cyan]Warrior Born[/cyan] [green](+5 Weapon Skill)[/green]",
]
COLORS = ["cyan", "magenta", "green", "red", "yellow"]
NUMBER_OF_STATS = 10
NUMBER_OF_STATS_SET = 3
MIN_VALUE_OF_STATS_SET = 100
MAX_VALUE_OF_STATS_SET = 130
POINT_BUY = 105
SHOW_STAT_VALUES = False
NUMBER_OF_RANDOM_TALENTS = 3


def get_set_of_stats():
    result = []
    while compute_value_of_stats(result) < MIN_VALUE_OF_STATS_SET or compute_value_of_stats(result) > MAX_VALUE_OF_STATS_SET:
        result = []
        for _ in range(NUMBER_OF_STATS):
            result.append(randint(1, 10) + randint(1, 10))
    return result


def compute_value_of_stats(stats):
    return sum([stat if stat <= 18 else stat + (stat - 18) for stat in stats])


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


def print_starting_exp(starting_exp):
    print(f"Starting experience is [red]{starting_exp}[/red].")


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

    print(f"Random Talent {num}: {first_talent} or {second_talent}")


def remove_used_talents(used_talents):
    if not used_talents:
        return
    detected_talents = detect_talents(used_talents)

    for detected_talent in detected_talents:
        RANDOM_TALENTS.remove(detected_talent)

    print(f"Detected Removed talents: {detected_talents}")


def detect_talents(used_talents):
    talents = [talent.strip() for talent in used_talents.split(",")]

    detected_talents = []
    for talent in talents:
        for random_talent in RANDOM_TALENTS:
            if talent.lower() in random_talent.lower():
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
    print_starting_exp(300)
    print()


if __name__ == "__main__":
    app()
