import streamlit as st

st.title("🍵 Coffee Voting App")
st.subheader("Vote for your favourite coffee:")

name = st.sidebar.text_input("Enter your name to confirm your vote:")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Frappucino")
    st.image(
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1OICu_tWtCca78j1tPNbB3eO9Fw0KGAupdg&s",
        width=150,
    )
    fp = st.button("Vote for Frappucino", disabled=not bool(name))

with col2:
    st.subheader("Cappuccino")
    st.image(
        "data:image/jpeg;base64,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",
        width=150,
    )
    cp = st.button("Vote for Cappuccino", disabled=not bool(name))

if cp:
    st.session_state.selected_coffee = "Cappuccino"
    st.success("Thank you for voting Cappuccino!")
elif fp:
    st.session_state.selected_coffee = "Frappucino"
    st.success("Thank you for voting Frappucino!")

if name:
    if "selected_coffee" in st.session_state:
        st.sidebar.success(
            f"Thank you {name}! You voted for {st.session_state.selected_coffee}."
        )
        if st.session_state.selected_coffee == "Cappuccino":
            with st.expander("Cappuccino Making steps at home ☕"):
                st.markdown(
                    """
**Ingredients:**
- 1/3 cup of espresso or strong brewed coffee
- 1/3 cup of steamed milk
- 1/3 cup of milk foam
- Sugar (optional)
- Cocoa powder or cinnamon for garnish (optional)

**Instructions:**
1. Brew a shot of espresso or make a strong cup of coffee.
2. Steam the milk until it's hot and frothy. You can use a milk frother or heat the milk on the stove and whisk it vigorously.
3. Pour the espresso into a cup.
4. Add sugar to taste if desired.
5. Pour the steamed milk over the espresso, holding back the foam with a spoon.
6. Spoon the milk foam on top of the drink.
7. Garnish with a sprinkle of cocoa powder or cinnamon if desired.
8. Serve immediately and enjoy your homemade cappuccino!
                """
                )
            with st.expander("Fun Fact about Cappuccino ☕"):
                st.markdown(
                    """
Did you know? The cappuccino is named after the Capuchin friars, whose brown robes reminded people of the color of the drink. Enjoy your cappuccino with a sprinkle of cocoa powder or cinnamon on top for an extra touch of flavor!
                    """
                )
        elif st.session_state.selected_coffee == "Frappucino":
            with st.expander("Frappucino Making steps at home 🍹"):
                st.markdown(
                    """
**Ingredients:**
- 1 cup of strong brewed coffee, cooled
- 1 cup of milk (whole, skim, or any plant-based milk)
- 2 cups of ice
- 2-3 tablespoons of sugar or sweetener (adjust to taste)
- Whipped cream (optional)
- Chocolate syrup or caramel sauce for garnish (optional)

**Instructions:**
1. Brew a cup of strong coffee and let it cool to room temperature.
2. In a blender, combine the cooled coffee, milk, ice, and sugar.
3. Blend until smooth and frothy. If the mixture is too thick, you can add a little more milk.
4. Taste and adjust the sweetness if needed by adding more sugar or sweetener.
5. Pour the frappucino into a tall glass.
6. Top with whipped cream if desired.
7. Drizzle chocolate syrup or caramel sauce on top for extra flavor.
8. Serve immediately with a straw and enjoy your homemade frappucino!
                """
                )
            with st.expander("Fun Fact about Frappucino 🍹"):
                st.markdown(
                    """
Did you know? The Frappuccino was created by blending a Starbucks coffee with ice and other ingredients to create a refreshing beverage. It's a popular choice for those who enjoy a cold, sweet coffee treat!
                    """
                )
        st.balloons()
    else:
        st.sidebar.warning("Please select a coffee to vote for.")

st.info("Thank you!\nFeel free to explore more about it and happy coding!🚀\n- ***Prath-Digital*** 🧑🏻‍💻")
