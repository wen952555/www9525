import subprocess

def create_wireguard_user(username: str) -> str:
    """
    创建一个新的 WireGuard 用户并生成配置文件
    """
    config_file = f"/etc/wireguard/{username}.conf"
    subprocess.run(["wg", "genkey"], stdout=open(f"{username}_private.key", "wb"))
    subprocess.run(["wg", "genkey"], stdout=open(f"{username}_public.key", "wb"))
    # 配置文件生成逻辑
    with open(config_file, "w") as f:
        f.write(f"[Interface]\nPrivateKey = ...\n...")
    return config_file