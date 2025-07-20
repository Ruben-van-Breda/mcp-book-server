# main.py
from fastapi import FastAPI
from server import mcp  # your FastMCP instance

app = FastAPI()
# mount the streamable‑HTTP MCP endpoint at /mcp
app.mount("/mcp", mcp.streamable_http_app(), name="books-mcp")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
