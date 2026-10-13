from typing import Any


class Event(list):
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for item in self:
            item(*args, **kwds)


class Game:
    def __init__(self) -> None:
        self.events = Event()

    def fire(self, args):
        self.events(args)

class GoalScoredInfo:
    def __init__(self, scorer, goals_scored) -> None:
        self.scorer = scorer
        self.goals_scored = goals_scored

class Player:
    def __init__(self, name, game) -> None:
        self.name = name
        self.game = game
        self.goals_scored = 0

    def score(self):
        self.goals_scored += 1
        goal = GoalScoredInfo(self.name, self.goals_scored)
        self.game.fire(goal)

class Coach:
    def __init__(self, game) -> None:
        game.events.append(self.celebrate_goal)

    def celebrate_goal(self, args):
        if isinstance(args, GoalScoredInfo) and args.goals_scored < 3:
            print(f"Coach says well done {args.scorer}")


if __name__ == "__main__":
    game = Game()
    player = Player("Sam", game)
    coach = Coach(game)
    player.score()
    player.score()
    player.score()
