from random import randint, choice
from typing_extensions import Annotated
from rich.panel import Panel
from rich.align import Align
from rich.columns import Columns
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.traceback import install
from visuals import get_color_cycle
from random_talents import RANDOM_TALENTS
from races import RACES, RACES_DISTRIBUTION
from star_signs import STAR_SIGNS, STAR_SIGNS_DISTRIBUTION
import typer
import os


app = typer.Typer()
install()
console = Console(record=True)


DUMPS_DIRECTORY = "dumps"


NUMBER_OF_STATS = 10
NUMBER_OF_STATS_SET = 3
MIN_VALUE_OF_STATS_SET = 100
MIN_VALUE_OF_STATS_SET_WITHOUT_HIGH_ROLLS = 108
MAX_VALUE_OF_STATS_SET = 130
ADDITIONAL_COST_FOR_STATS = {
    20: 22,
    19: 20,
}
POINT_BUY = 105
SHOW_STAT_VALUES = True
STARTING_EXP = 300


class CharacterCreation:
    def __init__(self):
        self._race = None
        self._stats = None
        self._stats_blocks = None
        self._point_buy = False
        self._star_sign = None
        self._detected_talents = []

    @property
    def RACE(self):
        return self._race

    @property
    def STATS(self):
        return self._stats
    
    def print_intro(self):
        console.print()
        console.print(f"[bold][red]Character Creation", justify="center")

    def print_available_races(self):
        tables = [race.get_table_with_race(idx + 1) for idx, race in enumerate(RACES)]

        panel = Panel.fit(
            Align.center(Columns(tables)),
            title="Available Races",
            border_style="red",
            title_align="left",
            padding=(1, 2),
        )

        console.print(panel)
        console.print(f"You can either choose a race or pick a random one. Either way there no additional experience.")
        console.print(f"To select a race: Type a number visible near race you want to choose or type 0 for a random one.")
        console.print()
    
    def print_selected_race_info(self):
        table = self.RACE.get_table_with_race()
        console.print()
        console.print(table, justify="center")
        console.print()

    def handle_race_selection(self):
        selected_number = Prompt.ask(f"Selected Race")
        self.select_race(selected_number)
    
    def select_race(self, selected_number: str):
        try:
            race_number = int(selected_number) - 1
        except Exception:
            console.print(f"[red]Error occurred when selecting a race!")
            raise typer.Abort()

        if not -1 <= race_number <= len(RACES) - 1:
            console.print(f"[red]Error occurred when selecting a race!")
            raise typer.Abort()
        
        if race_number == -1:
            race = RACES_DISTRIBUTION.random_value
            accept = typer.confirm(f"Random race: {race.NAME}. Do you accept randomly selected race?")

            if not accept:
                self.handle_race_selection()
            else:
                self._race = race
        else:
            self._race = RACES[race_number]
    
    def print_stats_info(self):
        stats_blocks = [sorted(self.get_set_of_stats(), key=lambda x: -x) for _ in range(NUMBER_OF_STATS_SET)]
        self._stats_blocks = stats_blocks
        colors = get_color_cycle()
        
        table = Table(title="Stats")

        for i in range(len(stats_blocks)):
            table.add_column(f"STATS SET {i + 1}", justify="center", style=next(colors))

        for i in range(NUMBER_OF_STATS):
            values = [str(stats[i]) for stats in stats_blocks]
            table.add_row(*values)

        sum_values = [f"SUM: {sum(stats)}" for stats in stats_blocks]
        table.add_row(*sum_values)

        if SHOW_STAT_VALUES:
            sum_values = [f"VALUE: {self.compute_value_of_stats(stats)}" for stats in stats_blocks]
            table.add_row(*sum_values)

        console.print(table, justify="center")
        console.print(f"You can either choose one of the sets or make a point-buy with sum of {POINT_BUY} points (4-18 per stat).")
        console.print(f"To select a set: Type a number visible near set you want to choose or type 0 for a point-buy.")
        console.print()

    def handle_stats_selection(self):
        selected_number = Prompt.ask(f"Selected Stats")
        self.select_stats(selected_number)
    
    def select_stats(self, selected_number: str):
        try:
            stats_number = int(selected_number) - 1
        except Exception:
            console.print(f"[red]Error occurred when selecting stats!")
            raise typer.Abort()

        if not -1 <= stats_number <= len(self._stats_blocks) - 1:
            console.print(f"[red]Error occurred when selecting stats!")
            raise typer.Abort()
        
        if stats_number == -1:
            self._point_buy = True
        else:
            self._stats = self._stats_blocks[stats_number]
        
        console.print()
    
    def print_selected_stats_info(self, suppress=False):
        if self._point_buy:
            if not suppress:
                console.print(f"[green]Point-buy selected.[/green]")
            return f"[green]Point-buy selected.[/green]"
        else:
            table = Table(title="Stats")
            table.add_column(f"VALUE", justify="center", style="cyan")

            for i in range(NUMBER_OF_STATS):
                table.add_row(f"{self.STATS[i]}")

            sum_values = f"SUM: {sum(self._stats)}"
            table.add_row(sum_values)

            if SHOW_STAT_VALUES:
                sum_values = f"VALUE: {self.compute_value_of_stats(self._stats)}"
                table.add_row(sum_values)
            
            if not suppress:
                console.print(table, justify="center")
            return table
    
    def get_outro_info(self):
        career_info = f"- You can either choose a career or pick a random one. Either way there no additional experience."
        exp_info = f"- Starting experience is [red]{STARTING_EXP}[/red]."
        return career_info + "\n" + exp_info + "\n"
    
    def get_set_of_stats(self):
        result = []
        while not self.is_stat_set_valid(result):
            result = []
            for _ in range(NUMBER_OF_STATS):
                result.append(randint(1, 10) + randint(1, 10))
        return result

    def is_stat_set_valid(self, result):
        if sum(result) == self.compute_value_of_stats(result):
            return MIN_VALUE_OF_STATS_SET_WITHOUT_HIGH_ROLLS <= self.compute_value_of_stats(result) <= MAX_VALUE_OF_STATS_SET
        return MIN_VALUE_OF_STATS_SET <= self.compute_value_of_stats(result) <= MAX_VALUE_OF_STATS_SET

    def compute_value_of_stats(self, stats):
        return sum([stat if stat not in ADDITIONAL_COST_FOR_STATS else ADDITIONAL_COST_FOR_STATS[stat] for stat in stats])

    def remove_used_talents(self, used_talents):
        if not used_talents:
            return
        detected_talents = self.detect_talents(used_talents)
        self._detected_talents = detected_talents

        for detected_talent in detected_talents:
            RANDOM_TALENTS.remove(detected_talent)

        console.print()
        console.print(self.get_detected_talents_table(), justify="center")
        console.print()
    
    def get_detected_talents_table(self):
        table = Table(title="Detected talents from random pool")

        table.add_column(f"Talent", justify="center", style="yellow")

        for detected_talent in self._detected_talents:
            table.add_row(f"{detected_talent.full_name}")

        return table

    def detect_talents(self, used_talents):
        talents = [talent.strip() for talent in used_talents.split(",")]

        detected_talents = []
        for talent in talents:
            for random_talent in RANDOM_TALENTS:
                if talent.lower() in random_talent.full_name.lower():
                    detected_talents.append(random_talent)
                    break
        return detected_talents

    def get_random_talents_table(self, number_of_random_talents):
        table = Table(title="Random Talents")

        table.add_column(f"#", justify="center", style="cyan")
        table.add_column(f"Talent A", justify="center")
        table.add_column(f"Talent B", justify="center")

        for idx in range(number_of_random_talents):
            first_talent = choice(RANDOM_TALENTS)
            RANDOM_TALENTS.remove(first_talent)

            second_talent = choice(RANDOM_TALENTS)
            RANDOM_TALENTS.remove(second_talent)

            table.add_row(f"{idx + 1}", f"{first_talent.full_name}", f"{second_talent.full_name}")

        return table

    def print_star_signs_info(self):
        table = Table(title="Star Signs")

        table.add_column(f"#", justify="center", style="cyan")
        table.add_column(f"Name", justify="center", style="yellow")
        table.add_column(f"Effect", justify="center")

        for idx, star_sign in enumerate(STAR_SIGNS):
            table.add_row(f"{idx + 1}", f"{star_sign.NAME}", f"{star_sign.EFFECT}")

        console.print(table, justify="center")
        console.print(f"You can either choose a star sign or pick a random one. Either way there no additional experience.")
        console.print(f"To select a star sign: Type a number visible near star sign you want to choose or type 0 for a random one.")
        console.print()
    
    def print_selected_star_sign_info(self):
        console.print()
        console.print(self._star_sign.get_table_with_star_sign(), justify="center")

    def handle_star_sign_selection(self):
        selected_number = Prompt.ask(f"Selected Star Sign")
        self.select_star_sign(selected_number)
    
    def select_star_sign(self, selected_number: str):
        try:
            star_sign_number = int(selected_number) - 1
        except Exception:
            console.print(f"[red]Error occurred when selecting a star sign!")
            raise typer.Abort()

        if not -1 <= star_sign_number <= len(STAR_SIGNS) - 1:
            console.print(f"[red]Error occurred when selecting a star sign!")
            raise typer.Abort()
        
        if star_sign_number == -1:
            star_sign = STAR_SIGNS_DISTRIBUTION.random_value
            accept = typer.confirm(f"Random race: {star_sign.NAME}. Do you accept randomly selected race?")

            if not accept:
                self.handle_star_sign_selection()
            else:
                self._star_sign = star_sign
        else:
            self._star_sign = STAR_SIGNS[star_sign_number]
    
    def print_final_panel(self, number_of_random_talents):
        console.print(60 * "\n")
        panel = Panel(
            Align.center(Columns([self.RACE.get_table_with_race(), self.print_selected_stats_info(suppress=True)], padding=(0, 30))),
            title="Final Panel",
            border_style="red",
            title_align="left",
            padding=(1, 2),
        )
        console.print(panel)
        panel = Panel(
            Align.center(Columns([self._star_sign.get_table_with_star_sign(), self.get_detected_talents_table()], padding=(0, 10))),
            title="Final Panel",
            border_style="red",
            title_align="left",
            padding=(1, 2),
        )
        console.print(panel)
        panel = Panel(
            Align.center(self.get_random_talents_table(number_of_random_talents)),
            title="Final Panel",
            border_style="red",
            title_align="left",
            padding=(1, 2),
        )
        console.print(panel)
        console.print(self.get_outro_info())
    
    def save_to_file(self):
        if not os.path.exists(DUMPS_DIRECTORY):
            os.makedirs(DUMPS_DIRECTORY)
        file_number = len([entry for entry in os.listdir(DUMPS_DIRECTORY) if os.path.isfile(os.path.join(DUMPS_DIRECTORY, entry))]) + 1
        console.save_html(f"{DUMPS_DIRECTORY}/character_{file_number}.html")


@app.command(help="Create a character.")
def main(
        number_of_random_talents: Annotated[int, typer.Argument(help="Number of random talents.")] = 3, 
        used_talents: Annotated[str, typer.Option(help="Already used talents. Add then with commas.")] = "",
    ):
    character = CharacterCreation()
    character.print_intro()
    character.remove_used_talents(used_talents)

    character.print_available_races()
    character.handle_race_selection()
    character.print_selected_race_info()

    character.print_stats_info()
    character.handle_stats_selection()
    character.print_selected_stats_info()

    character.print_star_signs_info()
    character.handle_star_sign_selection()
    character.print_selected_star_sign_info()

    character.print_final_panel(number_of_random_talents)
    character.save_to_file()
    

if __name__ == "__main__":
    app()
