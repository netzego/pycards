import attr

RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()


def _check_rank(instance, attribute, value):
    if not value in RANKS:
        raise ValueError(f"Allowed values are: `{'` `'.join(RANKS)}`")


@attr.define
class Rank:
    rank: str = attr.field(validator=[attr.validators.instance_of(str), _check_rank])

    def value(self) -> int:
        return RANKS.index(self.rank)
