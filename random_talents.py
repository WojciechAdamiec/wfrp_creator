from talent import Talent


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