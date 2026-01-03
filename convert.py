# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "torch",
#     "transformers",
#     "sentencepiece",
#     "gguf",
#     "accelerate",
# ]
# ///

import subprocess
import os
import sys

# 配置区
model_path = "./model_files"
output_gguf = "./output/my_model_f16.gguf"
llama_cpp_path = "./llama.cpp"

def run_convert():
    cmd = [
        sys.executable, 
        os.path.join(llama_cpp_path, "convert_hf_to_gguf.py"),
        model_path,
        "--outfile", output_gguf,
        "--outtype", "f16"
    ]
    print(f"正在启动转换进程...")
    result = subprocess.run(cmd)
    
    if result.returncode == 0:
        print(f"转换成功！输出文件: {output_gguf}")
    else:
        print(f"转换失败，错误码: {result.returncode}")

if __name__ == "__main__":
    run_convert()