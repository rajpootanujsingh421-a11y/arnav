from funasr import AutoModel

print("Loading SenseVoice Model...")

model = AutoModel(
    model="iic/SenseVoiceSmall",
    trust_remote_code=True
)

print("✅ SenseVoice Ready!")