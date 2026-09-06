"""L0: validate an explicit source list; no archive, install or runtime."""
import json
from pathlib import Path, PurePosixPath


def source_files(root: Path, manifest: dict) -> list[Path]:
    root = root.resolve(strict=True)
    if set(manifest) != {"files"} or not isinstance(manifest["files"], list):
        raise ValueError("expected only a files list")
    result = []
    seen = set()
    for entry in manifest["files"]:
        if not isinstance(entry, str):
            raise ValueError("path must be text")
        parts = PurePosixPath(entry).parts
        if (not parts or parts[0] != "product" or len(parts) < 2
                or any(p in {".", ".."} for p in entry.split("/"))
                or "\\" in entry or any(c in entry for c in "*?[]")
                or PurePosixPath(entry).as_posix() != entry):
            raise ValueError(f"not an explicit product path: {entry}")
        if entry in seen:
            raise ValueError(f"duplicate: {entry}")
        seen.add(entry)
        path = root
        for part in parts:
            path = path / part
            if path.is_symlink():
                raise ValueError(f"symlink: {entry}")
        if not path.is_file() or not path.resolve().is_relative_to(root / "product"):
            raise ValueError(f"not a product file: {entry}")
        result.append(path)
    return result


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    files = source_files(root, json.loads((root / "tooling/distribution.json").read_text()))
    print(json.dumps({"listed_files": len(files), "boundary": "PASS", "release": False}))
