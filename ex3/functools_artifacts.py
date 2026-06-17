from functools import reduce, partial, lru_cache, singledispatch
import operator
from typing import List, Callable, Any


def spell_reducer(spells: List[int], operation: str) -> int:
	if not spells:
		return 0
	ops = {
		"add": operator.add,
		"multiply": operator.mul,
		"max": max,
		"min": min
	}
	if operation not in ops:
		raise ValueError(f"Unknown operation {operation}")
	return reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
	fire_enchant = partial(base_enchantment, 50, "Fire")
	ice_enchant = partial(base_enchantment, 50, "Ice")
	lightning_enchant = partial(base_enchantment, 50, "Lightning")
	return {
		"fire": fire_enchant,
		"ice": ice_enchant,
		"lightning": lightning_enchant
	}


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
	if n < 0:
		raise ValueError("Index must be positive or zero")
	elif n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
	@singledispatch
	def base_dispatcher(spell: Any) -> str:
		return f"Unknown spell type: {type(spell).__name__}"

	@base_dispatcher.register(int)
	def _(spell: int) -> str:
		return f"Damage Spell: Dealt {spell} points of dmg!"

	@base_dispatcher.register(str)
	def _(spell: str) -> str:
		return f"Enchantment Spell: casted {spell}"

	@base_dispatcher.register(list)
	def _(spell: list) -> str:
		return f"Multi-cast Spell: Casting {len(spell)} spells in a row!"
	return base_dispatcher


def cast_spell(power: int, element: str, target: str) -> str:
	return f"[Power: {power}] | Element: {element} -> spell used on {target}"


def main():
	print("Testing spell reducer...")
	sample_spells = [10, 20, 30, 40]
	print(f"Sum: {spell_reducer(sample_spells, 'add')}")
	print(f"Product: {spell_reducer(sample_spells, 'multiply')}")
	print(f"Max: {spell_reducer(sample_spells, 'max')}")
	print("\nTesting partial enchanter...")
	spell_book = partial_enchanter(cast_spell)
	fire_spell = spell_book["fire"]
	ice_spell = spell_book["ice"]
	lightning_spell = spell_book["lightning"]
	print(fire_spell(target="Red Dragon"))
	print(ice_spell(target="Stone Golem"))
	print(lightning_spell(target="Frank"))
	print("\nTesting memoized fibonacci...")
	print(f"Fib(0): {memoized_fibonacci(0)}")
	print(f"Fib(1): {memoized_fibonacci(1)}")
	print(f"Fib(10): {memoized_fibonacci(10)}")
	print(f"Fib(15): {memoized_fibonacci(15)}")
	print("\nTesting spell dispatcher...")
	dispatcher = spell_dispatcher()
	print(dispatcher(42))
	print(dispatcher("Fireball"))
	print(dispatcher([1, 2, 3]))
	print(dispatcher(3.14))


if __name__ == "__main__":
	main()
