from crypt import methods
from flask import Blueprint, render_template, redirect, request, url_for, flash
from .models import Arcade, Time
from .forms import TimeForm, RegisterMachine

from .utils.db import db

auth = Blueprint("auth", __name__)
page = Blueprint("page", __name__)

from .controls.admin import ControlMachines
from .controls.ping import veryfi_ping_machine



################ (RUTAS DEL PANEL) ################
@page.route("/", methods=["GET", "POST"])
def index():
    return redirect(url_for('page.add_time'))


@page.route('/add_machines', methods=['GET', 'POST'])
def add_machines():
    form = RegisterMachine()
    if request.method == 'POST':
         if form.validate_on_submit():
              
              arcade = Arcade(name=form.name.data, ip=form.ip.data, description=form.description.data)
              db.session.add(arcade)
              db.session.commit()
              return redirect(url_for('page.add_machines'))
    return render_template('add.html', form=form)

@page.route("/add_time", methods=["GET", "POST"])
def add_time():
    form = TimeForm()
    machines = Arcade.query.with_entities(Arcade.id, Arcade.name, Arcade.ip).all()
    machines_on = veryfi_ping_machine(machines)
    
    data = {
        'machines': machines, 
        'list_machines': machines_on, 
    }
    

    if request.method == "POST":
         # Buscamos la maquina en la db
            machine_db = Arcade.query.filter_by(id=request.form["machine"]).first()
            
            if machine_db:
            # guardamos la hora y minuto en una lista
                datos = [form.hour.data, form.minute.data]

                # Instanciamos la la clase para enviar los datos a la maquina y dar tiempo
                control = ControlMachines(machine_db.ip, datos)
                if control.ping_machine() is None:
                    flash(f'Connection not found: {request.form["machine"]}')
                    return redirect(url_for("page.add_time"))
                else:

                    if control.add_time_machine() == "timeout":
                        flash(
                            f'Error, tiempo de espera en conectar termino: {machine_db.name}'
                        )
                        return redirect(url_for("page.add_time"))
                    elif control.add_time_machine() == "connect":
                        flash(f'Error, {machine_db.name} rechazo la conexion')
                        return redirect(url_for("page.add_time"))
                    elif control.add_time_machine():
                        credit_machine = Time(employee_id=1, hour=form.hour.data, minute=form.minute.data, price=form.price_time.data, machine_id=machine_db.id, description=form.description.data)
                        db.session.add(credit_machine)
                        db.session.commit()
                        flash(f'Se agrego tiempo a la maquina correctamente: {machine_db.name}', 'success')
                        return redirect(url_for("page.add_time"))

           

    return render_template("time.html", form=form, data=data)

@page.route('/reset_time', methods=['GET', 'POST'])
def reset_time():

    machines_all = Arcade.query.options(db.load_only(Arcade.id, Arcade.name)).all()
    if request.method == 'POST':
        machine = Arcade.query.filter_by(id=request.form['machine']).first()
        datos = [None]
        control = ControlMachines(machine.ip, datos)
        if control.ping_machine() is None:
            flash('No se pudo resetear el tiempo')
        else:
            if control.add_time_machine() == "timeout":
                    flash(
                            f'Error, tiempo de espera en conectar termino: {machine.name}'
                        )
                    return redirect(url_for("page.reset_time"))
            elif control.add_time_machine() == 'connect':
                        
                    flash(f'Error, {machine.name} rechazo la conexion')
                    return redirect(url_for("page.reset_time"))
            elif control.add_time_machine():
                flash(f'Se reseteo el tiempo correctamente: {machine.name}', 'success')
                return redirect(url_for('page.reset_time'))
                
        return redirect(url_for('page.reset_time'))
    return render_template('reset.html', machines_all=machines_all)


