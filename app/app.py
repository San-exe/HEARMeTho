import streamlit as st

st.set_page_config(page_title="HEARMeTho", page_icon="🎧", layout="wide")

st.title("HEARMeTho")
st.caption("Let the data hear you out.")

st.info(
    "Project scaffold is ready. Add the Spotify dataset to data/raw/ and wire the ETL + mining modules before the dashboard is used for real analysis."
)

st.subheader("Planned modules")
st.write(
    "ETL → Warehouse → Preprocessing/EDA → Decision Tree → Naive Bayes → Regression → K-Means → Hierarchical Clustering → Apriori → Vibe Engine"
)
