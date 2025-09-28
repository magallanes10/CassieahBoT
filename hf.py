import os
import sys
import subprocess

try:
    from huggingface_hub import login, create_repo, upload_folder
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "huggingface_hub"])
    from huggingface_hub import login, create_repo, upload_folder

repo_id = "hutchingd/Cassidy-Bot"
sdk = "docker"
token = os.getenv("HF_TOKEN")

if not token:
    raise ValueError("HF_TOKEN environment variable is missing")

login(token=token)
create_repo(repo_id=repo_id, repo_type="space", space_sdk=sdk, exist_ok=True)
upload_folder(
    folder_path=".",
    repo_id=repo_id,
    repo_type="space",
    exclude=[".git", ".github"]
  )
