# works with biotite 0.34.1
import biotite as bt
import biotite.database.rcsb as rcsb
import requests
import os
import gzip
import io
import shutil
###########
query1 = rcsb.FieldQuery("rcsb_polymer_entity_container_identifiers.reference_sequence_identifiers.database_accession", exact_match ='P07333')
query2 = rcsb.FieldQuery("reflns.d_resolution_high", less=2.5)
final_query = query1 & query2
pdb_ids = rcsb.search(final_query)
#################
for id in pdb_ids:
    download_url_prefix = 'http://dunbrack3.fccc.edu/PDBrenum/output_PDB/'
    download_url_suffix = '_renum.pdb.gz'
    pdb_id = id.lower()
    print(pdb_id)
    download_url = download_url_prefix + pdb_id + download_url_suffix
    print(download_url)
    response = requests.get(download_url)
    print(response.status_code)
    fname = pdb_id + '.pdb.gz'
    with open(fname, 'wb') as f:
        f.write(response.content)
    print(f'completed writing {fname}..')
