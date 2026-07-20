import streamlit as st
# Title
st.title("Rural Scholarship Finder")
st.write("Welcome to Rural Scholarship Finder!")
st.write("Helping Rural Students Discover Scholarship Opportunities Based On Academics, Location, and Eligibility.")
st.write("")
# User Input
with st.sidebar:
    st.header("About This App")
    st.write(""" The Rural Scholarship Finder was created to help southern students from rural communities discover scholarship opportunities that are often difficult to find in one place.

    Many students attend schools with limited college counseling resources. This app makes searching for scholarships easier by allowing users to filter opportunities based on certain criteria.""")
    st.divider()
    st.header ("About Me!")
    st.write(""" 
    Hello! My name is Hunter Baugh and I am a high school students from rural Tennessee. I know firsthand how overwhelming it can be to find college resources, and so I decided to make this app in order to help students like me have an easier time than I did.""")
    st.markdown("""
    <style>
    [data-testid="stImage"] img{border-radius: 20px; box-shadow:0 6px 18px rgba(0,0,0,0.2)}
    </style>
    """, unsafe_allow_html=True)
name = st.text_input("What is your name?")
state = st.text_input("What state do you live in?").strip().lower()
gpa = st.number_input("What is your GPA?", min_value=0.0, max_value=5.0, step=0.1) 
act_input = st.text_input ("What is your ACT score? (Leave blank if you have not taken it)")
income_input = st.text_input("What is your annual household income? (Numbers only, skip if unknown): $")
if income_input == "":
    income = None
else:
    income = int(income_input) 
if act_input == "":
    act = 0
else:
    act = int(act_input)
rural = st.selectbox("Do you live in a rural area?", ["Yes", "No"]) 
# Button
if st.button ("Find Scholarships!"):
    scholarships = []
    st.write ("### Searching for scholarships...")
scholarships = []
# Rural Scholarships
if rural == "Yes" and act >= 21 and gpa >= 3.0: 
      scholarships.append({
          "name": "USDA 1890 National Scholars Program",
          "details": "GPA 3.0+ | ACT 21+ | Agriculture, food, natural resources, or related majors | Rural/underserved students | Leadership and service required"}) 
# GPA Scholarships
if gpa <2.5:
    print ("Unfortunately, we could not find scholarships that allow for a GPA of 2.5 or lower.")
if gpa >= 3.5:
    scholarships.append({
        "name": "Coca-Cola Scholars Program",
        "details": "U.S. high school seniors | Leacdership, service, and academic achievement | Competitive national scholarship"}) 
if gpa >= 3.8:
    scholarships.append({
        "name": "Jack Kent Cooke Foundation Scholarship",
        "details": "High-achieving students with financial need | Strong academics and leadership experience"}) 
# ACT Scholarships
if act == "":
    print("We will match you using GPA and other factors.") 
if act >=30:
      scholarships.append({
          "name": "University Merit Scholarships",
          "details": "ACT 30+ | Competitive merit awards at many colleges | GPA requirements may apply"}) 
if act >=33:
      scholarships.append({
          "name": "Top-Tier Academic Merit Scholarships",
          "details": "ACT 33+ | Strong academic achievement | Competitive university merit awards, results vary by college | GPA requirements may apply"})
# Tennessee Scholarships
if state.lower() in {"tennessee", "tn"}:
      scholarships.append({
          "name": "Tennessee Promise",
          "details": "Tennessee residents | Community or technical college tuition assistance | Maintain 2.0 college GPA"})
      scholarships.append({
           "name": "Tennessee Student Assistance Award (TSAA)",
           "details": "Tennessee residents | Undergraduate students | Financial need required | FAFSA required | No ACT requirement"}) 
      if gpa >= 3.0 or act >= 21:
          scholarships.append({
          "name": "Tennessee HOPE Scholarship",
          "details": "Tennessee residents | 3.0 weighted GPA OR ACT 21+ (or equivalent SAT score)| High School graduates | Covers tuition and mandatory fees at eligible community and technical colleges"})
          scholarships.append({
              "name": " Carolyn Morrison Scholarship Fund",
              "details": "3.0+ OR 21+ ACT score | Preference given to students from Highlands of Tennessee (Overton, Putnam, and White counties)"})
      if rural.lower() == "yes" and gpa >= 3.5 and income is not None and income <= 100000:
          scholarships.append({
              "name": "Hagan Scholarship Foundation",
              "details": "Must attend public high school | Live in county or town with population under 50,000 | 3.5 GPA and household income under 100,000"}) 
# Alabama Scholarships
if state.lower() in {"alabama", "al"}:
    if gpa >=2.75:
        scholarships.append({
            "name": "CollegeCounts Scholarships - Alabama",
            "details": "Alabama Students | GPA 2.75+ | Financial Need Considered" })
    if gpa >=3.0:
        scholarships.append({
            "name": "Alabama Community Foundation Scholarships",
            "details": "Alabama students | GPA 3.0+ | Requirements vary by scholarship | Includes academic, leadership, and community-based awards"})
# Georgia Scholarships
if state.lower in {"alabama", "al"}:
    if gpa >= 2.5:
         scholarships.append({
             "name": "REACH Georgia Scholarship Program",
             "details": " Georgia students | Need-based scholarship support | Academic and behavioral requirements"})
    if gpa >= 3.0:
        scholarships.append ({
            "name": "Georgia HOPE Scholarship Program",
            "details": "Georgia residents | 3.0 HOPE GPA required | Merit-based financial aid"}) 
    if gpa >=3.7 and act >=26:
        scholarships.append({
            "name": "Georgia Zell Miller Scholarship",
            "details": "Georgia students | Higher academic requirements than HOPE | Merit-based aid"}) 
# Mississippi Scholarships
if state.lower in {"mississippi","ms"}:
    if gpa >= 2.5:
        scholarships.append({
            "name": "Mississippi Community Foundation Scholarships",
            "details": "Mississippi residents | Requirements vary | Local academic and community scholarships"}) 
    if gpa >= 2.5 and act >= 15:
        scholarships.append({
            "name": "Mississippi Tuition Assistance Grant (MTAG)",
            "details": " Mississippi residents | Undergraduate students | State financial aid program"}) 
    if gpa >= 3.5 and act >= 29:
        scholarships.append({
            "name": "Mississippi Eminent Scholars Grant",
            "details": "Mississippi residents | Strong academic achievement required | Merit-based aid"})
    if gpa>= 2.5 and act >= 20 and income is not None and income <= 39500:
        scholarships.append({
            "name" : "Higher Education Legislative Plan (HELP) Grant",
            "details": "Minimum 2.5 GPA | Minimum 20 ACT | Parents' Adjusted Gross Income must be 39500 or less| Must complete the 15.5 unit HELP Core Curriculum in high school"})
# Results
st.divider()
if len(scholarships) == 0:
    st.write ("Sorry, no scholarships were found.")
else:
    st.write(f"## Results for {name}")
    st.write("You may qualify for:")
    for scholarship in scholarships:
        with st.container(): 
            st.subheader(scholarship["name"])
            st.write(scholarship["details"])
