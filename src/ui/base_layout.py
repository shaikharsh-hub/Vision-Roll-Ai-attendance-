import streamlit as st


def style_background_home():
     
     st.markdown('''
        
        <style>   
            .stApp{
            background: #5A5FEF
            }
            .stApp div[data-testid="stColumn"]{
            background-color:#e6e6e6   !important;
            padding: 2.5rem !important;
            border-radius: 5rem !important;
            }
        
        </style>


''',unsafe_allow_html=True)


def style_background_dashboard():
     
     st.markdown('''
        
        <style>   
            .stApp{
            background: #FFB6C1
}
        </style>


''',unsafe_allow_html=True)

def style_base_layout():
     
     st.markdown("""
        <style>

               @import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap');
               @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');


 


          /* Hide Top Bar of streamlit*/
              
                #MainMenu,footer,header {
                     visibility: hidden;
                }

                .block-container{
                   padding-top:1.5rem !important
                }

                
                h1 {
                    font-family: 'Climate Crisis',sans-serif !important;
                    font-size: 3.5rem !important;
                    line-heigth:1.1 !important;
                    margin-bottom: 0rem !important;
                    }

                h2 {
                    font-family: 'Inter',sans-serif !important;
                    color: #000000 !important;
                    font-size: 2rem !important;
                   line-heigth:1.1 !important;
                    margin-bottom: 0rem !important;
                    }                   
                 
                h3,h4,p {
                    font-family: 'Outfit',sans-serif !important;
                   }


                /* Primary button */
                div[data-testid="stButton"] > button[kind="primary"]{
                    background-color:#FFD400 !important;
                    color:black !important;
                    border:none !important;
                    transition: all 0.3s ease !important;
                }

                div[data-testid="stButton"] > button[kind="primary"]:hover{
                    background-color:#FFC800 !important;
                    color:black !important;
                    transform: translateY(-2px);
                }

                /* Secondary button */
                div[data-testid="stButton"] > button[kind="secondary"]{
                    background-color:#000000 !important;
                    color:white !important;
                    border:none !important;
                    transition: all 0.3s ease !important;
                }

                div[data-testid="stButton"] > button[kind="secondary"]:hover{
                    background-color:#222222 !important;
                    color:white !important;
                    transform: translateY(-2px);
                }                
        </style>


""", unsafe_allow_html=True)

