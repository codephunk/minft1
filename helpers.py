import os.path as op
from pathlib import Path
import hashlib
from cfg import cfg


async def get_metadata(mint_id):
    metadata = Path(op.join("chia", "wallet", cfg.path.metadata, f"{mint_id}.json"))
    if not metadata.is_file():
        return False

    return open(f"{metadata}", 'rb')


async def get_image_path(mint_id):
    return op.join("chia", "wallet", cfg.path.images, f"{mint_id}.png")


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
