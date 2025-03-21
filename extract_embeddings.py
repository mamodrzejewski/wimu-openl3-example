import openl3
from pathlib import Path
from config import HOP_SIZE

if __name__ == "__main__":
    print("> Loading model")

    model = openl3.models.load_audio_embedding_model(
        input_repr="mel256",
        content_type="music",
        embedding_size=512,
    )
    print("> Model loaded")

    embeddings_dir = Path("embeddings")

    if not embeddings_dir.exists():
        embeddings_dir.mkdir(parents=True)
        print(f"> Directory '{embeddings_dir}' created.")
    else:
        print(f"> Directory '{embeddings_dir}' already exists.")

    for file in Path("raw_data/").iterdir():
        openl3.process_audio_file(
            str(file),
            model=model,
            hop_size=HOP_SIZE,
            suffix=f"embedded_{str(HOP_SIZE).replace('.', '')}",
            output_dir="embeddings/",
        )
