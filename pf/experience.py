from streamlit_timeline import timeline

with open('md/timeline.json', "r") as f:
    data = f.read()

# render timeline
timeline(data, height=600)
