import streamlit as st

from util.st_icon_button import LinkedInButton, GithubButton, BumblefliesButton, display_buttons

col1, col2 = st.columns(2)
with col1:
    st.image('assets/me_rounded.webp', width=300)
    display_buttons([LinkedInButton, GithubButton, BumblefliesButton])
with col2:
    st.title('About me')
    st.write('''Ich bin Christian Dähn, Diplom-Ingenieur der Informatik und leidenschaftlicher Organisationsentwickler und Team Lead. Mit über 15 Jahren Erfahrung in der IT-Branche unterstütze ich Unternehmen bei der digitalen Transformation und der Implementierung agiler Methoden.

Als Mitgründer der bumbleflies UG und Geschäftsführer helfe ich Organisationen, das Open Space Format erfolgreich zu nutzen und innovative Lösungen zu entwickeln. Meine Expertise umfasst die Leitung und Motivation von Teams, strategische Planung und die Umsetzung von Veränderungsprozessen.

Ich freue mich darauf, mit Ihnen zusammenzuarbeiten und Ihre Organisation auf dem Weg zu nachhaltigem Erfolg zu begleiten.''')
