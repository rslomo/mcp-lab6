from fastmcp import FastMCP

mcp = FastMCP("Hello_world")

@mcp.tool
def say_hello(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run()