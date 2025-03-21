HOP_SIZE = 0.2
HS_STR = str(HOP_SIZE).replace(".", "")
EMB_DIR = "embeddings"


def emb_path(name):
    return f"{EMB_DIR}/{name}_embedded_{HS_STR}.npz"


SINE_FILENAME = emb_path("sine_440hz")
CELLO_FILENAME = emb_path("144971__nightlife999__spirit-cello")
TRUMPET_1_FILENAME = emb_path("659454__matrixxx__a-sinful-city-01")
TRUMPET_2_FILENAME = emb_path("659452__matrixxx__a-sinful-city-03")
DRUMS_FILENAME = emb_path("381516__abbasgamez__drums")
ENGINE_FILENAME = emb_path(
    "585215__myeclecticself__car-engine-maserati-granturismo-switch-to-sport-mode-and-launch"
)
