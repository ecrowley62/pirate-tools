from abc import ABC, abstractmethod

# Base builder class and the builder director

class CommandExecutionPlanBuilder(ABC):
    """
    Abstract interface for specifying methods used to build a command execution plan
    object. These objects perform the logic desired for the given command
    """

    @property
    @abstractmethod
    def command(self) -> None:
        pass

    @abstractmethod
    def parse_input(self) -> None:
        pass

class CommandBuilderDirector:
    
    def __init__(self) -> None:
        self._command = None

    @property
    def command(self) -> None:
        return self._command
    
    @command.setter
    def command(self, command: CommandExecutionPlanBuilder) -> None:
        self._command = command

    def produce_command_dryrun(self) -> None:
        pass

    def produce_command_run(self) -> None:
        self.command.parse_input()

# Command specific data objects (ExecutionPlan) and corresponding builder classes

"""
Rename a given file or files from whatever mixed up pirate sytax was used
to something clean
"""

class RenameCommandExecutionPlan:
    """
    Object containing information needed to execute a Rename command 
    """
    def __init__(self) -> None:
        self.target_file: str = None
        self.is_directory: bool = None
        self.recurse: bool = None


class RenameBuilder(CommandExecutionPlanBuilder):
    """
    Builder for creating Rename command execution plans
    """

    def __init__(self) -> None:
        """
        A new builder should contain a fresh/clean execution plan
        """
        self.reset()

    def reset(self) -> None:
        self._command = RenameCommandExecutionPlan()

    @property
    def command(self) -> RenameCommandExecutionPlan:
        """
        Return the built command and reset this builder to a clean state
        """
        command = self._command
        self.reset()
        return command
    
    def parse_input(self, target_file: str, recurse: bool = False) -> None:
        pass



