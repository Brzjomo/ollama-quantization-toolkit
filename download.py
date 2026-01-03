# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "modelscope",
#     "huggingface_hub",
# ]
# ///

import os
from modelscope.utils.constant import DownloadMode
from modelscope import snapshot_download as ms_download
from huggingface_hub import snapshot_download as hf_download
from huggingface_hub.utils import RepositoryNotFoundError

# 配置区
MODEL_ID = 'Tencent-Hunyuan/HY-MT1.5-7B'
LOCAL_DIR = './model_files'

def smart_download(model_id, local_dir):
    # 优先尝试 ModelScope
    print(f"🚀 尝试从 ModelScope 下载: {model_id}...")
    try:
        path = ms_download(model_id, local_dir=local_dir)
        print(f"✅ 从 ModelScope 下载成功！路径: {os.path.abspath(path)}")
        return
    except Exception as e:
        print(f"⚠️ ModelScope 下载失败或模型不存在。错误信息: {e}")
        print(f"🔄 正在切换至 Hugging Face...")

    # 备选方案: Hugging Face
    try:
        # 自动配置镜像站以确保国内访问
        os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
        
        print(f"🌐 正在通过 HF 镜像站下载: {model_id}...")
        path = hf_download(
            repo_id=model_id,
            local_dir=local_dir,
            resume_download=True
        )
        print(f"✅ 从 Hugging Face 下载成功！路径: {os.path.abspath(path)}")
    except RepositoryNotFoundError:
        print(f"❌ 错误：在两个平台都找不到模型 ID '{model_id}'。请检查名称是否正确。")
    except Exception as e:
        print(f"❌ 下载过程中发生未知错误: {e}")

if __name__ == "__main__":
    smart_download(MODEL_ID, LOCAL_DIR)