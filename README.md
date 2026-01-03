## 使用流程

#### 克隆

```bash
git clone --recursive https://github.com/Brzjomo/ollama-quantization-toolkit.git
```



#### 安装UV

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```



#### 下载模型

先修改模型名称

```powershell
uv run download.py
```



#### 转换模型

先转换为fp16。

```powershell
uv run convert.py
```



#### 修改ModelFile

根据模型修改

```bash
FROM ./MT1.5_7B_f16.gguf

TEMPLATE """{{ if .System }}<|startoftext|>{{ .System }}<|extra_4|>{{ end }}{{ if .Prompt }}<|startoftext|>{{ .Prompt }}<|extra_0|>{{ end }}"""

PARAMETER top_k 20
PARAMETER top_p 0.6
PARAMETER repeat_penalty 1.05
PARAMETER temperature 0.7
PARAMETER num_ctx 4096
```



#### 创建ollama模型

量化为q4km。

```bash
ollama create Tencent-Hunyuan/MT1.5_7B_q4km -f Modelfile -q Q4_K_M
```



#### 手动清理中间文件