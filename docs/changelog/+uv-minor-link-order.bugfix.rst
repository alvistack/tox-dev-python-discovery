Rank uv's minor version links behind the concrete install on Windows too, where uv creates them as directory junctions
that ``Path.is_symlink()`` does not report.
