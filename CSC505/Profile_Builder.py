from typing import List

class DeveloperProfile:
    def __init__(self) -> None:
        self.name: str = "Unnamed"
        self.traits: List[str] = []
        self.signals: List[str] = []
        self.teamPractices: List[str] = []

    def summary(self) -> str:
        return (
            f"Developer Profile: {self.name}\n"
            f"- Traits: {', '.join(self.traits) or '(none)'}\n"
            f"- Behavioral signals: {', '.join(self.signals) or '(none)'}\n"
            f"- Team practices: {', '.join(self.teamPractices) or '(none)'}"
        )

class ProfileBuilder:
    def __init__(self) -> None:
        self.reset()
        self.steps_executed: List[str] = []

    def reset(self) -> None:
        self._product = DeveloperProfile()

    def setName(self, name: str) -> "ProfileBuilder":
        self._product.name = name
        self.steps_executed.append("setName")
        return self

    def addTrait(self, trait: str) -> "ProfileBuilder":
        self._product.traits.append(trait)
        self.steps_executed.append("addTrait")
        return self

    def addSignal(self, signal: str) -> "ProfileBuilder":
        self._product.signals.append(signal)
        self.steps_executed.append("addSignal")
        return self

    def addTeamPractice(self, practice: str) -> "ProfileBuilder":
        self._product.teamPractices.append(practice)
        self.steps_executed.append("addTeamPractice")
        return self

    def getResult(self) -> DeveloperProfile:
        self.steps_executed.append("getResult")
        return self._product

class Director:
    """Predefined recipes for building profiles."""
    def buildMinimal(self, b: ProfileBuilder, name: str) -> DeveloperProfile:
        b.reset()
        (b.setName(name)
          .addTrait("Curiosity & Continuous Learning")
          .addSignal("Runs small experiments; reads docs/tests")
          .addTeamPractice("Lightweight design notes"))
        return b.getResult()

    def buildCollaborative(self, b: ProfileBuilder, name: str) -> DeveloperProfile:
        b.reset()
        (b.setName(name)
          .addTrait("Ownership & Conscientiousness")
          .addSignal("Surfaces risks early; writes tests")
          .addTrait("Communication & Collaboration")
          .addSignal("Seeks feedback; documents decisions")
          .addTeamPractice("Code reviews")
          .addTeamPractice("Pairing / Mob sessions")
          .addTeamPractice("Decision records (ADR)"))
        return b.getResult()

def main():
    print("=== Developer Profile Builder Demo ===\n")

    director = Director()
    builder = ProfileBuilder()

    # Choose one recipe for the demo
    profile = director.buildCollaborative(builder, name="Exemplary Dev")

    # Brief description
    description = (
        "This demo uses a Builder-like sequence to assemble a developer profile.\n"
        "It captures three common traits (curiosity, ownership, communication),\n"
        "maps them to observable signals, and adds team practices that reinforce them."
    )

    # Print description, steps, count, and profile summary
    print(description)
    print("\nSteps executed (in order):")
    for s in builder.steps_executed:
        print(f" - {s}")
    print(f"\nNumber of steps: {len(builder.steps_executed)}\n")

    print(profile.summary())

if __name__ == "__main__":
    main()
