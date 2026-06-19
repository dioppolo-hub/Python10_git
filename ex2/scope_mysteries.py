from typing import Callable, Any


def mage_counter() -> Callable:
    counter = 1

    def increment_counter() -> int:
        nonlocal counter
        print(f"call {counter}: {counter}")
        counter += 1
        return counter
    return increment_counter


def spell_accomulator(initial_power: int) -> Callable:
    power = initial_power

    def add_power(add: int) -> int:
        nonlocal power
        print(f"Base: {power}, add {add}: ", end="")
        power = power + add
        return power
    return add_power


def enchantment_factory(enchantment_type: str) -> Callable:

    def item_name(name: str) -> str:
        item = enchantment_type + " " + name
        return item
    return item_name


def memory_vault() -> dict[str, Callable]:
    vault = {}

    def store(key: str, value: Any) -> str:
        vault[key] = value
        return f"{key} stored"

    def recall(key: str) -> Any:
        return vault.get(key, "Memory not found")
    return {'store': store, 'recall': recall}


def main():
    print("Testing mage counter...")
    counta = mage_counter()
    countb = mage_counter()
    print("counter_a ", end="")
    counta()
    print("counter_a ", end="")
    counta()
    print("counter_b ", end="")
    countb()
    print("\nTesting spell accumulator...")
    print("=" * 40)
    pow = spell_accomulator(10)
    print(pow(0))
    print(pow(25))
    print("\nTesting enchantment factory...")
    print("=" * 40)
    flaming = enchantment_factory("flaming")
    print(flaming("sword"))
    print(flaming("staff"))
    water = enchantment_factory("Water")
    print(water("orb"))
    print("\nTesting memory vault...")
    print("=" * 40)
    vault = memory_vault()
    store_spell = vault['store']
    recall_spell = vault['recall']
    print("Storing Fireball:", store_spell("Fireball", 85))
    print("Storing Teleport:", store_spell("Teleport", "Need Mana"))
    print("Recalling Fireball:", recall_spell("Fireball"))
    print("Recalling Teleport:", recall_spell("Teleport"))
    print("Recalling Iceball:", recall_spell("IceBall"))


if __name__ == "__main__":
    main()
