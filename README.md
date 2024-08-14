# EDGAR Financial Statements RAG

This project leverages Retrieval-Augmented Generation (RAG) to retrieve specific metrics from public company. To create the RAG, I fine tuned Llama 3.1 8B Instruct. To see more about the architecture, see [train.ipynb](train.ipynb).

## Project Structure

- [`train.ipynb`](train.ipynb): Notebook for training the RAG model on the previous quarter's public 10K and 10Q statements.
- [`demo.ipynb`](demo.ipynb): Notebook for demonstrating the generated responses of the trained RAG model.

The vector database can be downloaded with these commands

```bash
mkdir vector_db
cd vector_db
wget https://huggingface.co/liamjdavis/edgar_rag_llama3.1/resolve/main/index.faiss
wget https://huggingface.co/liamjdavis/edgar_rag_llama3.1/resolve/main/index.pkl
```