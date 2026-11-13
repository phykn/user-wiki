<div align="center">

# User Wiki

Cross-project preferences that make coding agents work your way.

![Python 3](https://img.shields.io/badge/python-3-blue)
![Last commit](https://img.shields.io/github/last-commit/phykn/user-wiki)

</div>

## Features

- Every task starts from one page, `graph/index.md`.
- Each kind of task is routed to only the pages it needs.
- It holds only confirmed preferences that change what an agent does.
- A checker verifies links, paths, and routes.

## Install

Ask an agent:

```text
Install my user wiki from https://github.com/phykn/user-wiki
```

To update it or apply it to another project, ask the same way. The agent follows `graph/setup.md`.

## Check

```sh
python3 scripts/check.py
```

Prints `WIKI_CHECK_OK`, or one problem per line.
