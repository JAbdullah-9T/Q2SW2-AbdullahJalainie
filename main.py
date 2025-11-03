from pyscript import document

def calculate_gwa():
    # Get input values
    name = document.getElementById("name").value
    student_id = document.getElementById("id").value
    tle = float(document.getElementById("tle").value)
    pe = float(document.getElementById("pe").value)
    music = float(document.getElementById("music").value)

    # Compute GWA
    gwa = (tle + pe + music) / 3

    # Display result
    result_html = f"""
        <p>Student Name: <strong>{name}</strong></p>
        <p>Student ID: <strong>{student_id}</strong></p>
        <p>General Weighted Average: <strong>{gwa:.2f}</strong></p>
    """
    document.getElementById("result").write(result_html)
