from random import choices


class SetValue:
    def __init__(self, value, weight: int):
        self.value = value
        self.weight = weight

    def __str__(self):
        return f"{self.weight}: {self.weight})"


class WeightedSet:
    def __init__(self, set_values: list[SetValue]):
        self._set_values = set_values
        self._values = [set_value.value for set_value in set_values]
    
    def __str__(self):
        return f"{self._values}"
    
    @property
    def random_value(self):
        return choices(
            [value.value for value in self._set_values],
            [value.weight for value in self._set_values],
        )[0]
    
    @property
    def values(self):
        return self._values
