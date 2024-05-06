import streamlit as st
import pandas as pd
import openpyxl


def displayInsights(selectedInsight):

    st.subheader(f"{selectedInsight}")


    if selectedInsight =="Home":
        st.markdown("<h3 style='text-align:left; color:white; '>Created By: Catalin Soare (W1924815)</h3> ", unsafe_allow_html=True)

        st.image("titlepic.png",use_column_width=True)

        

    elif selectedInsight == "Agricultural Land":
    
        st.markdown("<h3 style='text-align:center; color:white; '>Univariate analysis and a boxplot of the dataset.", unsafe_allow_html=True)

        st.image("ag.png",use_column_width=True)

        #zoom
        st.write("Zoom Slider:")
        zoom_level = st.slider("Zoom-Level", min_value=50, max_value=200, value=100, step=20)
        st.write("Use the slider to zoom in or out on the image. ")

        st.write("<style>img {transform: scale("+str(zoom_level/100)+");}</style>",unsafe_allow_html= True)
        

    elif selectedInsight == "Deforestation":
        
        st.markdown("<h3 style='text-align:center; color:white; '>DEFORESTATION CO2 BY PRODUCT", unsafe_allow_html=True)

        st.markdown("<h3 style='text-align:center; color:white; '>Univariate analysis and a boxplot of the dataset.", unsafe_allow_html=True)

        st.image("def.png",use_column_width=True)

        #zoom
        st.write("Zoom Slider:")
        zoom_level = st.slider("Zoom-Level", min_value=50, max_value=200, value=100, step=20)
        st.write("Use the slider to zoom in or out on the image. ")

        st.write("<style>img {transform: scale("+str(zoom_level/100)+");}</style>",unsafe_allow_html= True)


    elif selectedInsight == "Forest Area":
        st.markdown("<h3 style='text-align:center; color:white; '>Univariate analysis and a boxplot of the dataset.", unsafe_allow_html=True)

        st.image("for.png",use_column_width=True)

        #zoom
        st.write("Zoom Slider:")
        zoom_level = st.slider("Zoom-Level", min_value=50, max_value=200, value=100, step=20)
        st.write("Use the slider to zoom in or out on the image. ")

        st.write("<style>img {transform: scale("+str(zoom_level/100)+");}</style>",unsafe_allow_html= True)


    elif selectedInsight=="GHG Emissions":

        st.markdown("<h3 style='text-align:center; color:white; '>Univariate analysis and a boxplot of the dataset.", unsafe_allow_html=True)

        st.image("ghg.png",use_column_width=True)

        #zoom
        st.write("Zoom Slider:")
        zoom_level = st.slider("Zoom-Level", min_value=50, max_value=200, value=100, step=20)
        st.write("Use the slider to zoom in or out on the image. ")

        st.write("<style>img {transform: scale("+str(zoom_level/100)+");}</style>",unsafe_allow_html= True)


    elif selectedInsight == "Global Living Planet":
        st.markdown("<h3 style='text-align:center;color:white; '>Univariate analysis and a boxplot of the dataset. ", unsafe_allow_html=True)

        st.image("glp.png",use_column_width=True)

        #zoom
        st.write("Zoom Slider:")
        zoom_level = st.slider("Zoom-Level", min_value=50, max_value=200, value=100, step=20)
        st.write("Use the slider to zoom in or out on the image. ")

        st.write("<style>img {transform: scale("+str(zoom_level/100)+");}</style>",unsafe_allow_html= True)

    elif selectedInsight == "Tree Cover Loss":
        st.markdown("<h3 style='text-align:center;color:white; '>Univariate analysis and a boxplot of the dataset", unsafe_allow_html=True)

        st.image("tcl.png", use_column_width=True)

        #zoom
        st.write("Zoom Slider: ")
        zoom_level = st.slider("Zoom-Level", min_value=50, max_value=200, value=100, step=20)
        st.write("Use the slider to zoom in or out on the image ")

        st.write("<style>img {transform: scale("+str(zoom_level/100)+");}</style>",unsafe_allow_html= True)

    elif selectedInsight == "Wheat Yields":
        st.markdown("<h3 style='text-align:center; color:white; '>Univariate analysis and a boxplot of the dataset.", unsafe_allow_html=True)

        st.image("wl.png",use_column_width=True)

        #zoom
        st.write("Zoom Slider:")
        zoom_level = st.slider("Zoom-Level", min_value=50, max_value=200, value=100, step=20)
        st.write("Use the slider to zoom in or out on the image. ")

        st.write("<style>img {transform: scale("+str(zoom_level/100)+");}</style>",unsafe_allow_html= True)

    elif selectedInsight == "Regression Analysis":
        
        st.markdown("<h3 style='text-align:center; color:white; '>Regression Analysis", unsafe_allow_html=True)


        st.image("reg.png",use_column_width=True)

        st.image("crr.png",use_column_width=True)

        #zoom
        st.write("Zoom Slider:")
        zoom_level = st.slider("Zoom-Level", min_value=20, max_value=100, value=40, step=20)
        st.write("Use the slider to zoom in or out on the image. ")

        st.write("<style>img {transform: scale("+str(zoom_level/100)+");}</style>",unsafe_allow_html= True)


    elif selectedInsight == "Margin of Error":
       
        st.image("moe.png",use_column_width=True)

        #zoom
        st.write("Zoom Slider:")
        zoom_level = st.slider("Zoom-Level", min_value=20, max_value=100, value=40, step=20)
        st.write("Use the slider to zoom in or out on the image. ")

        st.write("<style>img {transform: scale("+str(zoom_level/100)+");}</style>",unsafe_allow_html= True)

    elif selectedInsight == "Biodiversity Score":
        
        st.image("bds.png",use_column_width=True)

        #zoom
        st.write("Zoom Slider:")
        zoom_level = st.slider("Zoom-Level", min_value=50, max_value=200, value=100, step=20)
        st.write("Use the slider to zoom in or out on the image. ")

        st.write("<style>img {transform: scale("+str(zoom_level/100)+");}</style>",unsafe_allow_html= True)



    elif selectedInsight == "Four Lens":
        
        st.write("Displaying data from the Four Lens Excel file:")
        
        #read file
        df = pd.read_excel("4Lenses.xlsx")
        st.dataframe(df)

        st.markdown("<h3 style='text-align:center; color:white; '>To filter Data, click on the desired column", unsafe_allow_html=True)


        st.image("fo.png",use_column_width=True)

        st.write("Zoom Slider:")
        zoom_level = st.slider("Zoom-Level", min_value=50, max_value=200, value=70, step=20)
        st.write("Use the slider to zoom in or out on the image. ")

        st.write("<style>img {transform: scale("+str(zoom_level/100)+");}</style>",unsafe_allow_html= True)


        
#layout
def layout():
    st.set_page_config(layout="wide")
  
def main():

    layout()
    st.title(" Welcome to the Biodiversity Insights Dashboard ")

    st.markdown("<h2 style='text-align: left; color: white;'>This Dashboard will show you key insights and findings from the Biodiversity report created for KORU Impact Solutions.</h3>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: left; color: white;'>Please select an insight from the dropdown menu to explore:</h3>",unsafe_allow_html=True)
  
    
    st.markdown("---")

    
    insight_options=["Home","Agricultural Land", "Deforestation", "Forest Area","GHG Emissions", "Global Living Planet","Tree Cover Loss","Wheat Yields" , "Regression Analysis", "Margin of Error", "Biodiversity Score", "Four Lens"]
    selectedInsight =st.selectbox("Select Insight:", insight_options)
    
    #display insight
    displayInsights(selectedInsight)

if __name__ == "__main__":

    main()
