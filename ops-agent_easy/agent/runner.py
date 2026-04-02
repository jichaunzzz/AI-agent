# ================================
# Runner：控制整个流程（核心）
# ================================

from agent.nodes import (
    analyze_node,
    metrics_node,
    memory_node,
    network_node,
    logs_node,
    reasoning_node
)


def run_agent(query):
    state = {
        "query": query,
        "metrics": None,
        "logs": None,
        "analysis": {},
        "history": []
    }

    print("🚀 Agent启动")

    state = analyze_node(state)

    node_map = {
        "check_metrics": metrics_node,
        "check_memory": memory_node,
        "check_network": network_node,
        "check_logs": logs_node
    }

    for step in range(5):
        print(f"\n🔄 第{step+1}轮")

        state = reasoning_node(state)
        decision = state["analysis"]["decision"]

        # finish验证
        if decision == "finish":
            if not state.get("logs"):
                print("⚠️ 信息不足，继续")
                continue
            print("✅ 分析完成")
            break

        next_node = node_map.get(decision)

        if not next_node:
            print("⚠️ 未知决策")
            continue

        print("➡️ 执行:", decision)

        state = next_node(state)
        state["history"].append(decision)

        print("📦 state:", state)

    return state