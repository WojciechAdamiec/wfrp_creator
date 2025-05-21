from weighted_set import WeightedSet


class StarSign:
    def __init__(self, name, effect, weighted_effect: WeightedSet=None):
        self._name = name
        self._effect = effect
        self._weighted_effect = weighted_effect
        self._selected_effect = self._make_selected_effect() if weighted_effect else effect
        self._full_name = self._make_full_name()

    @property
    def NAME(self):
        return self._name
    
    @property
    def EFFECT(self):
        return self._effect
    
    @property
    def FULL_NAME(self):
        return self._full_name
    
    @property
    def SELECTED_EFFECT(self):
        return self._selected_effect

    def _make_selected_effect(self):
        return self._weighted_effect.random_value
    
    def _make_full_name(self):
        current_full_name = f""
        current_full_name += f"[cyan]{self.NAME}[/cyan]"
        current_full_name += f" [green]({self.EFFECT})[/green]"
        return current_full_name