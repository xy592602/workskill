"""Build an offline variant plan. Does not submit generation requests."""
import argparse
import itertools
import json
from pathlib import Path


def build(plan):
    axes = []
    for key in ('sources', 'palettes', 'layouts', 'copies'):
        values = plan.get(key)
        if not isinstance(values, list) or not values:
            raise ValueError(f'{key} must be a nonempty list')
        ids = []
        for value in values:
            if key in ('sources', 'copies'):
                if not isinstance(value, dict):
                    raise ValueError(f'{key} entries must be objects')
                identity = value.get('id')
                fields = ('reference',) if key == 'sources' else ('title', 'body')
                for field in fields:
                    if not isinstance(value.get(field), str):
                        raise ValueError(f'{key}.{field} must be text')
                if key == 'sources' and not value['reference'].strip():
                    raise ValueError('empty source reference')
            else:
                identity = value
            if not isinstance(identity, str) or not identity.strip():
                raise ValueError(f'{key} needs nonempty string IDs')
            if identity in ids:
                raise ValueError(f'duplicate {key} ID: {identity}')
            ids.append(identity)
        axes.append(values)
    count = 1
    for axis in axes:
        count *= len(axis)
    limit = plan.get('max_outputs')
    if type(limit) is not int or limit < 1 or count > limit:
        raise ValueError(f'{count} outputs exceed or lack a valid max_outputs')
    entries = []
    for n, (source, palette, layout, copy) in enumerate(itertools.product(*axes), 1):
        entries.append(dict(id=f'variant-{n:04d}', source_id=source['id'],
                            reference=source['reference'], palette=palette, layout=layout,
                            copy_id=copy['id'], title=copy['title'], body=copy['body'],
                            output=f'{n:04d}.png', status='planned',
                            visual_check='not_checked', business_review='not_reviewed'))
    return dict(version=1, expected_count=count, entries=entries)


def save(plan_path, output_path):
    result = build(json.loads(Path(plan_path).read_text(encoding='utf-8')))
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open('x', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        f.write('\n')
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('plan')
    parser.add_argument('output')
    args = parser.parse_args()
    try:
        result = save(args.plan, args.output)
    except (ValueError, OSError) as exc:
        parser.exit(1, f'Error: {exc}\n')
    print(f"Planned {result['expected_count']} outputs; no generation requests sent.")
