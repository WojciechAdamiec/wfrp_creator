from star_sign import StarSign
from weighted_set import WeightedSet, SetValue


WYMUND = StarSign(
    name="Wymund the Anchorite",
    effect="[green]+2 Fellowship[/green], [green]+2 Initiative[/green], [red]-3 Intelligence[/red]"
)

BIG_CROSS = StarSign(
    name="The Big Cross",
    effect="[green]+2 Strength[/green], [green]+2 Willpower[/green], [red]-3 Initiative[/red]"
)

LIMNERS_LINE = StarSign(
    name="The Limner’s Line",
    effect="[green]+2 Ballistic Skill[/green], [green]+2 Agility[/green], [red]-3 Weapon Skill[/red]"
)

GNUTHUS = StarSign(
    name="Gnuthus the Ox",
    effect="[green]+2 Toughness[/green], [green]+2 Willpower[/green], [red]-3 Intelligence[/red]"
)

DRAGOMAS = StarSign(
    name="Dragomas the Drake",
    effect="[green]+2 Willpower[/green], [green]+2 Fellowship[/green], [red]-3 Dexterity[/red]"
)

GLOAMING = StarSign(
    name="The Gloaming",
    effect="[green]+2 Intelligence[/green], [green]+2 Initiative[/green], [red]-3 Willpower[/red]"
)

GRUNGNIS_BALDRIC = StarSign(
    name="Grungni’s Baldric",
    effect="[green]+2 Weapon Skill[/green], [green]+2 Willpower[/green], [red]-3 Fellowship[/red]"
)

MAMMIT_WISE = StarSign(
    name="Mammit the Wise",
    effect="[green]+2 Initiative[/green], [green]+2 Intelligence[/green], [red]-3 Fellowship[/red]"
)

MAMMIT_FOOL = StarSign(
    name="Mammit the Fool",
    effect="Gain one level of the [cyan]Luck[/cyan] Talent, [red]-3 Willpower[/red]"
)

TWO_BULLOCKS = StarSign(
    name="The Two Bullocks",
    effect="Gain one level of the [cyan]Craftsman[/cyan] Talent, [red]-3 Intelligence[/red]"
)

DANCER = StarSign(
    name="The Dancer",
    effect="Gain one level of the [cyan]Impassioned Zeal[/cyan] Talent, [red]-3 Initiative[/red]"
)

DRUMMER = StarSign(
    name="The Drummer",
    effect="Gain one level of the [cyan]Carouser[/cyan] Talent, [red]-3 Willpower[/red]"
)

PIPER = StarSign(
    name="The Piper",
    effect="[green]+2 Fellowship[/green], [green]+2 Dexterity[/green], [red]-3 Weapon Skill[/red]"
)

VOBIST = StarSign(
    name="Vobist the Faint",
    effect="Gain one level of the [cyan]Sixth Sense[/cyan] Talent, [red]-3 Initiative[/red]"
)

BROKEN_CART = StarSign(
    name="The Broken Cart",
    effect="Gain one level of the [cyan]Resistance (Disease)[/cyan] Talent, [red]-3 Willpower[/red]"
)

GREASED_GOAT = StarSign(
    name="The Greased Goat",
    effect="Gain one level of the [cyan]Animal Affinity[/cyan] Talent, [red]-3 Toughness[/red]"
)

RHYAS_CAULDRON = StarSign(
    name="Rhya’s Cauldron",
    effect="Gain one level of the [cyan]Iron Will[/cyan] Talent, [red]-3 Agility[/red]"
)

CACKLEFAX = StarSign(
    name="Cacklefak the Cockerel",
    effect="Gain one level of the [cyan]Dealmaker[/cyan] Talent, [red]-3 Fellowship[/red]"
)

BONESAW = StarSign(
    name="The Bonesaw",
    effect="[green]+2 Intelligence[/green], [green]+2 Fellowship[/green], [red]-3 Weapon Skill[/red]"
)

WITCHLING_STAR = StarSign(
    name="The Witchling Star",
    effect=(
        "Roll a d10:\n"
        "1-3: Gain the [cyan]Sixth Sense[/cyan] Talent\n"
        "4-6: Gain the [cyan]Second Sight[/cyan] Talent, [red]-3 Strength[/red]\n"
        "7-9: Gain the [cyan]Petty Magic[/cyan] Talent, [red]-3 Strength[/red]\n"
        "10: Gain the [cyan]Witch![/cyan] Talent, [red]-5 Strength[/red]"
    ),
    weighted_effect=WeightedSet([
        SetValue("Gain the [cyan]Sixth Sense[/cyan] Talent", 3),
        SetValue("Gain the [cyan]Second Sight[/cyan] Talent, [red]-3 Strength[/red]", 3),
        SetValue("Gain the [cyan]Petty Magic[/cyan] Talent, [red]-3 Strength[/red]", 3),
        SetValue("Gain the [cyan]Witch![/cyan] Talent, [red]-5 Strength[/red]", 1),
    ]),
)


STAR_SIGNS_DISTRIBUTION = WeightedSet([
    SetValue(WYMUND, 1),
    SetValue(BIG_CROSS, 1),
    SetValue(LIMNERS_LINE, 1),
    SetValue(GNUTHUS, 1),
    SetValue(DRAGOMAS, 1),
    SetValue(GLOAMING, 1),
    SetValue(GRUNGNIS_BALDRIC, 1),
    SetValue(MAMMIT_WISE, 1),
    SetValue(MAMMIT_FOOL, 1),
    SetValue(TWO_BULLOCKS, 1),
    SetValue(DANCER, 1),
    SetValue(DRUMMER, 1),
    SetValue(PIPER, 1),
    SetValue(VOBIST, 1),
    SetValue(BROKEN_CART, 1),
    SetValue(GREASED_GOAT, 1),
    SetValue(RHYAS_CAULDRON, 1),
    SetValue(CACKLEFAX, 1),
    SetValue(BONESAW, 1),
    SetValue(WITCHLING_STAR, 1),
])


STAR_SIGNS = STAR_SIGNS_DISTRIBUTION.values
