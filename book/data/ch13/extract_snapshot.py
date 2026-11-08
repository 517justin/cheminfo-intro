"""Author utility: project a pinned ORD archive; reader notebooks need no ORD install.
Usage: python extract_snapshot.py source.pb.gz output.json.gz
Temporary author environment: ord-schema 0.9.6, protobuf 5.29.6.
"""
import gzip, hashlib, json, sys
from pathlib import Path
from google.protobuf.json_format import MessageToDict
from ord_schema.proto import dataset_pb2
SOURCE_SHA = '0cbcf613395e9bab0bd274f0ae81a73f4b230fbba557e4cf477d024407dcf8af'
COMMIT = '2a6dff66c02f5d1c9b1589691f845b941c981a7a'
DATASET = 'ord_dataset-68cb8b4b2b384e3d85b5b1efae58b203'
source = Path(sys.argv[1]).read_bytes()
assert hashlib.sha256(source).hexdigest() == SOURCE_SHA
message = dataset_pb2.Dataset(); message.ParseFromString(gzip.decompress(source))
raw = MessageToDict(message, preserving_proto_field_name=True)
assert raw['dataset_id'] == DATASET and len(raw['reactions']) == 5760
records = []
for r in raw['reactions']:
    # Retain recorded chemical/measurement fields; exclude submitter contact data.
    item = {k: r[k] for k in ('reaction_id', 'inputs', 'conditions', 'outcomes')}
    item['doi'] = r['provenance']['doi']
    item['has_notes'] = bool(r.get('notes'))
    item['has_observations'] = bool(r.get('observations'))
    records.append(item)
payload = {'dataset_id': DATASET, 'source_commit': COMMIT, 'source_sha256': SOURCE_SHA,
           'source_url': f'https://github.com/open-reaction-database/ord-data/blob/{COMMIT}/data/68/{DATASET}.pb.gz',
           'license': 'CC-BY-SA-4.0', 'original_doi': '10.1126/science.aap9112',
           'ord_doi': '10.1021/jacs.1c09820', 'projection_version': 1,
           'modifications': 'Retained all 5760 reactions; projected inputs, conditions, outcomes, DOI and presence flags. No imputation or recalculation of yields; contact fields excluded.',
           'records': records}
encoded = gzip.compress(json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode(), mtime=0)
Path(sys.argv[2]).write_bytes(encoded)
print(len(records), len(encoded), hashlib.sha256(encoded).hexdigest())
