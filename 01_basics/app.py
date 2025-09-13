import streamlit as st

st.title("Hello, Streamlit!")
st.subheader("This is a subheader")
st.text("This is a simple text element.")
st.write("This is a simple write element")

choice = st.selectbox("Choose your favourite cold drink company:", ["Coca Cola", "Sprite", "Thums Up", "Pepsi", "Dr. Pepper", "Red Bull", "Mountain Dew", "Mazza", "Frooti", "Nestle", "Slice", "Fanta", "Mirinda", "7 Up", "Limca", "Appy Fizz", "Coco Cola", "Minute Maid", "Tropicana", "Real", "Paper Boat", "Bovonto", "Maaza", "Rasna", "Citra", "Orangina", "Sunkist", "Jarritos", "Inca Kola", "Lemonade", "Ginger Ale", "Club Soda", "Tonic Water", "Sparkling Water", "Flavored Water", "Iced Tea", "Lassi", "Chaas", "Nimbu Pani", "Sharbat", "Aam Panna", "Jaljeera", "Cucumber Cooler", "Mint Mojito", "Virgin Mary", "Fruit Punch", "Smoothies", "Milkshakes", "Hot Chocolate", "Coffee", "Tea", "Herbal Tea", "Green Tea", "Black Tea", "Oolong Tea", "White Tea", "Chai", "Masala Chai", "Bubble Tea", "Kombucha", "Other"])

if choice == "Other":
    other_choice = st.text_input("Please specify your favourite cold drink company:")
    if other_choice == "":
        st.error("You did not specify any company.")
    else:
        st.write("Your favourite cold drink company is:", other_choice)
else:
    st.write("Your favourite cold drink company is:", choice)