import streamlit as st

st.title("🍵 Coffee Maker App")

coffee_options = [
    "Espresso", "Latte", "Cappuccino", "Americano", "Frappuccino", "Mocha", "Macchiato", "Flat White", "Irish Coffee", "Turkish Coffee", "Ristretto", "Doppio", "Affogato", "Cortado", "Red Eye", "Black Eye", "Vienna Coffee", "Iced Coffee", "Nitro Coffee", "Cold Brew", "Bulletproof Coffee", "Cafe au Lait", "Cafe Breve", "Cafe con Leche", "Cafe Cubano", "Cafe de Olla", "Cafe Zorro", "Café Bombón", "Café Touba", "Café Miel", "Café con Hielo", "Café con Panna", "Café Marocchino", "Café Viennois", "Café Liégeois", "Café glacé", "Café frappé", "Café royale", "Café mocha frappé", "Café latte macchiato", "Café caramel macchiato", "Café hazelnut latte", "Café vanilla latte", "Café pumpkin spice latte", "Café coconut latte", "Café almond latte", "Café oat latte", "Café soy latte", "Café macadamia latte", "Café pecan latte", "Café walnut latte", "Café chestnut latte", "Café pistachio latte", "Café hazelnut mocha", "Café caramel mocha", "Café white chocolate mocha", "Café dark chocolate mocha", "Café peppermint mocha", "Café spiced mocha", "Café cinnamon mocha", "Café gingerbread mocha", "Café toffee nut latte", "Café butter pecan latte", "Café maple walnut latte", "Café honey almond latte", "Café lavender latte", "Café rose latte", "Café saffron latte", "Café turmeric latte", "Café matcha latte", "Café chai latte", "Café golden latte", "Café dirty chai", "Café London fog", "Café earl grey latte", "Café jasmine latte", "Café hibiscus latte", "Café rosehip latte", "Café chamomile latte", "Café peppermint latte", "Café lemongrass latte", "Café ginger latte", "Café turmeric ginger latte", "Café spiced turmeric latte", "Café cardamom latte", "Café nutmeg latte", "Café clove latte", "Café allspice latte", "Café pumpkin pie latte", "Café apple pie latte", "Café cinnamon roll latte", "Café s'mores latte", "Café tiramisu latte", "Café cannoli latte", "Café baklava latte", "Café churro latte", "Café tres leches latte", "Café flan latte", "Café dulce de leche latte", "Café coconut cream latte", "Café banana latte", "Café strawberry latte", "Café blueberry latte", "Café raspberry latte", "Café blackberry latte", "Café mixed berry latte", "Café tropical latte", "Café mango latte", "Café pineapple latte", "Café passion fruit latte", "Café guava latte", "Café lychee latte", "Café dragon fruit latte", "Café acai latte", "Café pomegranate latte", "Café cranberry latte", "Café fig latte", "Café date latte", "Café persimmon latte", "Café quince latte", "Café kumquat latte", "Café starfruit latte", "Café jackfruit latte", "Café durian latte", "Café rambutan latte", "Café longan latte", "Café sapodilla latte", "Café soursop latte", "Café breadfruit latte", "Café cherimoya latte", "Café salak latte", "Café mangosteen latte", "Other"
]

if "show_select" not in st.session_state:
    st.session_state.show_select = False

if st.button("Start Making Coffee"):
    st.session_state.show_select = True

