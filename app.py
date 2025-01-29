import streamlit as st
from agent import CallAIAgent

# Streamlit app
st.set_page_config(page_title="LegalEase AI", page_icon="📜", layout="wide")

# Sidebar with logo
st.sidebar.image("C:/Users/Acer/Desktop/callai/a/logo/icon.png", width=300)

# API Key Input below icon (Always Visible)
st.sidebar.subheader("🔑 Enter OpenAI API Key")
api_key = st.sidebar.text_input("API Key", type="password")

# Initialize the agent only if the API key is provided
agent = CallAIAgent(api_key) if api_key else None

# Sidebar Navigation
st.sidebar.title("Navigate")
option = st.sidebar.selectbox(
    "Choose an option",
    ["Contract Analyzer", "Contract Generator", "Contract Improvement", "Legal Query", "Full Analysis"]
)

# Custom styles
st.markdown("""
    <style>
        .title {
            font-size: 36px;
            font-weight: bold;
            color: #4CAF50;
            text-align: center;
        }
        .header {
            font-size: 28px;
            color: #4CAF50;
            margin-top: 20px;
            margin-bottom: 20px;
        }
        .sidebar .sidebar-content {
            background-color: #f0f0f0;
            padding: 20px;
        }
        .button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            border-radius: 8px;
        }
        .button:hover {
            background-color: #45a049;
        }
        .spinner {
            color: #4CAF50;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="title">LegalEase AI - Comprehensive Contract Assistant</h1>', unsafe_allow_html=True)
st.markdown("""
    <div style="font-size: 18px; color: #555; text-align: center; max-width: 800px; margin: 0 auto;">
        LegalEase AI helps you effortlessly analyze, generate, and improve legal contracts. 
        Whether you're drafting a new agreement, reviewing an existing contract, or seeking legal advice, 
        this AI-powered tool simplifies the process to ensure clarity and compliance.
    </div>
""", unsafe_allow_html=True)

# 🚀 Always show input fields but disable buttons if no API key is provided
api_key_missing = not api_key

# Display selected option
if option == "Contract Analyzer":
    st.header("Contract Analyzer")
    contract_text = st.text_area("Paste your contract here:", height=300)
    analyze_button = st.button("Analyze Contract", key="analyze", help="Click to analyze the contract.", use_container_width=True)

    if analyze_button:
        if api_key_missing:
            st.warning("⚠️ Please enter your OpenAI API key to enable this feature.")
        elif contract_text.strip():
            with st.spinner("Analyzing contract..."):
                analysis_result = agent.analyze_contract(contract_text)
                st.success("Analysis Complete!")
                st.write(analysis_result)
        else:
            st.error("Please enter a contract to analyze.")

elif option == "Contract Generator":
    st.header("Contract Generator")
    requirements = st.text_area("Describe your contract requirements:", height=300)
    generate_button = st.button("Generate Contract", key="generate", help="Click to generate the contract.", use_container_width=True)

    if generate_button:
        if api_key_missing:
            st.warning("⚠️ Please enter your OpenAI API key to enable this feature.")
        elif requirements.strip():
            with st.spinner("Generating contract..."):
                generated_contract = agent.generate_contract(requirements)
                st.success("Contract Generated!")
                st.write(generated_contract)
        else:
            st.error("Please enter your contract requirements.")

elif option == "Contract Improvement":
    st.header("Contract Improvement")
    contract_text = st.text_area("Paste your contract here:", height=300)
    improve_button = st.button("Suggest Improvements", key="improve", help="Click to suggest improvements.", use_container_width=True)

    if improve_button:
        if api_key_missing:
            st.warning("⚠️ Please enter your OpenAI API key to enable this feature.")
        elif contract_text.strip():
            with st.spinner("Generating suggestions..."):
                suggestions = agent.suggest_improvements(contract_text)
                st.success("Suggestions Generated!")
                st.write(suggestions)
        else:
            st.error("Please enter a contract to improve.")

elif option == "Legal Query":
    st.header("Legal Query")
    question = st.text_area("Ask your legal question:", height=150)
    answer_button = st.button("Get Answer", key="answer", help="Click to get a legal answer.", use_container_width=True)

    if answer_button:
        if api_key_missing:
            st.warning("⚠️ Please enter your OpenAI API key to enable this feature.")
        elif question.strip():
            with st.spinner("Generating answer..."):
                answer = agent.answer_legal_query(question)
                st.success("Answer Generated!")
                st.write(answer)
        else:
            st.error("Please enter a legal question.")

elif option == "Full Analysis":
    st.header("Full Analysis")
    input_text = st.text_area("Paste your contract or describe your requirements here:", height=300)
    full_analysis_button = st.button("Run Full Analysis", key="full_analysis", help="Click to run full analysis.", use_container_width=True)

    if full_analysis_button:
        if api_key_missing:
            st.warning("⚠️ Please enter your OpenAI API key to enable this feature.")
        elif input_text.strip():
            with st.spinner("Running full analysis..."):
                analysis_result = agent.analyze_contract(input_text)
                generated_contract = agent.generate_contract(input_text)
                suggestions = agent.suggest_improvements(input_text)
                legal_answer = agent.answer_legal_query("What are the key legal considerations for this contract?")

                # Display results in tabs
                tab1, tab2, tab3, tab4 = st.tabs(["📄 Contract Analyzer", "📝 Generated Contract", "💡 Improvement Suggestions", "⚖️ Legal Advice"])
                with tab1: st.write(analysis_result)
                with tab2: st.write(generated_contract)
                with tab3: st.write(suggestions)
                with tab4: st.write(legal_answer)

                st.success("Full Analysis Complete!")
        else:
            st.error("Please enter a contract or requirements to analyze.")
