"""Build the public Japanese resource pack and optional server guide (Python 3.10+)."""
from pathlib import Path
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parent
VERSION = '1.0.0'
DIST = ROOT / 'dist'


def build_zip(name, files):
    target = DIST / name
    with zipfile.ZipFile(target, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for archive_name, path in sorted(files.items()):
            data = path.read_bytes()
            if path.suffix in {'.json', '.mcmeta'}:
                json.loads(data.decode('utf-8'))
            info = zipfile.ZipInfo(archive_name, date_time=(2026, 11, 12, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    with zipfile.ZipFile(target) as archive:
        assert archive.testzip() is None
    return target


def tree(folder):
    base = ROOT / folder
    return {p.relative_to(base).as_posix(): p for p in base.rglob('*') if p.is_file()}


def main():
    DIST.mkdir(exist_ok=True)
    notices = {f'LICENSES/{p.relative_to(ROOT / "LICENSES").as_posix()}': p
               for p in (ROOT / 'LICENSES').rglob('*') if p.is_file()}
    notices.update({name: ROOT / name for name in ['README.md', 'LICENSE.md', 'THIRD_PARTY_NOTICES.md']})
    notices.update({f'docs/{p.relative_to(ROOT / "docs").as_posix()}': p
                    for p in (ROOT / 'docs').rglob('*') if p.is_file()})
    packs = [build_zip(f'Cuboid-Outpost-1.1.2-Japanese-v{VERSION}.zip', {**tree('resourcepack'), **notices}),
             build_zip(f'Cuboid-Outpost-1.1.2-ServerGuide-Japanese-v{VERSION}.zip', {**tree('server-guide'), **notices})]
    checksums = ''.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n' for p in packs)
    (DIST / 'SHA256SUMS.txt').write_text(checksums, encoding='utf-8', newline='\n')
    print(checksums, end='')


if __name__ == '__main__':
    main()