if st.session_state.show_select:
    st.subheader("Select your coffee type:")

    coffee_type = st.selectbox("Choose your coffee:", coffee_options, key="coffee_type")
    if coffee_type == "Other":
        other_coffee = st.text_input("Please specify your coffee type:", key="other_coffee")
        if other_coffee.strip() == "":
            st.error("Input cannot be empty. Please specify your coffee type.")
        elif other_coffee in coffee_options:
            st.warning("This coffee is already in the dropdown. Please select it from the list above.")
        elif other_coffee:
            st.success(f"Great choice! {other_coffee} is a fantastic coffee.")
        else:
            st.error("Invalid input. Please specify a valid coffee type.")
        selected_coffee = other_coffee
    else:
        selected_coffee = coffee_type
        st.write(f"You selected: {selected_coffee}")

    st.subheader("Customize your coffee:")
    milk_type = st.radio("Choose your milk type:", ["Whole Milk", "Skim Milk", "Soy Milk", "Almond Milk", "Oat Milk", "Coconut Milk", "No Milk"])

    st.write(f"You selected: {milk_type}")

    if "show_toppings" not in st.session_state:
        st.session_state.show_toppings = False

    if st.button("Add Toppings"):
        st.session_state.show_toppings = True

    if st.session_state.show_toppings:
        toppings = [
            "Whipped Cream", "Chocolate Syrup", "Caramel Syrup", "Cinnamon", "Nutmeg", "Marshmallows", "Crushed Cookies", "Sprinkles", "Honey", "Maple Syrup", "Peanut Butter", "Almond Butter", "Hazelnut Spread", "Coconut Flakes", "Chopped Nuts", "Fresh Fruit", "Dried Fruit", "Granola", "Cereal", "Oats", "Chia Seeds", "Flax Seeds", "Hemp Seeds", "Pumpkin Seeds", "Sunflower Seeds", "Goji Berries", "Cacao Nibs", "Matcha Powder", "Turmeric Powder", "Cinnamon Powder", "Nutmeg Powder", "Clove Powder", "Cardamom Powder", "Ginger Powder", "Allspice Powder", "Vanilla Extract", "Almond Extract", "Peppermint Extract", "Other"
        ]
        selected_toppings = []

        for topping in toppings:
            if st.checkbox(topping, key=f"topping_{topping}"):
                selected_toppings.append(topping)

        if "Other" in selected_toppings:
            other_topping = st.text_input("Please specify your topping:", key="other_topping")
            if other_topping.strip() == "":
                st.error("Input cannot be empty. Please specify your topping.")
            elif other_topping in toppings:
                st.warning("This topping is already in the list. Please select it above.")
            elif other_topping:
                st.success(f"Great choice! {other_topping} is a fantastic topping.")
                selected_toppings.append(other_topping)
            else:
                st.error("Invalid input. Please specify a valid topping.")

        # Remove 'Other' from the display list if custom topping is provided
        display_toppings = [t for t in selected_toppings if t != "Other"]

        if display_toppings:
            st.write("You selected toppings:")
            st.write(", ".join(display_toppings))
        else:
            st.write("No toppings selected.")

        st.subheader("Select sugar level:")
        sugar_level = st.slider("Choose your sugar level (in teaspoons):", 0, 7, 4)
        st.write(f"You selected {sugar_level} teaspoons of sugar.")

        st.subheader("How many cups would you like to make?")
        cup_count = st.number_input("Enter the number of cups:", min_value=1, value=1, step=1)
        st.write(f"You selected {cup_count} cup(s).")

        st.subheader("Information about you:")
        full_name = st.text_input("Enter your full name:")
        email = st.text_input("Enter your email:")
        age = st.number_input("Enter your age:", min_value=0)
        dob = st.date_input("Enter your date of birth:")

        if full_name and email and age and dob:
            st.success("Thank you for providing your information!")
            st.write("Your Information:")
            st.write(f"Name: {full_name}")
            gmail_link = f"https://mail.google.com/mail/?view=cm&fs=1&to={email}"
            st.markdown(f"**Email:** [📧 {email}]({gmail_link})")
            st.write(f"Age: {age}")
            st.write(f"Date of Birth: {dob}")

            st.write(f"Thank you, {full_name}! Your {selected_coffee} with {milk_type}, {sugar_level} tsp of sugar, and {', '.join(display_toppings) if display_toppings else 'no toppings'} is on the way. Enjoy your coffee!")
        else:
            st.warning("Please fill in all your information.")

        
