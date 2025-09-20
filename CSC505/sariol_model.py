def ask(prompt: str) -> str:
    return input(f"{prompt}: ").strip()

def ask_list(prompt: str):
    raw = input(f"{prompt} (comma-separated): ").strip()
    return [x.strip() for x in raw.split(",")] if raw else []

def main():
    print("=== Sariol Model — Quick Input ===")

    # Discovery / Risk Spike
    top_risks = ask_list("Top risks to de-risk first")
    spike_goal = ask("Prototype / spike goal")

    # Communication
    problem = ask("Problem statement")
    stakeholders = ask_list("Stakeholders")
    success_metrics = ask_list("Success metrics")

    # Planning
    schedule = ask("Schedule overview (e.g., 3 sprints x 2 weeks)")
    estimation = ask("Estimation approach (e.g., story points)")
    
    # Modeling
    key_requirements = ask_list("Key requirements")
    arch_notes = ask_list("Architecture notes / key decisions")

    # Construction + Continuous V&V
    coding_standards = ask_list("Coding standards (e.g., PEP8, linters)")
    testing = ask_list("Testing (e.g., unit, property-based, security)")
    integration = ask("Integration cadence (e.g., CI per commit)")

    # Deployment + Feedback
    release_strategy = ask("Release strategy (e.g., canary, blue/green)")
    telemetry = ask_list("Telemetry to watch (e.g., latency, error_rate)")
    feedback_channels = ask_list("User feedback channels (e.g., in-app survey)")

    # Change Queue / Triage
    small_policy = ask("Policy for SMALL changes (how to flow)")
    large_policy = ask("Policy for LARGE changes (how to re-plan)")

    # ---- Output ----
    print("\n=== Sariol Model — Summary ===")
    print("Discovery / Risk Spike")
    print(f"  Spike goal: {spike_goal}")
    print(f"  Top risks: {', '.join(top_risks) if top_risks else '(none)'}")

    print("\nCommunication")
    print(f"  Problem: {problem}")
    print(f"  Stakeholders: {', '.join(stakeholders) if stakeholders else '(none)'}")
    print(f"  Success metrics: {', '.join(success_metrics) if success_metrics else '(none)'}")

    print("\nPlanning")
    print(f"  Schedule: {schedule}")
    print(f"  Estimation: {estimation}")

    print("\nModeling")
    print(f"  Key requirements: {', '.join(key_requirements) if key_requirements else '(none)'}")
    print(f"  Architecture notes: {', '.join(arch_notes) if arch_notes else '(none)'}")

    print("\nConstruction + Continuous V&V")
    print(f"  Coding standards: {', '.join(coding_standards) if coding_standards else '(none)'}")
    print(f"  Testing: {', '.join(testing) if testing else '(none)'}")
    print(f"  Integration cadence: {integration}")

    print("\nDeployment + Feedback")
    print(f"  Release strategy: {release_strategy}")
    print(f"  Telemetry: {', '.join(telemetry) if telemetry else '(none)'}")
    print(f"  Feedback channels: {', '.join(feedback_channels) if feedback_channels else '(none)'}")

    print("\nChange Queue / Triage")
    print(f"  Small changes: {small_policy}")
    print(f"  Large changes: {large_policy}")
    print("\n=== End ===")

if __name__ == '__main__':
    main()
