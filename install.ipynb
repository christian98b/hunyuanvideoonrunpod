import subprocess
import os

# Clone the repository
subprocess.run(["git", "clone", "https://github.com/tencent/HunyuanVideo"])

subprocess.run(["python", "-m", "pip", "install", "hf_transfer"])

subprocess.run(["python", "-m", "pip", "install", "huggingface_hub[hf_transfer]"])

# Change directory to HunyuanVideo
os.chdir("HunyuanVideo")

# Install pip dependencies
subprocess.run(["python", "-m", "pip", "install", "-r", "requirements.txt"])

# Install flash attention v2 for acceleration (requires CUDA 11.8 or above)
subprocess.run(["python", "-m", "pip", "install", "ninja"])
subprocess.run(["python", "-m", "pip", "install", "git+https://github.com/Dao-AILab/flash-attention.git@v2.6.3"])

# Install huggingface-cli
subprocess.run(["python", "-m", "pip", "install", "huggingface_hub[cli]"])

# Download the HunyuanVideo model
subprocess.run(["huggingface-cli", "download", "tencent/HunyuanVideo", "--local-dir", "./ckpts"])

# Download Text Encoder
# Download MLLM model (text_encoder folder)
os.chdir("ckpts")
subprocess.run(["huggingface-cli", "download", "xtuner/llava-llama-3-8b-v1_1-transformers", "--local-dir", "./llava-llama-3-8b-v1_1-transformers"])

# Separate the language model parts of llava-llama-3-8b-v1_1-transformers into text_encoder
os.chdir("../")
subprocess.run(["python", "hyvideo/utils/preprocess_text_encoder_tokenizer_utils.py", "--input_dir", "ckpts/llava-llama-3-8b-v1_1-transformers", "--output_dir", "ckpts/text_encoder"])

# Download CLIP model (text_encoder_2 folder)
os.chdir("ckpts")
subprocess.run(["huggingface-cli", "download", "openai/clip-vit-large-patch14", "--local-dir", "./text_encoder_2"])
