Stop a ``.python-version`` file that is not valid UTF-8, or that cannot be read, from aborting discovery through a
pyenv, mise or asdf shim; a stray byte no longer hides the versions it names, and an unreadable file is skipped like a
missing one.
