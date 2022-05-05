import attr

# Common spades high scoreing
SUITS = "clubs diamonds hearts spades".split()


def _check_suit(instance, attribute, value):
    if not value in SUITS:
        raise ValueError(f"Allowed values are: `{'` `'.join(SUITS)}`")


@attr.define
class Suit:
    suit: str = attr.field(validator=[attr.validators.instance_of(str), _check_suit])

    def value(self) -> int:
        return SUITS.index(self.suit)
