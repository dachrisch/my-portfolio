import streamlit as st
from st_pages import show_pages, Page, Section


def app():
    st.set_page_config(page_title="Chris' Portfolio", )

    show_pages(
        [Page('me.py', 'Christian Dähn', '💁'),
         Page('pf/experience.py', 'Experience', '🏫')]
    )


if __name__ == '__main__':
    app()
