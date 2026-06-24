from dataclasses import dataclass, field


@dataclass
class Task:
    name: str
    duration_minutes: int
    priority: str
    category: str
    is_recurring: bool = False
    frequency: str = ""
    is_complete: bool = False

    def mark_complete(self) -> None:
        pass


@dataclass
class Pet:
    name: str
    species: str
    breed: str
    age: int
    tasks: list = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        pass

    def remove_task(self, task: Task) -> None:
        pass

    def get_tasks(self) -> list:
        pass


@dataclass
class Owner:
    name: str
    available_minutes: int
    preferences: list = field(default_factory=list)
    pets: list = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        pass

    def remove_pet(self, pet: Pet) -> None:
        pass


class Scheduler:
    def __init__(self, owner: Owner, pet: Pet):
        self.owner = owner
        self.pet = pet
        self.plan: list = []

    def generate_plan(self) -> list:
        pass

    def sort_tasks(self) -> list:
        pass

    def filter_by_time(self) -> list:
        pass

    def explain_plan(self) -> str:
        pass
