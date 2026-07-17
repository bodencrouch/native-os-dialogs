"""Native OS dialogs (message box / file-folder browser)."""
import sys

def messagebox(*args, **kwargs):
    if sys.platform == "win32":
        from native_os_dialogs.win32 import messagebox as m
    elif sys.platform == "darwin":
        from native_os_dialogs.darwin import messagebox as m
    else:
        from native_os_dialogs.linux import messagebox as m
    return m

__all__ = ["messagebox"]
