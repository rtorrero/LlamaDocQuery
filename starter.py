import sys

from llama_index import (
    SimpleDirectoryReader,
    ServiceContext,
    VectorStoreIndex
)

# use Huggingface embeddings
from llama_index.embeddings import HuggingFaceEmbedding
from llama_index.llms import LlamaCPP
from llama_index.llms.llama_utils import (
    messages_to_prompt,
    completion_to_prompt,
)

model_url = "https://huggingface.co/TheBloke/Speechless-Llama2-Hermes-Orca-Platypus-WizardLM-13B-GGUF/resolve/main/speechless-llama2-hermes-orca-platypus-wizardlm-13b.Q4_K_M.gguf"
llm = LlamaCPP(
    model_url=model_url,
    model_path=None,
    temperature=0.1,
    max_new_tokens=256,
    # llama2 has a context window of 4096 tokens, but we set it lower to allow for some wiggle room
    context_window=3900,
    # kwargs to pass to __call__()
    generate_kwargs={},
    # kwargs to pass to __init__()
    # set to at least 1 to use GPU
    model_kwargs={"n_gpu_layers": 30},
    # transform inputs into Llama2 format
    messages_to_prompt=messages_to_prompt,
    completion_to_prompt=completion_to_prompt,
    verbose=True,
)

embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

# create a service context
service_context = ServiceContext.from_defaults(
    llm=llm,
    embed_model=embed_model,
)

# load documents
documents = SimpleDirectoryReader("data").load_data()

# create vector store index
index = VectorStoreIndex.from_documents(
    documents, service_context=service_context
)

# set up query engine
query_engine = index.as_query_engine()
question = sys.argv[1]

#question = "As a SAP customer, why would I want to use Trento?"
response = query_engine.query(question)

print("\nQ: ", question)
print("\nA: ", response)