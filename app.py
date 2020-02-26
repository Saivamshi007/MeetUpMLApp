import os
import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
from PIL import Image
import plotly.express as px



def file_selector(folder_path='./datasets'):
            filenames=os.listdir(folder_path)
            selected_filename=st.selectbox("select A file",filenames)
            return os.path.join(folder_path,selected_filename)


def main():

    st.info("Stramlit documentaion are very much fun to read, it is not like the common hestic doc of other tech. I reccomand all our group members to read it")
    st.info("link for doc:https://streamlit.io/docs/api.html")
  
    st.title("Dataset Explorer Steamlit App")
    image=Image.open("assistant.jpeg")

    st.image(image, caption='Hi iam your assistant! lets have a Tour over this App',use_column_width=True)

    user_name=st.text_input("Please Enter Your Name")

    st.write("Cool!{}, Lets go ahead".format(user_name))

    filename=file_selector()
    st.write("you selected {}".format(filename))
    df=pd.read_csv(filename)

    if st.checkbox("Show datasets"):
        number=st.number_input("Number of Rows to view",5,10)
        st.dataframe(df.head(number))


    if st.button("Column names"):
        st.write(df.columns)
    if st.checkbox("Shape of the dataset"):
        st.write(df.shape)
        data_dim=st.radio("show Dimension By",("Rows","Column"))
        if data_dim=="Rows":
            st.text("Number of Rows")
            st.write(df.shape[0])
        elif data_dim=="Column":
            st.text("Number of Rows")
            st.write(df.shape[1])
        else:
            st.write(df.shape)





    if st.checkbox("Seelet cloumns To show"):
        all_columns=df.columns.tolist()
        selected_columns=st.multiselect("select",all_columns)
        new_df=df[selected_columns]
        st.dataframe(new_df)

    if st.button("Check the value count"):
        st.text("Value count by Target/Class")
        st.write(df.iloc[ :,-1].value_counts())

    if st.button("Data Types"):
        st.write(df.dtypes)

    if st.button("Summary of the DataSet"):
        st.write(df.describe().T)

    st.subheader("Data Visualization")

    st.subheader("Plots")


    all_columns_names=df.columns.tolist()
    type_Of_plot=st.selectbox("Select Type of pllot",["area","bar","line","hist","box","kde","Scatter Plot"])
    selected_columns_names=st.multiselect("Select Columns To Plot",all_columns_names)

    st.write("Steamlit Comes With its in build Plots :sunglasses:")
    st.write("if you want to save this plots you can do it by clicking the circle near the plot. This only works for Streamlit Generated plots")

    if st.button("Generate Plot"):
        st.success("Produce plot for {}  and {}".format(type_Of_plot,selected_columns_names))


    if type_Of_plot=='area':
        cust_data=df[selected_columns_names]
        st.area_chart(cust_data)

    if type_Of_plot=='bar':
        cust_data=df[selected_columns_names]
        st.bar_chart(cust_data)

    if type_Of_plot=='line':
        cust_data=df[selected_columns_names]
        st.line_chart(cust_data)

    if type_Of_plot=="Scatter Plot":
         X=selected_columns_names[0]
         Y=selected_columns_names[1]
      
         fig = px.scatter(df, x =X,y=Y)
# Plot!
 
 
         st.plotly_chart(fig)



    if type_Of_plot:
        st.write("Below are matplotlib Plots")
        cust_plot=df[selected_columns_names].plot(kind=type_Of_plot)
        st.write(cust_plot)
        st.pyplot()


    if st.button("Pie Plot"):
        all_columns_names=df.columns.tolist()
        st.success("Generating your plot")
        st.write(df.iloc[:,-1].value_counts().plot.pie(autopct="%1.1f%%"))
        st.pyplot()

    if st.checkbox("Correlation Polt"):
        st.write(sns.heatmap(df.corr(),annot=True))
        st.pyplot()
   


    if st.checkbox("Value count"):
        st.text("Value count by Target")
        all_columns_names=df.columns.tolist()
        primary_col=st.selectbox("Primary column to GroupBy",all_columns_names)
        selected_columns_names=st.multiselect("Select Columns",all_columns_names)
        if st.button("Plot"):
            st.text("Generate Plot")
            if selected_columns_names:
                vc_plot=df.groupby(primary_col)[selected_columns_names].count()
            else:
                vc_plot=df.iloc[:,-1].value_counts()
            st.write(vc_plot.plot(kind='bar'))
            st.pyplot()



    if st.button("Click me to get Excited"):
        st.balloons()




  
      




        

        
        

if __name__== '__main__' : 
    main()
