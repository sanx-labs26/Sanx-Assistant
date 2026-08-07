from assistant_router import AssistantRouter
from commands import handle_task_command

router = AssistantRouter()


async def process_command(session, command):

    command = command.strip()

    # Task Manager
    task = handle_task_command(command)

    if task:
        await session.say(task)
        return True

    # Router
    result = router.route(command)

    if result:
        print(result)
        return True

    return False