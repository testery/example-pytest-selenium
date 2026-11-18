"""
Tiny file-polling REPL for driving a paused Selenium session interactively.

Windows can't reliably hand a FIFO-backed stdin to a native Win32 python.exe
launched from a Unix-style shell (git-bash/MSYS) -- pdb's input() call just
gets "OSError: [Errno 9] Bad file descriptor". So instead of routing
commands through real pdb + stdin, this polls a plain command file for new
lines, executes each against the paused test's local variables (so
`selenium` etc. are already in scope -- no frame-climbing needed), and
appends results/tracebacks to a plain output file.

Write `__CONTINUE__` as a line in the command file to end the session and
let the test proceed.
"""
import time
import traceback
from pathlib import Path

DEFAULT_DIR = Path(__file__).parent / ".live_repl"


def live_repl(local_vars, cmd_path=None, out_path=None, poll_interval=0.3):
    cmd_path = Path(cmd_path) if cmd_path else DEFAULT_DIR / "cmd.txt"
    out_path = Path(out_path) if out_path else DEFAULT_DIR / "out.log"
    cmd_path.parent.mkdir(parents=True, exist_ok=True)
    cmd_path.write_text("", encoding="utf-8")
    out_path.write_text("", encoding="utf-8")

    env = dict(local_vars)
    seen = 0

    while True:
        lines = cmd_path.read_text(encoding="utf-8").splitlines()
        new_lines = lines[seen:]
        seen = len(lines)

        for line in new_lines:
            stripped = line.strip()
            if not stripped:
                continue
            if stripped == "__CONTINUE__":
                return env

            with out_path.open("a", encoding="utf-8") as f:
                f.write(f">>> {line}\n")
                try:
                    try:
                        result = eval(line, env)
                        if result is not None:
                            f.write(f"{result!r}\n")
                    except SyntaxError:
                        exec(line, env)
                except Exception:
                    f.write(traceback.format_exc())
                f.write("\n")

        time.sleep(poll_interval)
