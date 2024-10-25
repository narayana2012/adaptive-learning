import streamlit as st

class Header:
    def header():
        st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
        st.markdown("""
        <style>
        .stAppHeader {
            z-index: 99;
        }
                            .navbar {
            box-shadow: -2px 0px 8px 0px rgba(42, 7, 70, 0.02), 2px 6px 8px 0px rgba(42, 7, 70, 0.04); 
                            height: 64px
        }
                     body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f9;
            color: #333;
        }
        .styled-list {
            list-style-type: none;
            padding: 0;
        }
        .styled-list li {
            margin: 10px 0;
        }
        .styled-list a {
            text-decoration: none;
            color: #007BFF;
            font-weight: bold;
            padding: 10px 15px;
            border-radius: 5px;
            transition: background-color 0.3s ease;
        }
        .styled-list a:hover {
            background-color: #007BFF;
            color: white;
        }
        .container {
            margin-top: 50px;
            text-align: center;
        }
        .stVerticalBlock{
                    gap:1px}
                    .stApp{
                    background-color:rgb(246, 243, 236)
                    }
                    .stElementContainer:has(.parent-div) + .stElementContainer {
  background: #fff;
                    padding: 0 15px;
}
                    .stElementContainer:has(.parent-div) + .stElementContainer div{
                    padding: 15px;}

                    .breadcrumb1{
                        color: #000 !important

                    }
        </style>""", unsafe_allow_html=True)
        st.markdown("""
        <nav class="navbar fixed-top navbar-expand-lg navbar-dark">
        <img alt="upgrad-logo" src="https://upgrad.com/_ww3-next/_next/static/media/upgrad-header-logo.325f003e.svg">
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        </nav>
        """, unsafe_allow_html=True)

        st.markdown("""
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
        """, unsafe_allow_html=True)