from flask import Flask, render_template, request, redirect, url_for, send_file
import re
import os

app = Flask(__name__)

contacts = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contacts')
def display_contacts():
    return render_template('display_contacts.html', contacts=contacts)

@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        user_name = request.form['name']
        user_number = request.form['phone_number']
        phone_number_pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
        if not phone_number_pattern.match(user_number):
            return render_template('add_contact.html', error="Invalid phone number format. Please use ###-###-####.")
        contacts.append({"name": user_name, "phone_number": user_number})
        return redirect(url_for('display_contacts'))
    return render_template('add_contact.html')

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_contact(index):
    if request.method == 'POST':
        contacts[index]['name'] = request.form['name']
        contacts[index]['phone_number'] = request.form['phone_number']
        return redirect(url_for('display_contacts'))
    return render_template('edit_contact.html', contact=contacts[index], index=index)

@app.route('/delete/<int:index>')
def delete_contact(index):
    del contacts[index]
    return redirect(url_for('display_contacts'))

@app.route('/export')
def export_contacts():
    file_name = "my_contacts.txt"
    with open(file_name, "w") as file:
        for contact in contacts:
            file.write(f"{contact['name']},{contact['phone_number']}\n")
    return send_file(file_name, as_attachment=True)

@app.route('/import')
def import_contacts():
    file_name = "my_contacts.txt"
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            for line in file:
                name, phone_number = line.strip().split(",")
                contacts.append({"name": name, "phone_number": phone_number})
        return redirect(url_for('display_contacts'))
    return "No contacts to import"

if __name__ == '__main__':
    app.run(debug=True)

