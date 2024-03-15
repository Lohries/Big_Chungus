import streamlit as st 
import cv2 as cv
from model_st import *
import numpy as np


def main():
    image_increment = 15
    mathcing = 0
    st.title("Brain Project - Second Part")
    st.header("The objective of this project is to complemente the studies arround deepface, like the real time functoinalities. That's why I created my version of the world wide famous Tinder.")

    st.text("Place your data if you want to make part of this big database")
    x = st.text_input("Name")
    y = slider = st.slider("Range of age", 5, 65)
    if slider <= 17:
        st.write("You are crazy dude, get out of that shit. You don't have the right age")
    elif slider >= 18 and slider < 50:
        st.write("Now that's aceptable")
    elif slider >= 50:
        st.write("I'm suprised that you come so far")

    if x and y:
        image = st.camera_input("Camera Input")

        if image:
            
            if st.button("Insert"):
                image_increment += 1
                with open (f'img/img{image_increment}.jpg','wb') as file:
                    file.write(image.getbuffer())

 

        

    with st.sidebar:
        st.header("Select the parameters that you like in your future love")
        feelings_1 = st.radio("Mark your type of person", ["Happy", "Neutral", "Sad"])
        if feelings_1 == "Happy":
            st.write("A happy couple ")
            feelings_1 = 'happy'
        elif feelings_1 == "Neutral":
            st.write("A conserviter couple")
            feelings_1 = 'neutral'
        else:
            st.write("Ok, peculiar tastes")
            feelings_1 = 'sad'
        print(feelings_1)

        feelings_2 = st.radio("Select the best age", ["Young (18<)", "Adults (30<)", "Sugar Daddy/Mummy (55<)"])
        if feelings_2 == "Young (18<)":
            st.write("Red flag")
            feelings_2 = 18
        elif feelings_2 == "Adults (30<)":
            st.write("Similar ages, similar tastes")
            feelings_2 = 30
        else:
            st.write("Are you interest in the money, aren't you ?")
            feelings_2 = 55
        print(feelings_2)
        
        feelings_3 = st.radio("Select the gender", ["Male", "Female"])
        if feelings_3 == "Male":
            st.write("So you like boys")
            feelings_3 = 'male'
        elif feelings_3 == "Female":
            st.write("The girls are waiting for you")
            feelings_3 = 'female'

        print(feelings_3)

        feelings_4 = st.radio("Select race", ["White", "Black", "Indian", "Middle East", "Asian", "Latino"])
        if feelings_4 == "White":
            feelings_4 = 'white'
            pass
        elif feelings_4 == "Black":
            feelings_4 = 'black'
            pass
        elif feelings_4 == "Indian":
            feelings_4 = 'indian'
            pass
        elif feelings_4 == "Middle East":
            feelings_4 = 'middle eastern'
            pass
        elif feelings_4 == "Asian":
            feelings_4 = 'asian'
        else:
            feelings_4 = 'latino hispanic'

        #print(feelings_4)
        


        list1 =  [feelings_1, feelings_2, feelings_3, feelings_4]

        #print(list1)

        if st.button("Submit"):
            img_adress = data_base_analyze(list1)
    
            st.image(f'img/img{img_adress}.jpg')
        

        

if __name__ == "__main__":

    main()
