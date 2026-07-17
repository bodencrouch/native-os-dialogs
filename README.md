# native-os-dialogs

Native message boxes, file/folder browsers, and related OS dialog helpers for Windows, Linux, and macOS.

v0 excludes Win32 job objects (see `app-process-lifecycle`) and the large FSCTL / statresult test dump.

## Install

```bash
pip install -e .
```

## Origin

Extracted from PyKotor `utility/system/{win32,Linux,darwin}/`.

Complements [`python-os-helpers`](https://github.com/bodencrouch/python-os-helpers) (path/frozen-app helpers).

## License

LGPL-3.0-or-later
