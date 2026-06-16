from typing import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restore {target} for {power} HP"


def LightingBolt(target: str, power: int) -> str:
    return f"LightingBolt hit {target} for {power} dmg"


def fireball(target: str, power: int) -> str:
    return f"Fireball deals {power} dmg to {target}"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    if not callable(spell1) or not callable(spell2):
        raise TypeError("[Error]: Le spell devono essere 'callable'")

    def combined_spell(target: str, power: int) -> str:
        new_spell = f"{spell1(target, power)} and {spell2(target, power)}"
        return new_spell
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    if not callable(base_spell):
        raise TypeError("[Error]: Base_spell deve essere 'callable'")

    def amplified_spell(target: str, power: int) -> Callable:
        new_spell = power * multiplier
        return base_spell(target, new_spell)
    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    if not callable(condition) or not callable(spell):
        raise TypeError("[Error]: Le spell devono essere 'callable'")

    def conditional_spell(target: str, power: int) -> str:
        if condition(power):
            return spell(target, power)
        else:
            return "Spell Fizzled"
    return conditional_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    for spell in spells:
        if not callable(spell):
            raise TypeError("[Error] La spell deve essere 'callable'")

    def cast_spell(target: str, power: int) -> list[Callable]:
        results = []
        for spell in spells:
            result = spell(target, power)
            results.append(result)
        return results
    return cast_spell


def condition(power: int) -> bool:
    if power >= 50:
        return True
    else:
        return False


def main():
    print("Trying combiner...")
    comb = spell_combiner(fireball, heal)
    print(comb("Frank", 50))
    print("\nTrying amplifier...")
    pow = power_amplifier(LightingBolt, 4)
    print(pow("Bob", 75))
    print("\nTrying conditional...")
    cond1 = conditional_caster(condition, heal)
    cond2 = conditional_caster(condition, LightingBolt)
    print(cond1("Itself", 25))
    print(cond2("Sinner", 75))
    print("\nTrying sequence...")
    spell_list = [
        fireball,
        heal,
        LightingBolt
        ]
    seq = spell_sequence(spell_list)
    print(seq("Donald D. Trump", 50))


if __name__ == "__main__":
    main()
