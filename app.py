import streamlit as st
import pandas as pd
import plotly.express as px

def load_data(data):
    return pd.read_csv(data)

def main():

    st.title("Maps App")
    world = load_data("worldcities.csv")
    menu = ["Home", "Advanced", "Attendees", "About"]
    choice = st.sidebar.selectbox("Menu",menu)
    color = st.sidebar.color_picker("Color", value="#9E1FA2")

    if choice=="Home":
        with st.expander("Data View"):
            st.dataframe(world)

        fig = px.scatter_mapbox(world, lat="lat", lon="lng", hover_name="city_ascii",
                                hover_data=["country","population"],
                                color_discrete_sequence=[color], zoom=1, height=700)
        
        fig.update_layout(mapbox_style="open-street-map")
        st.plotly_chart(fig)

    elif choice=="Advanced":
        countries_list = world['country'].unique().tolist()
        countries_list.sort()
        selected_country = st.sidebar.selectbox("Country", countries_list, index=94)
        with st.expander("Data View"):
            df = world[world['country']==selected_country]
            st.dataframe(df)

        fig = px.scatter_mapbox(df, lat="lat", lon="lng", hover_name="city_ascii",
                                hover_data=["country","population"],
                                color_discrete_sequence=[color], zoom=1, height=700)
        
        fig.update_layout(mapbox_style="open-street-map")
        st.plotly_chart(fig)

    elif choice=="Attendees":
        cities_list = world['city_ascii'].unique().tolist()
        #cities_list.sort()
        selected_city = st.multiselect("Cities", cities_list, default=["New Delhi"])
        with st.expander("Data View"):
            df = world[world['city_ascii'].isin(selected_city)]
            st.dataframe(df)

        fig = px.scatter_mapbox(df, lat="lat", lon="lng", hover_name="city_ascii",
                                hover_data=["country","population"],
                                color_discrete_sequence=[color], zoom=1, height=700)
        
        fig.update_layout(mapbox_style="open-street-map")
        st.plotly_chart(fig)

    else:
        st.subheader("About")

if __name__=="__main__":
    main()