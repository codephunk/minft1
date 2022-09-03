import os.path as op
import hashlib
from cfg import cfg

zfill_count = len(str(cfg.collection.size - 1))


def get_full_mint_id(mint_id):
    return str(mint_id).zfill(zfill_count)


def get_metadata_path(mint_id):
    file_name = f"{get_full_mint_id(mint_id)}.json"
    return op.join(cfg.path.metadata, file_name)


def get_image_path(mint_id):
    image_name = f"{get_full_mint_id(mint_id)}.png"
    return op.join(cfg.path.images, image_name)


def sha256sum(filename):
    h = hashlib.sha256()
    with open(filename, 'rb') as file:
        while True:
            # Reading is buffered, so we can read smaller chunks.
            chunk = file.read(h.block_size)
            if not chunk:
                break
            h.update(chunk)

    return h.hexdigest()
