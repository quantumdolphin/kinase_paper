import streamlit as st
import pandas as pd

def search_data(data, query):
    filtered_data = data[data['Column'].str.contains(query, case=False)]
    return filtered_data

def main():
    # Set title and sidebar
    st.title("CSV Data Search")
    st.sidebar.title("Search Options")
    
    # Upload CSV file
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    
    if uploaded_file is not None:
        # Read the CSV file
        data = pd.read_csv(uploaded_file)
        
        # Display the CSV file
        st.subheader("CSV Data")
        st.write(data)
        
        # Search input
        search_query = st.sidebar.text_input("Search query", "")
        
        # Perform search and display results
        if st.sidebar.button("Search"):
            filtered_data = search_data(data, search_query)
            if filtered_data.empty:
                st.warning("No results found.")
            else:
                st.subheader("Search Results")
                st.write(filtered_data)
    else:
        st.warning("Upload a CSV file to get started.")

if __name__ == "__main__":
    main()
