"""Validate the generated import ZIP without installing or launching the game."""
from pathlib import Path
import hashlib
import io
import json
import zipfile
from build import ROOT, DIST, VERSION


def main():
    original_index = json.loads((ROOT / 'docs/UPSTREAM_FILES.json').read_text(encoding='utf-8'))
    manifest = json.loads((ROOT / 'modpack-base/manifest.json').read_text(encoding='utf-8'))
    assert manifest['manifestType'] == 'minecraftModpack' and manifest['manifestVersion'] == 1
    assert manifest['minecraft'] == {'version': '1.16.5', 'modLoaders': [
        {'id': 'forge-36.2.26', 'primary': True}], 'recommendedRam': 4096}
    assert manifest['overrides'] == 'overrides' and len(manifest['files']) == 138
    canonical = json.dumps(manifest['files'], sort_keys=True, separators=(',', ':')).encode()
    assert hashlib.sha256(canonical).hexdigest() == original_index['original_dependency_sha256']
    for item in manifest['files']:
        assert type(item['projectID']) is int and item['projectID'] > 0
        assert type(item['fileID']) is int and item['fileID'] > 0
        assert item['required'] is True

    with zipfile.ZipFile(DIST / f'Cuboid-Outpost-1.1.2-Japanese-Easy-Import-v{VERSION}.zip') as z:
        assert z.testzip() is None
        names = set(z.namelist())
        assert json.loads(z.read('manifest.json')) == manifest
        assert 'instance.cfg' not in names and 'mmc-pack.json' not in names
        for name in names:
            assert '..' not in Path(name).parts and not name.startswith('/')
            assert not name.endswith(('.jar', '.exe', '.dll', '.log', '.db', '.bak', '.local'))
            assert not any(part in {'saves', 'accounts', 'screenshots', 'logs'} for part in Path(name).parts)
        replaced = 'patchouli_books/cuboidoutpost_server_guide/book.json'
        for item in original_index['original_files']:
            path = item['path']
            source = ROOT / 'modpack-base/overrides' / path
            assert hashlib.sha256(source.read_bytes()).hexdigest() == item['sha256']
            if path != replaced:
                assert z.read('overrides/' + path) == source.read_bytes(), path
        for path in original_index['omitted_generated_or_unused']:
            assert 'overrides/' + path not in names
        assert 'overrides/config/skyblockbuilder/template.nbt' in names
        for f in (ROOT / 'server-guide').rglob('*.json'):
            assert z.read('overrides/' + f.relative_to(ROOT / 'server-guide').as_posix()) == f.read_bytes()

        options = dict(line.split(':', 1) for line in z.read('overrides/options.txt').decode().splitlines())
        assert set(options) == {'version', 'lang', 'resourcePacks', 'incompatibleResourcePacks'}
        assert options['version'] == '2586' and options['lang'] == 'ja_jp'
        pack = f'Cuboid-Outpost-1.1.2-Japanese-v{VERSION}.zip'
        assert json.loads(options['resourcePacks']) == ['vanilla', 'file/' + pack]
        assert json.loads(options['incompatibleResourcePacks']) == []
        resource = z.read('overrides/resourcepacks/' + pack)
        assert resource == (DIST / pack).read_bytes()
        with zipfile.ZipFile(io.BytesIO(resource)) as rp:
            assert rp.testzip() is None
            assert json.loads(rp.read('pack.mcmeta'))['pack']['pack_format'] == 6
            assert len(json.loads(rp.read('assets/cuboidquests/lang/ja_jp.json'))) == 4421
            assert len([n for n in rp.namelist() if n.startswith('assets/tconstruct/book/')]) == 386
        # Reject unexpected executable content, settings, or account files in the import.
        expected = {'manifest.json', 'overrides/options.txt', 'overrides/resourcepacks/' + pack}
        expected.update('overrides/' + f.relative_to(ROOT / 'modpack-base/overrides').as_posix()
                        for f in (ROOT / 'modpack-base/overrides').rglob('*') if f.is_file())
        expected.update('overrides/' + f.relative_to(ROOT / 'server-guide').as_posix()
                        for f in (ROOT / 'server-guide').rglob('*') if f.is_file())
        expected.update(f.relative_to(ROOT).as_posix() for folder in ['LICENSES', 'docs']
                        for f in (ROOT / folder).rglob('*') if f.is_file())
        expected.update({'README.md', 'LICENSE.md', 'THIRD_PARTY_NOTICES.md'})
        assert names == expected, names ^ expected
    for line in (DIST / 'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines():
        expected_hash, name = line.split('  ', 1)
        assert hashlib.sha256((DIST / name).read_bytes()).hexdigest() == expected_hash
    print('PASS: 138 original MOD references; 559 original files; Japanese enabled; guide included; no bundled MOD JARs.')


if __name__ == '__main__':
    main()
