from dataclasses import dataclass, field


@dataclass
class WithOMSId:
    oms_id: int = field(default=1, init=False)

    def __post_init__(self):
        object.__setattr__(self, 'oms_id', 1)
