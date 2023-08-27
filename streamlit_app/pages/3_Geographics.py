import streamlit as st
from streamlit_extras.switch_page_button import switch_page

from utils.general_utils import refer_to_load_data_section, set_background


def main():
    set_background()

    if 'data' not in st.session_state:
        refer_to_load_data_section()

    else:

        # Sidebar navigation
        section = st.sidebar.radio("Navigate", ("Main App", "Section A", "Section B", "Section C"))

        if section == "Main App":

                st.header("Data Preview")
                st.write(st.session_state['data'].head())

        elif section in ("Section A", "Section B", "Section C"):
            st.header(section)
            # You can create a similar template for each section as the main app


# Run the app
if __name__ == "__main__":
    main()
