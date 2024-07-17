import streamlit as st
from attrs import define


@define
class StreamlitIconButton:
    icon_url: str
    link: str
    display_text: str

    @property
    def md(self):
        return f'[![{self.display_text}]({self.icon_url})]({self.link})'


def display_buttons(buttons: [StreamlitIconButton]):
    button_columns = st.columns(len(buttons))
    for button_column, button in zip(button_columns, buttons):
        with button_column:
            st.markdown(button.md)


LinkedInButton = StreamlitIconButton(
    icon_url='https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white',
    link='https://www.linkedin.com/in/christiandaehn/', display_text='LinkedIn')

GithubButton = StreamlitIconButton(
    icon_url='https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white',
    link='https://github.com/dachrisch', display_text='GitHub')

BumblefliesButton = StreamlitIconButton(
    icon_url='https://bumbleflies.de/favicon.ico',
    link='https://bumbleflies.de', display_text='Bumbleflies')
