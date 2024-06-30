import streamlit as st
from hugchat import hugchat
from hugchat.login import Login


def generate_response(prompt_input, email, password):
    """
    Generate a response from HugChat given a prompt, email, and password.

    Args:
        prompt_input (str): The user's input prompt.
        email (str): The user's email for login.
        password (str): The user's password for login.

    Returns:
        str: The response from HugChat.
    """
    sign = Login(email, password)
    cookies = sign.login()
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    return chatbot.chat(prompt_input)


def main():
    """
    Main function to run the Streamlit chatbot application.
    """
    st.title("Simple Chatbot")

    # Sidebar for user login
    with st.sidebar:
        st.title('Login HugChat')
        hf_email = st.text_input('Enter Email:')  # Input field for email
        # Input field for password
        hf_pass = st.text_input('Enter Password:', type='password')
        if not (hf_email and hf_pass):
            # Warning if email or password is missing
            st.warning('Please enter your account!')
        else:
            # Success message if email and password are provided
            st.success('Proceed to entering your prompt message!')

    # Initialize session state for messages if not already initialized
    if "messages" not in st.session_state.keys():
        st.session_state.messages = [
            {"role": "assistant", "content": "How may I help you?"}]

        # Display initial messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])

    # Check for user input prompt
    if prompt := st.chat_input(disabled=not (hf_email and hf_pass)):

        # Display existing messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])

        # Append user prompt to messages
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        # Generate response from the assistant
        if st.session_state.messages[-1]["role"] != "assistant":
            with st.chat_message("assistant"):
                with st.spinner("Thinking.."):
                    response = generate_response(prompt, hf_email, hf_pass)
                    st.write(response)
            # Append assistant's response to messages
            message = {"role": "assistant", "content": response}
            st.session_state.messages.append(message)


if __name__ == "__main__":
    main()
