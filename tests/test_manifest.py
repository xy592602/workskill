import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('manifest', ROOT / 'skills/image-variants/scripts/build_manifest.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ManifestTest(unittest.TestCase):
    def setUp(self):
        self.plan = json.loads((ROOT / 'skills/image-variants/references/plan.example.json').read_text())

    def test_complete_unique_combinations_and_verbatim_copy(self):
        self.plan['copies'][0]['body'] = 'β + 10%\n原文，不能改。'
        result = module.build(self.plan)
        self.assertEqual(result['expected_count'], 8)
        self.assertEqual(len({e['output'] for e in result['entries']}), 8)
        self.assertEqual(len({(e['source_id'], e['palette'], e['layout'], e['copy_id']) for e in result['entries']}), 8)
        for entry in result['entries']:
            self.assertEqual(entry['status'], 'planned')
            if entry['copy_id'] == 'copy-01':
                self.assertEqual(entry['body'], 'β + 10%\n原文，不能改。')

    def test_reject_unsafe_plans(self):
        for key, value in [('sources', []), ('palettes', ['x', 'x']), ('max_outputs', 7), ('max_outputs', True), ('copies', [{'id':'x','title':'缺正文'}])]:
            with self.subTest(key=key, value=value):
                plan = copy.deepcopy(self.plan)
                plan[key] = value
                with self.assertRaises(ValueError):
                    module.build(plan)

    def test_no_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / 'plan.json'
            output = Path(directory) / 'manifest.json'
            source.write_text(json.dumps(self.plan))
            module.save(source, output)
            previous = output.read_bytes()
            with self.assertRaises(FileExistsError):
                module.save(source, output)
            self.assertEqual(output.read_bytes(), previous)


if __name__ == '__main__':
    unittest.main()
