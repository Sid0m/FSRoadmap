import streamlit as st
import streamlit.components.v1 as comp
import pandas as pd
import os

st.set_page_config(
  page_title="FutureSkills",
  page_icon="🛣️",
)

st.title("OTH FutureSkills Project")
st.text_area(
  "Was sind Future Skills",
  "Unsere Welt ist in stetigem Wandel. Kaum ein Berufszweig kommt ohne Zukunftskompetenzen aus."
  "Future Skills sind wichtig für das alltägliche und professionelle Leben. An der 0TH haben wir 18 Future Skills zusammengefasst." 
  "Hier ist eine Geschichte, um ein gesamtes Bild von allen Kompetenzen zu zeigen.",
  height = 125
)

col1, col2, col3 = st.columns([0.2,0.2,0.6])

with col1:
  with st.container(border=True):
    st.image("icons/1.png")

with col2:
  st.html("<hr>")
  
with col3: 
  with st.container(border=True):
    st.header("Agile Arbeitsweise")
    st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")  

roadmap_html="""
    <div class="container">
      <div class="timeline">
        <div class="row no-gutters justify-content-end justify-content-md-around align-items-start  timeline-nodes">
          <div class="col-10 col-md-5 order-3 order-md-1 timeline-content">
            <h3 class=" text-light">Timeline Heading</h3>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Saepe, eaque amet deleniti hic quas qui cumque delectus aliquid, eius quia quod, quae, aliquam aspernatur facilis. Minima quod corporis dignissimos porro.</p>
          </div>
          <div class="col-2 col-sm-1 px-md-3 order-2 timeline-image text-md-center">
            <img src="icons/1.png" class="img-fluid" alt="img">
          </div>
          <div class="col-10 col-md-5 order-1 order-md-3 py-3 timeline-date">
            <time>2018-02-23</time>
          </div>
        </div>
        <div class="row no-gutters justify-content-end justify-content-md-around align-items-start  timeline-nodes">
          <div class="col-10 col-md-5 order-3 order-md-1 timeline-content">
            <h3 class=" text-light">Timeline Heading</h3>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Saepe, eaque amet deleniti hic quas qui cumque delectus aliquid, eius quia quod, quae, aliquam aspernatur facilis. Minima quod corporis dignissimos porro.</p>
          </div>
          <div class="col-2 col-sm-1 px-md-3 order-2 timeline-image text-md-center">
            <img src="icons/2.png" class="img-fluid" alt="img">
          </div>
          <div class="col-10 col-md-5 order-1 order-md-3 py-3 timeline-date">
            <time>2018-02-23</time>
          </div>
        </div>
        <div class="row no-gutters justify-content-end justify-content-md-around align-items-start  timeline-nodes">
          <div class="col-10 col-md-5 order-3 order-md-1 timeline-content">
            <h3 class=" text-light">Timeline Heading</h3>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Saepe, eaque amet deleniti hic quas qui cumque delectus aliquid, eius quia quod, quae, aliquam aspernatur facilis. Minima quod corporis dignissimos porro.</p>
          </div>
          <div class="col-2 col-sm-1 px-md-3 order-2 timeline-image text-md-center">
            <img src="icons/3.png" class="img-fluid" alt="img">
          </div>
          <div class="col-10 col-md-5 order-1 order-md-3 py-3 timeline-date">
            <time>2018-02-23</time>
          </div>
        </div>
        <div class="row no-gutters justify-content-end justify-content-md-around align-items-start  timeline-nodes">
          <div class="col-10 col-md-5 order-3 order-md-1 timeline-content">
            <h3 class=" text-light">Timeline Heading</h3>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Saepe, eaque amet deleniti hic quas qui cumque delectus aliquid, eius quia quod, quae, aliquam aspernatur facilis. Minima quod corporis dignissimos porro.</p>
          </div>
          <div class="col-2 col-sm-1 px-md-3 order-2 timeline-image text-md-center">
            <img src="icons/4.png" class="img-fluid" alt="img">
          </div>
          <div class="col-10 col-md-5 order-1 order-md-3 py-3 timeline-date">
            <time>2018-02-23</time>
          </div>
        </div>
      </div>
    </div>
"""
image = 1

def main():
  
  load_css("css/styles.css")
  st.markdown("""
              <link href="//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
              <script src="//maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
              <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  """, unsafe_allow_html=True)
  st.markdown(roadmap_html, unsafe_allow_html=True)
  st.image(f"icons/{image}.png", use_column_width=True)