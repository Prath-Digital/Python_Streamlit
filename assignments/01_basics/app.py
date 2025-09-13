import streamlit as st

st.title("🧑🏻‍💻 Favourite coding language")
st.subheader("Please select your favourite programming language from the dropdown below:")

choices = ["Python", "JavaScript", "Java", "C++", "Ruby", "Go", "Swift", "Kotlin", "C#", "PHP", "TypeScript", "Rust", "Dart", "Scala", "Perl", "Haskell", "Lua", "R", "MATLAB", "Objective-C", "Shell", "PowerShell", "Visual Basic", "COBOL", "Fortran", "Ada", "Lisp", "Prolog", "Erlang", "Elixir", "Clojure", "F#", "Groovy", "Julia", "Crystal", "Nim", "OCaml", "Scheme", "Smalltalk", "Tcl", "VBScript", "ActionScript", "Awk", "Bash", "Batch", "D", "Delphi", "Hack", "J#", "LiveCode", "Modula-2", "NATURAL", "PL/I", "Q#", "Racket", "REXX", "SAS", "SPARK", "VHDL", "Verilog", "Zig", "Other"]

language = st.selectbox("Select your favourite programming language:", choices)

if language != "Other":
    st.success(f"Great choice! {language} is a fantastic programming language.")
else:
    other_language = st.text_input("Please specify your favourite programming language:")
    if other_language.strip() == "":
        st.error("Input cannot be empty. Please specify your favourite programming language.")
    elif other_language in choices:
        st.warning("This language is already in the dropdown. Please select it from the list above.")
    elif other_language:
        st.success(f"Great choice! {other_language} is a fantastic programming language.")
    else:
        st.error("Invalid input. Please specify a valid programming language.")

st.info("Thank you for sharing your favourite programming language!\nFeel free to explore more about it and happy coding!🚀\n- ***Prath-Digital*** 🧑🏻‍💻")