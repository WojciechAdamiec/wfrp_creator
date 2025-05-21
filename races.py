from race import Race, Size, Wounds
from weighted_set import WeightedSet, SetValue


HUMAN = Race(
    name="Human",
    size=Size.AVERAGE,
    weapon_skill=20,
    ballistic_skill=20,
    strength=20,
    toughness=20,
    initiative=20,
    agility=20,
    dexterity=20,
    intelligence=20,
    willpower=20,
    fellowship=20,
    fate=2,
    resilience=1,
    extra_points=3,
    movement=4,
    wounds=Wounds.REGULAR
)

DWARF = Race(
    name="Dwarf",
    size=Size.AVERAGE,
    weapon_skill=30,
    ballistic_skill=20,
    strength=20,
    toughness=30,
    initiative=20,
    agility=10,
    dexterity=30,
    intelligence=20,
    willpower=40,
    fellowship=10,
    fate=0,
    resilience=2,
    extra_points=2,
    movement=3,
    wounds=Wounds.REGULAR
)

HALFLING = Race(
    name="Halfling",
    size=Size.SMALL,
    weapon_skill=10,
    ballistic_skill=30,
    strength=10,
    toughness=20,
    initiative=20,
    agility=20,
    dexterity=30,
    intelligence=20,
    willpower=30,
    fellowship=30,
    fate=0,
    resilience=2,
    extra_points=3,
    movement=3,
    wounds=Wounds.SMALL
)

ELF = Race(
    name="Elf",
    size=Size.AVERAGE,
    weapon_skill=30,
    ballistic_skill=30,
    strength=20,
    toughness=20,
    initiative=40,
    agility=30,
    dexterity=30,
    intelligence=30,
    willpower=30,
    fellowship=20,
    fate=0,
    resilience=0,
    extra_points=2,
    movement=5,
    wounds=Wounds.REGULAR
)

GNOME = Race(
    name="Gnome",
    size=Size.SMALL,
    weapon_skill=20,
    ballistic_skill=10,
    strength=10,
    toughness=15,
    initiative=30,
    agility=30,
    dexterity=30,
    intelligence=30,
    willpower=40,
    fellowship=15,
    fate=2,
    resilience=0,
    extra_points=2,
    movement=3,
    wounds=Wounds.SMALL
)

OGRE = Race(
    name="Ogre",
    size=Size.LARGE,
    weapon_skill=20,
    ballistic_skill=10,
    strength=35,
    toughness=35,
    initiative=0,
    agility=15,
    dexterity=10,
    intelligence=10,
    willpower=20,
    fellowship=10,
    fate=0,
    resilience=3,
    extra_points=1,
    movement=6,
    wounds=Wounds.BIG
)

RACES_DISTRIBUTION = WeightedSet([
    SetValue(HUMAN, 88),
    SetValue(DWARF, 4),
    SetValue(HALFLING, 4),
    SetValue(ELF, 2),
    SetValue(GNOME, 1),
    SetValue(OGRE, 1),
])

RACES = RACES_DISTRIBUTION.values
