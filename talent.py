class Talent:
    def __init__(self, name, description=""):
        self._name = name
        self._description = description
        self._full_name = self._make_full_name()

    @property
    def name(self):
        return self._name
    
    @property
    def description(self):
        return self._description
    
    @property
    def full_name(self):
        return self._full_name
    
    def _make_full_name(self):
        current_full_name = f""
        current_full_name += f"[cyan]{self.name}[/cyan]"
        if self.description:
            current_full_name += f" [green]({self.description})[/green]"
        return current_full_name
