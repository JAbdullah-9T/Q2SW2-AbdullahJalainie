from pyscript import document

def calculate_gwa():
    # Get input values
    name = Element("name").value
    student_id = Element("id").value
    tle = float(Element("tle").value)
    pe = float(Element("pe").value)
    music = float(Element("music").value)

    # Compute GWA
    gwa = (tle + pe + music) / 3

    # Display result
    result_html = f"""
        <p>Student Name: <strong>{name}</strong></p>
        <p>Student ID: <strong>{student_id}</strong></p>
        <p>General Weighted Average: <strong>{gwa:.2f}</strong></p>
    """
    Element("result").write(result_html)