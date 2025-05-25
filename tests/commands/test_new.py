from pathlib import Path

from cleo.testers.command_tester import CommandTester
from pytest_mock import MockerFixture

from expanse_cli.main import app


def test_new_command(tmp_path: Path, mocker: MockerFixture) -> None:
    """
    The new command creates a new expanse project.
    """
    run_copy = mocker.patch("copier.run_copy")
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

    run_copy.assert_called_once_with(
        command.REPOSITORY_URL,
        str(tmp_path),
        vcs_ref="HEAD",
        quiet=True,
    )


def test_new_command_with_reference(tmp_path: Path, mocker: MockerFixture) -> None:
    """
    The new command creates a new expanse project based on Git reference.
    """
    run_copy = mocker.patch("copier.run_copy")
    command = app.find("new")
    tester = CommandTester(command)

    assert tester.execute(f"{tmp_path} -r 1.x") == 0

    run_copy.assert_called_once_with(
        command.REPOSITORY_URL,
        str(tmp_path),
        vcs_ref="1.x",
        quiet=True,
    )
