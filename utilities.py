import inspect
import time
from datetime import datetime, timezone
import os

import psutil
from rich import print as _print

def Print(logType: str, message: str) -> None:
    """
    Prints a log message with timestamp, function name, symbols wrapping the logType, and the message.
    """
    try:
        # Mapping of logType to symbols
        logTypeSymbols = {
            'SUCCESS': ('^^^', '^^^'),
            'FAILURE': ('###', '###'),
            'STATE': ('~~~', '~~~'),
            'INFO': ('---', '---'),
            'IMPORTANT': ('===', '==='),
            'CRITICAL': ('***', '***'),  # Changed symbols for CRITICAL
            'EXCEPTION': ('!!!', '!!!'),
            'WARNING': ('(((', ')))'),
            'DEBUG': ('[[[', ']]]'),
            'ATTEMPT': ('???', '???'),
            'STARTING': ('>>>', '>>>'),
            'PROGRESS': ('vvv', 'vvv'),
            'COMPLETED': ('<<<', '<<<'),
        }

        # Mapping of logType to styles
        logTypeStyles = {
            'SUCCESS': 'green',
            'FAILURE': 'red bold',
            'STATE': 'cyan',
            'INFO': 'blue',
            'IMPORTANT': 'magenta',
            'CRITICAL': 'red bold',
            'EXCEPTION': 'red bold',
            'WARNING': 'yellow',
            'DEBUG': 'white',
            'ATTEMPT': 'cyan',
            'STARTING': 'green',
            'PROGRESS': 'blue',
            'COMPLETED': 'green',
        }

        # Get current timestamp with microseconds
        current_time = time.time()
        timestamp = datetime.fromtimestamp(current_time, tz=timezone.utc).isoformat(timespec='microseconds') + 'Z'

        # Get symbols for the logType
        logTypeUpper = logType.upper()
        symbols = logTypeSymbols.get(logTypeUpper, ('', ''))
        before_symbol, after_symbol = symbols

        # Construct the formatted logType with symbols
        formattedLogType = f"{before_symbol} {logTypeUpper} {after_symbol}"

        # Apply style if available
        style = logTypeStyles.get(logTypeUpper, '')
        if style:
            formattedLogType = f"[{style}]{formattedLogType}[/{style}]"

        # Get the caller function name
        caller_frame = inspect.stack()[1]
        function_name = caller_frame.function

        # If the caller is Print, get the next frame
        if function_name == 'Print':
            caller_frame = inspect.stack()[2]
            function_name = caller_frame.function

        # Pad the function name for alignment (optional)
        functionNamePadding = 40
        paddedFunctionName = function_name.ljust(functionNamePadding)

        # Construct the output line
        output_line = f"{timestamp} {formattedLogType} {paddedFunctionName} {message}"

        # Print the output using rich
        _print(output_line)

    except Exception as e:
        error_message = f"Something went wrong when attempting to print.\nError: {e}"
        print(error_message)


def CPU_and_Mem_usage() -> str:
    """
    Returns a string with the CPU usage and memory usage of the current process.
    """
    current_process = psutil.Process(os.getpid())
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = current_process.memory_info()
    memory_usage_mb = memory_info.rss / (1024 ** 2)
    return f"CPU Usage: {cpu_usage}%, Process Memory Usage: {memory_usage_mb:.2f} MB"
