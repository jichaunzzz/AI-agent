import streamlit as st
from agent.runner import run_agent

st.title("🧠 运维Agent")

query = st.text_input("输入问题", "服务A变慢")

if st.button("开始分析"):
    result = run_agent(query)

    st.subheader("结果")
    st.write(result)