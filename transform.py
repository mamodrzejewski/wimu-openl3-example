import openl3
from pathlib import Path

HOP_SIZE = 0.2

if __name__ == "__main__":
    model = openl3.models.load_audio_embedding_model(
        input_repr="mel256", content_type="music", embedding_size=512,
    )

    for file in Path("raw_data/").iterdir():
        openl3.process_audio_file(
            str(file), model=model, hop_size=HOP_SIZE, suffix="embedded_02", output_dir="embeddings/"
        )
