from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
from flask_app.models.spellbook_model import Spellbook
from flask_app.models.spell_model import Spell
bcrypt = Bcrypt(app)

@app.route('/directory')
def render_directory():
    if 'user_id' not in session:
        flash('Please login to access this page.', 'login')
        return redirect('/')
    spellbooks = Spellbook.get_all_by_id({'id':session['user_id']})
    return render_template('spell_directory.html', spellbooks = spellbooks)

@app.route('/library')
def render_library():
    if 'user_id' not in session:
        flash('Please login to access this page.', 'login')
        return redirect('/')
    spellbooks = Spellbook.get_all_by_id({'id':session['user_id']})
    return render_template('library.html', spellbooks = spellbooks)

@app.route('/spellbook/<int:id>')
def render_spellbook(id):
    if 'user_id' not in session:
        flash('Please login to access this page.', 'login')
        return redirect('/')
    spellbooks = Spellbook.get_all_by_id({'id':session['user_id']})
    spellbook = Spellbook.get_one_by_id({'id':id})
    spells0 = Spell.get_spell_information({'spellbook_id':id,'spell_level':0})
    print(spells0)
    spells1 = Spell.get_spell_information({'spellbook_id':id,'spell_level':1})
    spells2 = Spell.get_spell_information({'spellbook_id':id,'spell_level':2})
    spells3 = Spell.get_spell_information({'spellbook_id':id,'spell_level':3})
    spells4 = Spell.get_spell_information({'spellbook_id':id,'spell_level':4})
    spells5 = Spell.get_spell_information({'spellbook_id':id,'spell_level':5})
    spells6 = Spell.get_spell_information({'spellbook_id':id,'spell_level':6})
    spells7 = Spell.get_spell_information({'spellbook_id':id,'spell_level':7})
    spells8 = Spell.get_spell_information({'spellbook_id':id,'spell_level':8})
    spells9 = Spell.get_spell_information({'spellbook_id':id,'spell_level':9})
    return render_template('spellbook_display.html', spellbooks = spellbooks, spellbook = spellbook, spells0=spells0, spells1=spells1, spells2=spells2, spells3=spells3, spells4=spells4, spells5=spells5, spells6=spells6, spells7=spells7, spells8=spells8, spells9=spells9,)

@app.route('/new_spellbook')
def render_new_spellbook_page():
    if 'user_id' not in session:
        flash('Please login to access this page.', 'login')
        return redirect('/')
    return render_template('create_spellbook.html')

@app.route('/spellbook/create', methods=['POST'])
def create_spellbook():
    if 'user_id' not in session:
        flash('Please login to access this page.', 'login')
        return redirect('/')
    #! VALIDATE
    if not Spellbook.validate_spellbook(request.form):
        return redirect('/new_spellbook')
    data = {
        "name":request.form['spellbook_name'],
        "wielder_name":request.form['wielder_name'],
        "wielder_class":request.form['wielder_class'],
        "wielder_level":request.form['level'],
        "user_id":session['user_id']
    }
    Spellbook.create_spellbook(data)
    return redirect('/library')

@app.route('/spellbook/<int:id>/delete')
def delete_spellbook(id):
    if 'user_id' not in session:
        flash('Please login to access this page.', 'login')
        return redirect('/')
    data1 = {
        'spellbook_id':id,
    }
    data2 = {
        "id":id
    }
    Spell.delete_all_spells_from_spellbook(data1)
    Spellbook.delete_spellbook(data2)
    return redirect('/library')

@app.route('/spellbook/<int:id>/delete/<int:id2>')
def delete_spell(id,id2):
    if 'user_id' not in session:
        flash('Please login to access this page.', 'login')
        return redirect('/')
    data = {
        'spellbook_id':id,
        'spell_id':id2
    } 
    Spell.delete_single_spell_from_spellbook(data)
    return redirect (f'/spellbook/{id}')

@app.route('/spell/link', methods=['POST'])
def link_spells():
    if 'user_id' not in session:
        flash('Please login to access this page.', 'login')
        return redirect('/')
    # ! if statement to determine if the spell is already in the database
    if request.form['spellbook_id'] == "":
        flash('Please select a spellbook to add a spell.', 'spellbook')
        return redirect('/directory')
    spell_id = Spell.insert_spell_into_db({
        'name':request.form['spell_name'],
        'description':request.form['desc'],
        'higher_level':request.form['higher_level'],
        'range':request.form['range'],
        'components':request.form['components'],
        'material':request.form['material'],
        'ritual':request.form['ritual'],
        'casting_time':request.form['casting_time'],
        'duration':request.form['duration'],
        'concentration':request.form['concentration'],
        'level_int':request.form['level_int'],
        'school':request.form['school'],
        'level':request.form['level']
        })
    Spell.link_spell_to_spellbook({'spellbook_id':request.form['spellbook_id'],'spell_id':spell_id})
    return redirect('/directory')