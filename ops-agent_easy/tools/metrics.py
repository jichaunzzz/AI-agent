# ================================
# 工具层：负责获取真实系统数据
# ================================

import subprocess
import re


def get_cpu_usage():
    """
    获取CPU使用率
    """
    print("🧰 获取CPU")

    try:
        result = subprocess.check_output(
            "top -bn1 | grep 'Cpu(s)'",
            shell=True
        ).decode()

        # 使用正则表达式从命令输出中提取空闲 CPU 百分比
        match = re.search(r'(\d+\.\d+)\s*id', result)
        if match:
            idle = float(match.group(1))  # 获取空闲 CPU 百分比
            cpu = 100 - idle  # 计算 CPU 使用率
            return round(cpu, 2)
        else:
            return 0.0  # 如果没有找到空闲 CPU 数据，返回 0.0

    except subprocess.CalledProcessError as e:
        print("错误：无法执行 top 命令")
        return 0.0  # 如果发生错误，返回 0.0


def get_memory_usage():
    """
    获取内存使用率
    """
    print("🧰 获取内存")

    result = subprocess.check_output(
        "free | grep Mem",
        shell=True
    ).decode().split()

    total = int(result[1])
    used = int(result[2])

    return round(used / total * 100, 2)


def get_network_latency():
    """
    获取网络延迟
    """
    print("🧰 获取网络")

    result = subprocess.check_output(
        "ping -c 1 8.8.8.8",
        shell=True
    ).decode()

    latency = result.split("time=")[1].split()[0]

    return float(latency)