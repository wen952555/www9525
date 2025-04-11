import base64

def generate_clash_subscription(nodes: List[dict]) -> str:
    """
    生成 Clash 订阅链接
    """
    clash_format = []
    for node in nodes:
        clash_format.append(f"{node['name']} -> {node['url']}")
    # Base64 加密
    return base64.b64encode("\n".join(clash_format).encode()).decode()

def generate_v2ray_subscription(nodes: List[dict]) -> str:
    """
    生成 V2Ray 订阅链接
    """
    v2ray_format = []
    for node in nodes:
        v2ray_format.append(f"v2ray://{node['url']}")
    return base64.b64encode("\n".join(v2ray_format).encode()).decode()