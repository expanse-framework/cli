from pathlib import Path

from cleo.testers.command_tester import CommandTester

from expanse_cli.main import app


def test_new_command(tmp_path: Path) -> None:
    """
    The new command creates a new expanse project.
    """
    command = app.find("new")
    tester = CommandTester(command)

    assert tester.execute(str(tmp_path)) == 0

    output = tester.io.fetch_output()

    assert (
        output
        == f"""
███████╗██╗  ██╗██████╗  █████╗ ███╗   ██╗███████╗███████╗
██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗████╗  ██║██╔════╝██╔════╝
█████╗   ╚███╔╝ ██████╔╝███████║██╔██╗ ██║███████╗█████╗
██╔══╝   ██╔██╗ ██╔═══╝ ██╔══██║██║╚██╗██║╚════██║██╔══╝
███████╗██╔╝ ██╗██║     ██║  ██║██║ ╚████║███████║███████╗
╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝

• Creating a new Expanse project at {tmp_path}...\x1b[1G\x1b[2K\
• Created a new Expanse project at {tmp_path}.
"""
    )
