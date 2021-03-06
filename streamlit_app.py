import streamlit as st
from supabase import create_client, Client

# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    url = st.secrets["supabase_url"]
    key = st.secrets["supabase_key"]
    return create_client(url, key)

supabase = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query():
    return supabase.table("dane_2022-06-03").select("*").execute()

rows = run_query()
st.write('Hejo')
st.dataframe(rows)
# Print results.
#for row in rows.data:
#    st.write(f"{row['Data']} xd :{row['Godzina']}:")
