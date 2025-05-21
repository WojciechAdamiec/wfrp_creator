from enum import Enum
from rich.table import Table
from visuals import get_color_cycle


NUMBER_OF_RACE_STATS = 10


class Size(Enum):
    TINY = f"TINY"
    LITTLE = f"LITTLE"
    SMALL = f"[red]SMALL[/red]"
    AVERAGE = f"[cyan]AVERAGE[/cyan]"
    LARGE = f"[green]LARGE[/green]"
    ENORMOUS = f"ENORMOUS"
    MONSTROUS = f"MONSTROUS"


class Wounds(Enum):
    SMALL = "(2x[red]TB[/red])+[deep_sky_blue1]WPB[/deep_sky_blue1]"
    REGULAR = "[green]SB[/green]+(2x[red]TB[/red])+[deep_sky_blue1]WPB[/deep_sky_blue1]"
    BIG = "2x([green]SB[/green]+(2x[red]TB[/red])+[deep_sky_blue1]WPB[/deep_sky_blue1])"
    

class Race:
    def __init__(
        self,
        name: str,
        size: Size,
        weapon_skill: int,
        ballistic_skill: int,
        strength: int,
        toughness: int,
        initiative: int,
        agility: int,
        dexterity: int,
        intelligence: int,
        willpower: int,
        fellowship: int,
        fate: int,
        resilience: int,
        extra_points: int,
        movement: int,
        wounds: Wounds,
    ):
        self._name = name
        self._size = size

        self._weapon_skill = weapon_skill
        self._ballistic_skill = ballistic_skill
        self._strength = strength
        self._toughness = toughness
        self._initiative = initiative
        self._agility = agility
        self._dexterity = dexterity
        self._intelligence = intelligence
        self._willpower = willpower
        self._fellowship = fellowship

        self._fate = fate
        self._resilience = resilience
        self._extra_points = extra_points
        self._movement = movement
        self._wounds = wounds
    
    @property
    def NAME(self) -> str:
        return self._name
    
    @property
    def SIZE(self) -> Size:
        return self._size.value
    
    @property
    def WS(self) -> int:
        return self._weapon_skill

    @property
    def BS(self) -> int:
        return self._ballistic_skill
    
    @property
    def S(self) -> int:
        return self._strength
    
    @property
    def T(self) -> int:
        return self._toughness
    
    @property
    def I(self) -> int:
        return self._initiative
    
    @property
    def AG(self) -> int:
        return self._agility
    
    @property
    def DEX(self) -> int:
        return self._dexterity
    
    @property
    def INT(self) -> int:
        return self._intelligence
    
    @property
    def WP(self) -> int:
        return self._willpower
    
    @property
    def FEL(self) -> int:
        return self._fellowship
    
    @property
    def FATE(self) -> int:
        return self._fate
    
    @property
    def RESILIENCE(self) -> int:
        return self._resilience
    
    @property
    def EXTRA_POINTS(self) -> int:
        return self._extra_points
    
    @property
    def MOVEMENT(self) -> int:
        return self._movement
    
    @property
    def WOUNDS(self) -> Wounds:
        return self._wounds.value

    def get_table_with_race(self, num=None):
        colors = get_color_cycle()

        num_text = ""
        if num:
            num_text = f"([bold][cyan]{num}[/cyan][/bold]): "

        table = Table(title=f"{num_text}{self.NAME}", caption=f"SIZE: {self.SIZE}\n\nWOUNDS:\n{self.WOUNDS}")

        table.add_column(f"STAT", justify="left")
        table.add_column(f"VALUE", justify="center")

        table.add_row(f"WS", f"{self.WS}", style=next(colors))
        table.add_row(f"BS", f"{self.BS}", style=next(colors))
        table.add_row(f"S", f"{self.S}", style=next(colors))
        table.add_row(f"T", f"{self.T}", style=next(colors))
        table.add_row(f"I", f"{self.I}", style=next(colors))
        table.add_row(f"AG", f"{self.AG}", style=next(colors))
        table.add_row(f"DEX", f"{self.DEX}", style=next(colors))
        table.add_row(f"INT", f"{self.INT}", style=next(colors))
        table.add_row(f"WP", f"{self.WP}", style=next(colors))
        table.add_row(f"FEL", f"{self.FEL}", style=next(colors))
        table.add_row(f"", f"")

        colors = get_color_cycle()
        table.add_row(f"FATE", f"{self.FATE}", style=next(colors))
        table.add_row(f"RES", f"{self.RESILIENCE}", style=next(colors))
        table.add_row(f"EXTRA", f"{self.EXTRA_POINTS}", style=next(colors))
        table.add_row(f"MOVE", f"{self.MOVEMENT}", style=next(colors))
        
        return table
