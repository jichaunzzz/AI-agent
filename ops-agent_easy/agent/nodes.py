# ================================
# Node层：每一步操作
# ================================

from tools.metrics import get_cpu_usage, get_memory_usage, get_network_latency
from llm.qwen_client import ask_llm


def analyze_node(state):
    """
    初始分析
    """
    print("🧠 分析:", state["query"])
    return state


def metrics_node(state):
    """
    查CPU
    """
    cpu = get_cpu_usage()

    return {
        **state,
        "metrics": {
            **(state.get("metrics") or {}),
            "cpu": cpu
        }
    }


def memory_node(state):
    """
    查内存
    """
    memory = get_memory_usage()

    return {
        **state,
        "metrics": {
            **(state.get("metrics") or {}),
            "memory": memory
        }
    }


def network_node(state):
    """
    查网络
    """
    network = get_network_latency()

    return {
        **state,
        "metrics": {
            **(state.get("metrics") or {}),
            "network": network
        }
    }


def logs_node(state):
    """
    查日志
    """
    import subprocess

    try:
        logs = subprocess.check_output(
            "tail -n 5 /var/log/syslog",
            shell=True
        ).decode()
    except:
        logs = "日志读取失败"

    return {
        **state,
        "logs": logs
    }


def reasoning_node(state):
    """
    LLM决策核心
    """
    metrics = state.get("metrics")
    logs = state.get("logs")
    history = state.get("history")

    prompt = f"""
当前信息：
metrics: {metrics}
logs: {logs}
history: {history}

规则：
- 不要重复操作
- 信息不足继续查
- 信息足够 finish

返回：
check_metrics / check_memory / check_network / check_logs / finish
"""

    decision = ask_llm(prompt)

    if not decision:
        decision = "check_metrics"

    decision = decision.strip()

    print("🧠 决策:", decision)

    return {
        **state,
        "analysis": {
            "decision": decision
        }
    }