import subprocess
from typing import List, Dict

def check_node_latency(node_list: List[str]) -> Dict[str, float]:
    """
    通过 Ping 检查每个节点的延迟
    """
    latency_results = {}
    for node in node_list:
        try:
            result = subprocess.run(["ping", "-c", "1", node], stdout=subprocess.PIPE)
            latency = float(result.stdout.decode().split('time=')[1].split(' ms')[0])
            latency_results[node] = latency
        except Exception:
            latency_results[node] = float('inf')  # 无法访问的节点延迟设为无穷大
    return latency_results

def get_best_node(node_list: List[str]) -> str:
    """
    返回延迟最低的节点
    """
    latencies = check_node_latency(node_list)
    return min(latencies, key=latencies.get)