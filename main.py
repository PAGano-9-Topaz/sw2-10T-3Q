from pyscript import display, document

def intrams(e):

    Medical = document.querySelector('input[name="Medical"]:checked').value
    Online_Reg= document.querySelector('input[name="OnReg"]:checked').value
    Gradelevel = document.getElementById("Select1").value
    Section = document.getElementById("Select2").value

    Grades = ["G7", "G8", "G9", "G10"]
    Sections = ["TP", "SP", "RB", "EM", "JD"]

    # MedicalCheck = str(Medical)
    # Online_RegCheck = str(Online_Reg)
    # Selected1Check = str(Selected1)
    # Selected2Check = str(Selected2)

    if Medical == "Yes" and Online_Reg == "Yes" and Gradelevel == "G10" and Section == "TP":
        message = f"""Congratulations, your team is Red Bulldogs!"""

    elif Medical == "Yes" and Online_Reg == "Yes" and Gradelevel == "G10" and Section == "SP":
        message = f"""Congratulations, your team is Green Hornets!"""

    elif Medical == "Yes" and Online_Reg == "Yes" and Gradelevel == "G10" and Section == "EM":
        message = f"""Congratulations, your team is Yellow Tigers!"""

    elif Medical == "Yes" and Online_Reg == "Yes" and Gradelevel == "G10" and Section == "RB":
        message = f"""Congratulations, your team is Blue Bears!"""

    elif Medical == "Yes" and Online_Reg == "Yes" and Gradelevel == "G9" and Section == "RB":
        message = f"""Congratulations, your team is Red Bulldogs!"""

    elif Medical == "Yes" and Online_Reg == "Yes" and Gradelevel == "G9" and Section == "SP":
        message = f"""Congratulations, your team is Green Hornets!"""

    elif Medical == "Yes" and Online_Reg == "Yes" and Gradelevel == "G9" and Section == "TP":
        message = f"""Congratulations, your team is Yellow Tigers!"""

    elif Medical == "Yes" and Online_Reg == "Yes" and Gradelevel == "G9" and Section == "EM":
        message = f"""Congratulations, your team is Blue Bears!"""
    
    elif Medical == "Yes" and Online_Reg == "Yes" and Gradelevel == "G8" and Section == "JD":
        message = f"""Congratulations, your team is Red Bulldogs!"""

    elif Medical == "Yes" and Online_Reg == "Yes" and Gradelevel == "G8" and Section == "TP":
        message = f"""Congratulations, your team is Green Hornets!"""

    elif Medical == "Yes" and Online_Reg == "Yes" and Gradelevel == "G8" and Section == "SP":
        message = f"""Congratulations, your team is Yellow Tigers!"""

    elif Medical == "Yes" and Online_Reg == "Yes" and Gradelevel == "G8" and Section == "EM":
        message = f"""Congratulations, your team is Blue Bears!"""

    elif Medical == "Yes" and Online_Reg == "Yes" and Gradelevel == "G8" and Section == "RB":
        message = f"""Congratulations, your team is Blue Bears!"""
    
    elif Medical == "Yes" and Online_Reg == "Yes" and Gradelevel == "G7" and Section == "RB":
        message = f"""Congratulations, your team is Red Bulldogs!"""

    elif Medical == "Yes" and Online_Reg == "Yes" and Gradelevel == "G7" and Section == "SP":
        message = f"""Congratulations, your team is Green Hornets!"""

    elif Medical == "Yes" and Online_Reg == "Yes" and Gradelevel == "G7" and Section == "TP":
        message = f"""Congratulations, your team is Yellow Tigers!"""

    elif Medical == "Yes" and Online_Reg == "Yes" and Gradelevel == "G7" and Section == "EM":
        message = f"""Congratulations, your team is Blue Bears!"""

    elif Medical == "No" or Online_Reg == "No" and Gradelevel in Grades and Section in Sections:
        message = f"""Sorry, you are ineligible for a team. Please get a Medical clearance and finish your Online registration"""
        
    else: 
        message = f"""<p class='bold2'>⚠ No/incomplete items has been selected. Please complete the selection before generating your team.</p>"""
    
    document.getElementById("output1").innerHTML = message




