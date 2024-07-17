import streamlit as st

from md.markdown_reader import MarkdownReader, md
from util.st_icon_button import LinkedInButton, GithubButton, BumblefliesButton, display_buttons


col1,col2,_ = st.columns(3)
with col1:
    st.image('static/me_rounded.webp', width=300)
    display_buttons([LinkedInButton, GithubButton, BumblefliesButton])
with col2:
    st.markdown(md.read('about_me'))
