from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.guest import Guest

@app.route('/admin')
def admin():
    if 'admin' in session:
        return redirect('/admin/view')
    else:
        return redirect('/admin/auth')

@app.route('/admin/auth')
def admin_auth():
    return render_template('admin_auth.html')


@app.route('/admin/auth/validate', methods = ["POST"])
def admin_auth_validate():
    if request.form['admin_password'] == "whatupdude2022":
        session['admin'] = 'Valid Admin in Session'
        return redirect('/admin/view')
    else:
        return redirect('/admin/auth')

@app.route('/admin/view')
def admin_view():
    guests = Guest.get_all_guests()
    return render_template('admin.html', guests = guests)

@app.route('/delete/<int:guest_id>')
def delete_guest(guest_id):
    Guest.delete_guest(data = {
        'id' : guest_id,
    })
    return redirect('/admin/view')