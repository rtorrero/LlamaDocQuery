# LlamaDocQuery

Welcome to LlamaDocQuery, a tool that leverages the power of `llama-index` to enable querying pre-existing documents using `llama`. This project allows users to ask questions about any text data without requiring fine-tuning. Perfect for quickly extracting information from large document sets.

## Features

- **Easy Integration:** Seamlessly integrates with existing `llama` models.
- **No Fine-Tuning Required:** Use `llama` on pre-existing documents without additional training.
- **Versatile Document Handling:** Supports a variety of document formats placed in the `data/` directory.

## Getting Started

### Prerequisites

- Python 3.8 or later
- Pip package manager

### Installation

1. Clone this repository to your local machine:
   `git clone [repository-url]`

2. Navigate to the cloned repository directory:
   `cd LlamaDocQuery`

3. Install the required dependencies:
   `pip install -r requirements.txt`

### Adding Documents

To query documents:

1. Place your documents in the `data/` directory.
2. Ensure the documents are in a supported format.

### Running an Example

We've included documentation from the Trento project in the `data/` directory. To test the system with this example:

1. Run the following command passing your question as an argument:

`python starter.py "What is Trento?"`

```
─$ python starter.py "what is Trento?"
llama_model_loader: loaded meta data with 19 key-value pairs and 363 tensors from /tmp/llama_index/models/speechless-llama2-hermes-orca-platypus-wizardlm-13b.Q4_K_M.gguf (version GGUF V2)
llama_model_loader: - tensor    0:                token_embd.weight q4_K     [  5120, 32000,     1,     1 ]
llama_model_loader: - tensor    1:           blk.0.attn_norm.weight f32      [  5120,     1,     1,     1 ]
...
... (Suppressed output)
....................................................................................................
llama_new_context_with_model: n_ctx      = 3900
llama_new_context_with_model: freq_base  = 10000.0
llama_new_context_with_model: freq_scale = 1
llama_new_context_with_model: kv self size  = 3046.88 MB
llama_build_graph: non-view tensors processed: 924/924
llama_new_context_with_model: compute buffer total size = 348.93 MB
AVX = 1 | AVX2 = 1 | AVX512 = 0 | AVX512_VBMI = 0 | AVX512_VNNI = 0 | FMA = 1 | NEON = 0 | ARM_FMA = 0 | F16C = 1 | FP16_VA = 0 | WASM_SIMD = 0 | BLAS = 0 | SSE3 = 1 | SSSE3 = 1 | VSX = 0 |

llama_print_timings:        load time =   11871.59 ms
llama_print_timings:      sample time =      15.34 ms /   124 runs   (    0.12 ms per token,  8082.39 tokens per second)
llama_print_timings: prompt eval time =   11871.41 ms /   327 tokens (   36.30 ms per token,    27.55 tokens per second)
llama_print_timings:        eval time =   21856.65 ms /   123 runs   (  177.70 ms per token,     5.63 tokens per second)
llama_print_timings:       total time =   33902.48 ms

Q:  what is Trento?

A:    Trento is a comprehensive cloud-native, distributed monitoring solution that consists of three main components: Agent, Wanda, and Web. The Agent is a single background process that runs on each host in the target infrastructure, while Wanda orchestrates check executions among the installed Trento Agents. The Web component serves as the control plane of the Trento Platform, working together with the Agents and Wanda to discover, observe, monitor, and check the target SAP infrastructure. Trento provides basic integration with Grafana and Prometheus for effective monitoring in critical business systems.
```
