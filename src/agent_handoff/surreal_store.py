from surrealdb import Surreal

from agent_handoff.models import A2AHandoff


class SurrealHandoffStore:
    def __init__(
        self,
        url: str,
        namespace: str,
        database: str,
        username: str,
        password: str,
    ):
        self.db = Surreal(url)
        self.namespace = namespace
        self.database = database
        self.username = username
        self.password = password

    async def connect(self):
        await self.db.signin({
            "username": self.username,
            "password": self.password,
        })

        await self.db.use(self.namespace, self.database)

    async def create_handoff(self, handoff: A2AHandoff):
        return await self.db.create(
            f"a2a_handoff:{handoff.id}",
            handoff.model_dump(),
        )

    async def get_handoff(self, handoff_id: str):
        return await self.db.select(f"a2a_handoff:{handoff_id}")

    async def update_status(self, handoff_id: str, status: str):
        return await self.db.merge(
            f"a2a_handoff:{handoff_id}",
            {
                "status": status,
            },
        )
