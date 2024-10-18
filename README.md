# Beepy Web Radio

## Overview

This is a Beepy app to play web radio, powered by [radio.garden](http://radio.garden). The application is written in Python, using [Textual](https://textual.textualize.io/) for the TUI. You should install this through the [bapp-store](https://github.com/conor-f/bapp-store), but if you want to run this on a non-Beepy device, the `justfile` gives a pretty clear indication of what to do (or look at the Developer Quickstart below). In addition to the TUI, you can use `beepy-web-radio` as a regular CLI.


[Demo GIF Here](https://example.com)


## Developer Quickstart

```
$ just init
$ just run
$ just run
$ just run --help
```

The `just init` rule will install a number of pre-commit hooks in addition to installing the actual project.
