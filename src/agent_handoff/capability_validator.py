from agent_handoff.models import A2AHandoff


class CapabilityValidationError(ValueError):
    pass


class CapabilityValidator:
    def __init__(
        self,
        available_skills: list[str],
        available_tools: list[str],
    ):
        self.available_skills = set(available_skills)
        self.available_tools = set(available_tools)

    def validate(self, handoff: A2AHandoff):
        missing_skills = []
        missing_tools = []

        for skill in handoff.capabilities.required_skills:
            if skill not in self.available_skills:
                missing_skills.append(skill)

        for tool in handoff.capabilities.required_tools:
            if tool not in self.available_tools:
                missing_tools.append(tool)

        handoff.capabilities.missing_skills = missing_skills
        handoff.capabilities.missing_tools = missing_tools

        if missing_skills or missing_tools:
            raise CapabilityValidationError(
                f"A2A handoff capability mismatch. Missing skills={missing_skills}, missing tools={missing_tools}"
            )

        return handoff
