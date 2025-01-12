from typing import ClassVar

from cleo.commands.command import Command
from cleo.helpers import argument
from cleo.io.inputs.argument import Argument


class NewCommand(Command):
    name: str = "new"

    description = "Create a new Expanse project."

    arguments: ClassVar[list[Argument]] = [
        argument("path", "The path where the new project will be created.")
    ]

    REPOSITORY_URL = "https://github.com/expanse-framework/app.git"

    def handle(self) -> int:
        self.line(r"""<fg=blue>
███████╗██╗  ██╗██████╗  █████╗ ███╗   ██╗███████╗███████╗
██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗████╗  ██║██╔════╝██╔════╝
█████╗   ╚███╔╝ ██████╔╝███████║██╔██╗ ██║███████╗█████╗
██╔══╝   ██╔██╗ ██╔═══╝ ██╔══██║██║╚██╗██║╚════██║██╔══╝
███████╗██╔╝ ██╗██║     ██║  ██║██║ ╚████║███████║███████╗
╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝
</>""")
        path = self.argument("path")

        from copier import run_copy

        run_copy("../app", path)

        return 0
