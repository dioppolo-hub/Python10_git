import time
from typing import Callable
from functools import wraps


def spell_timer(func: Callable) -> Callable:

    @wraps(func)
    def wrapper():
        print(f"Casting {func.__name__}...")
        start_time = time.perf_counter()
        result = func()
        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f"Spell completed in {duration:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(self, spell_name: str, power: int):
            if power >= min_power:
                return func(self, spell_name, power)
            else:
                return "Insufficent power"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper():
            for attempt in range(1, max_attempts + 1):
                try:
                    return func()
                except Exception:
                    print(f"Spell failed, retrying... (attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return name.replace(" ", "").isalpha()

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main():
    print("Testing spell timer...")

    @spell_timer
    def fireball():
        time.sleep(0.101)
        return "Fireball cast!"
    print(f"Result: {fireball()}\n")
    print("\nTesting retrying spell...")

    @retry_spell(max_attempts=3)
    def unstable_spell():
        raise ValueError("Boom!")
    print(unstable_spell())
    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("Ro"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Firebolt", 5))


if __name__ == "__main__":
    main()