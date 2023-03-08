let school_filter = "";
let current_spellbook= ""

function schoolFilter(school) {
    school_filter = "&school__iexact=" + school;
    loadSpells(school_filter);
}

function choose_spellbook(spellbook_id){
    current_spellbook = spellbook_id
    loadSpells(school_filter)
    return current_spellbook
}

loadSpells()

function loadSpells(school_filter) {
    
    cantrips_api =
        "https://api.open5e.com/spells/?level_int=0&limit=200" + school_filter;
    console.log(cantrips_api);
    response_cantrips = fetch(cantrips_api)
        .then(function (response_cantrips) {
            return response_cantrips.json();
        })
        .then(function (data) {
            var list_spells_cantrips = document.getElementById(`cantrips`);
            list_spells_cantrips.innerHTML = "";
            for (i = 0; i < data["results"].length; i++) {
                list_spells_cantrips.innerHTML += `<tr data-bs-toggle="collapse" data-bs-target="#cantrip-desc-${i}" id="cantrip-${i}">
                <th>${data["results"][i]["name"]}</th>
                <td>${data["results"][i]["casting_time"]}</td>
                <td>${data["results"][i]["school"]}</td>
                <td>${data["results"][i]["range"]}</td>
                <td>${data["results"][i]["duration"]}</td>
                <td>${data["results"][i]["dnd_class"]}</td>
                <td></td>
                </tr>
                <tr class="collapse accordion-collapse" data-bs-parent=".table" id="cantrip-desc-${i}">
                <td colspan="6">
                <div class="d-flex gap-5">
                <p>Components = ${data["results"][i]["components"]}</p>
                <p>Ritual = ${data["results"][i]["ritual"]}</p>
                <p>Concentration = ${data["results"][i]["concentration"]}</p>
                </div>
                <hr>
                ${data["results"][i]["desc"]}
                <br>
                ${data["results"][i]["higher_level"]}
                </td>
                
                <td>
                <form action="/spell/link" method="post" class="container">
                <div>
                <input type="hidden" name="spell_name" value="${data['results'][i]['name']}">
                <input type="hidden" name="desc" value="${data['results'][i]['desc']}">
                <input type="hidden" name="higher_level" value="${data['results'][i]['higher_level']}">
                <input type="hidden" name="range" value="${data['results'][i]['range']}">
                <input type="hidden" name="components" value="${data['results'][i]['components']}">
                <input type="hidden" name="material" value="${data['results'][i]['material']}">
                <input type="hidden" name="ritual" value="${data['results'][i]['ritual']}">
                <input type="hidden" name="concentration" value="${data['results'][i]['concentration']}">
                <input type="hidden" name="casting_time" value="${data['results'][i]['casting_time']}">
                <input type="hidden" name="duration" value="${data['results'][i]['duration']}">
                <input type="hidden" name="level_int" value="${data['results'][i]['level_int']}">
                <input type="hidden" name="level" value="${data['results'][i]['level']}">
                <input type="hidden" name="school" value="${data['results'][i]['school']}">
                <input type="hidden" name="spellbook_id" value="${current_spellbook}">
                </div>
                <button type="submit" class="btn btn-dark mt-2">Add to Spellbook</button>
                </form>
                </td>
                </tr>
            `;
            }
        })
        .catch(function (err) {
            console.log("Error - There is a problem", err);
        });

    level_one_api =
        "https://api.open5e.com/spells/?level_int=1&limit=200" + school_filter;
    console.log(level_one_api);
    response_level_one = fetch(level_one_api)
        .then(function (response_level_one) {
            return response_level_one.json();
        })
        .then(function (data) {
            var list_spells_first_level = document.getElementById(`level_ones`);
            list_spells_first_level.innerHTML = "";
            for (i = 0; i < data["results"].length; i++) {
                list_spells_first_level.innerHTML += `
            <tr data-bs-toggle="collapse" data-bs-target="#level1-desc-${i}" id="level1-${i}">
            <th>${data["results"][i]["name"]}</th>
            <td>${data["results"][i]["casting_time"]}</td>
            <td>${data["results"][i]["school"]}</td>
            <td>${data["results"][i]["range"]}</td>
            <td>${data["results"][i]["duration"]}</td>
            <td>${data["results"][i]["dnd_class"]}</td>
            <td></td>
            </tr>
            <tr class="collapse accordion-collapse" data-bs-parent=".table" id="level1-desc-${i}">
            <td colspan="6">
            <div class="d-flex gap-5">
            <p>Components = ${data["results"][i]["components"]}</p>
            <p>Ritual = ${data["results"][i]["ritual"]}</p>
            <p>Concentration = ${data["results"][i]["concentration"]}</p>
            </div>
            <hr>
                ${data["results"][i]["desc"]}
                <br>
                ${data["results"][i]["higher_level"]}
                </td>
                
                <td>
                <form action="/spell/link" method="post" class="container">
                <div>
                <input type="hidden" name="spell_name" value="${data['results'][i]['name']}">
                <input type="hidden" name="desc" value="${data['results'][i]['desc']}">
                <input type="hidden" name="higher_level" value="${data['results'][i]['higher_level']}">
                <input type="hidden" name="range" value="${data['results'][i]['range']}">
                <input type="hidden" name="components" value="${data['results'][i]['components']}">
                <input type="hidden" name="material" value="${data['results'][i]['material']}">
                <input type="hidden" name="ritual" value="${data['results'][i]['ritual']}">
                <input type="hidden" name="concentration" value="${data['results'][i]['concentration']}">
                <input type="hidden" name="casting_time" value="${data['results'][i]['casting_time']}">
                <input type="hidden" name="duration" value="${data['results'][i]['duration']}">
                <input type="hidden" name="level_int" value="${data['results'][i]['level_int']}">
                <input type="hidden" name="level" value="${data['results'][i]['level']}">
                <input type="hidden" name="school" value="${data['results'][i]['school']}">
                <input type="hidden" name="spellbook_id" value="${current_spellbook}">
                </div>
                <button type="submit" class="btn btn-dark mt-2">Add to Spellbook</button>
                </form>
                </td>
                </tr>
            `;
            }
        })
        .catch(function (err) {
            console.log("Error - There is a problem", err);
        });

    level_two_api =
        "https://api.open5e.com/spells/?level_int=2&limit=200" + school_filter;
    console.log(level_two_api);
    response_level_two = fetch(level_two_api)
        .then(function (response_level_two) {
            return response_level_two.json();
        })
        .then(function (data) {
            var list_spells_second_level =
                document.getElementById(`level_twos`);
            list_spells_second_level.innerHTML = "";
            for (i = 0; i < data["results"].length; i++) {
                list_spells_second_level.innerHTML += `
            <tr data-bs-toggle="collapse" data-bs-target="#level2-desc-${i}" id="level2-${i}">
            <th>${data["results"][i]["name"]}</th>
            <td>${data["results"][i]["casting_time"]}</td>
            <td>${data["results"][i]["school"]}</td>
            <td>${data["results"][i]["range"]}</td>
            <td>${data["results"][i]["duration"]}</td>
            <td>${data["results"][i]["dnd_class"]}</td>
            <td></td>
            </tr>
            <tr class="collapse accordion-collapse" data-bs-parent=".table" id="level2-desc-${i}">
            <td colspan="6">
            <div class="d-flex gap-5">
            <p>Components = ${data["results"][i]["components"]}</p>
            <p>Ritual = ${data["results"][i]["ritual"]}</p>
            <p>Concentration = ${data["results"][i]["concentration"]}</p>
            </div>
            <hr>
                ${data["results"][i]["desc"]}
                <br>
                ${data["results"][i]["higher_level"]}
                </td>
                
                <td>
                <form action="/spell/link" method="post" class="container">
                <div>
                <input type="hidden" name="spell_name" value="${data['results'][i]['name']}">
                <input type="hidden" name="desc" value="${data['results'][i]['desc']}">
                <input type="hidden" name="higher_level" value="${data['results'][i]['higher_level']}">
                <input type="hidden" name="range" value="${data['results'][i]['range']}">
                <input type="hidden" name="components" value="${data['results'][i]['components']}">
                <input type="hidden" name="material" value="${data['results'][i]['material']}">
                <input type="hidden" name="ritual" value="${data['results'][i]['ritual']}">
                <input type="hidden" name="concentration" value="${data['results'][i]['concentration']}">
                <input type="hidden" name="casting_time" value="${data['results'][i]['casting_time']}">
                <input type="hidden" name="duration" value="${data['results'][i]['duration']}">
                <input type="hidden" name="level_int" value="${data['results'][i]['level_int']}">
                <input type="hidden" name="level" value="${data['results'][i]['level']}">
                <input type="hidden" name="school" value="${data['results'][i]['school']}">
                <input type="hidden" name="spellbook_id" value="${current_spellbook}">
                </div>
                <button type="submit" class="btn btn-dark mt-2">Add to Spellbook</button>
                </form>
                </td>
                </tr>
            `;
            }
        })
        .catch(function (err) {
            console.log("Error - There is a problem", err);
        });

    level_three_api =
        "https://api.open5e.com/spells/?level_int=3&limit=200" + school_filter;
    console.log(level_three_api);
    response_level_three = fetch(level_three_api)
        .then(function (response_level_three) {
            return response_level_three.json();
        })
        .then(function (data) {
            var list_spells_third_level =
                document.getElementById(`level_threes`);
            list_spells_third_level.innerHTML = "";
            for (i = 0; i < data["results"].length; i++) {
                list_spells_third_level.innerHTML += `
            <tr data-bs-toggle="collapse" data-bs-target="#level3-desc-${i}" id="level3-${i}">
            <th>${data["results"][i]["name"]}</th>
            <td>${data["results"][i]["casting_time"]}</td>
            <td>${data["results"][i]["school"]}</td>
            <td>${data["results"][i]["range"]}</td>
            <td>${data["results"][i]["duration"]}</td>
            <td>${data["results"][i]["dnd_class"]}</td>
            <td></td>
            </tr>
            <tr class="collapse accordion-collapse" data-bs-parent=".table" id="level3-desc-${i}">
            <td colspan="6">
            <div class="d-flex gap-5">
            <p>Components = ${data["results"][i]["components"]}</p>
            <p>Ritual = ${data["results"][i]["ritual"]}</p>
            <p>Concentration = ${data["results"][i]["concentration"]}</p>
            </div>
            <hr>
                ${data["results"][i]["desc"]}
                <br>
                ${data["results"][i]["higher_level"]}
                </td>
                
                <td>
                <form action="/spell/link" method="post" class="container">
                <div>
                <input type="hidden" name="spell_name" value="${data['results'][i]['name']}">
                <input type="hidden" name="desc" value="${data['results'][i]['desc']}">
                <input type="hidden" name="higher_level" value="${data['results'][i]['higher_level']}">
                <input type="hidden" name="range" value="${data['results'][i]['range']}">
                <input type="hidden" name="components" value="${data['results'][i]['components']}">
                <input type="hidden" name="material" value="${data['results'][i]['material']}">
                <input type="hidden" name="ritual" value="${data['results'][i]['ritual']}">
                <input type="hidden" name="concentration" value="${data['results'][i]['concentration']}">
                <input type="hidden" name="casting_time" value="${data['results'][i]['casting_time']}">
                <input type="hidden" name="duration" value="${data['results'][i]['duration']}">
                <input type="hidden" name="level_int" value="${data['results'][i]['level_int']}">
                <input type="hidden" name="level" value="${data['results'][i]['level']}">
                <input type="hidden" name="school" value="${data['results'][i]['school']}">
                <input type="hidden" name="spellbook_id" value="${current_spellbook}">
                </div>
                <button type="submit" class="btn btn-dark mt-2">Add to Spellbook</button>
                </form>
                </td>
                </tr>
            `;
            }
        })
        .catch(function (err) {
            console.log("Error - There is a problem", err);
        });

    level_four_api =
        "https://api.open5e.com/spells/?level_int=4&limit=200" + school_filter;
    console.log(level_four_api);
    response_level_four = fetch(level_four_api)
        .then(function (response_level_four) {
            return response_level_four.json();
        })
        .then(function (data) {
            var list_spells_fourth_level =
                document.getElementById(`level_fours`);
            list_spells_fourth_level.innerHTML = "";
            for (i = 0; i < data["results"].length; i++) {
                list_spells_fourth_level.innerHTML += `
            <tr data-bs-toggle="collapse" data-bs-target="#level4-desc-${i}" id="level4-${i}">
            <th>${data["results"][i]["name"]}</th>
            <td>${data["results"][i]["casting_time"]}</td>
            <td>${data["results"][i]["school"]}</td>
            <td>${data["results"][i]["range"]}</td>
            <td>${data["results"][i]["duration"]}</td>
            <td>${data["results"][i]["dnd_class"]}</td>
            <td></td>
            </tr>
            <tr class="collapse accordion-collapse" data-bs-parent=".table" id="level4-desc-${i}">
            <td colspan="6">
            <div class="d-flex gap-5">
            <p>Components = ${data["results"][i]["components"]}</p>
            <p>Ritual = ${data["results"][i]["ritual"]}</p>
            <p>Concentration = ${data["results"][i]["concentration"]}</p>
            </div>
            <hr>
            ${data["results"][i]["desc"]}
            <br>
            ${data["results"][i]["higher_level"]}
            </td>
            
            <td>
            <form action="/spell/link" method="post" class="container">
            <div>
            <input type="hidden" name="spell_name" value="${data['results'][i]['name']}">
            <input type="hidden" name="desc" value="${data['results'][i]['desc']}">
            <input type="hidden" name="higher_level" value="${data['results'][i]['higher_level']}">
            <input type="hidden" name="range" value="${data['results'][i]['range']}">
            <input type="hidden" name="components" value="${data['results'][i]['components']}">
            <input type="hidden" name="material" value="${data['results'][i]['material']}">
            <input type="hidden" name="ritual" value="${data['results'][i]['ritual']}">
            <input type="hidden" name="concentration" value="${data['results'][i]['concentration']}">
            <input type="hidden" name="casting_time" value="${data['results'][i]['casting_time']}">
            <input type="hidden" name="duration" value="${data['results'][i]['duration']}">
            <input type="hidden" name="level_int" value="${data['results'][i]['level_int']}">
            <input type="hidden" name="level" value="${data['results'][i]['level']}">
            <input type="hidden" name="school" value="${data['results'][i]['school']}">
            <input type="hidden" name="spellbook_id" value="${current_spellbook}">
            </div>
            <button type="submit" class="btn btn-dark mt-2">Add to Spellbook</button>
            </form>
            </td>
            </tr>
        `;
            }
        })
        .catch(function (err) {
            console.log("Error - There is a problem", err);
        });

    level_five_api =
        "https://api.open5e.com/spells/?level_int=5&limit=200" + school_filter;
    console.log(level_five_api);
    response_level_five = fetch(level_five_api)
        .then(function (response_level_five) {
            return response_level_five.json();
        })
        .then(function (data) {
            var list_spells_fifth_level =
                document.getElementById(`level_fives`);
            list_spells_fifth_level.innerHTML = "";
            for (i = 0; i < data["results"].length; i++) {
                list_spells_fifth_level.innerHTML += `
            <tr data-bs-toggle="collapse" data-bs-target="#level5-desc-${i}" id="level5-${i}">
            <th>${data["results"][i]["name"]}</th>
            <td>${data["results"][i]["casting_time"]}</td>
            <td>${data["results"][i]["school"]}</td>
            <td>${data["results"][i]["range"]}</td>
            <td>${data["results"][i]["duration"]}</td>
            <td>${data["results"][i]["dnd_class"]}</td>
            <td></td>
            </tr>
            <tr class="collapse accordion-collapse" data-bs-parent=".table" id="level5-desc-${i}">
            <td colspan="6">
            <div class="d-flex gap-5">
            <p>Components = ${data["results"][i]["components"]}</p>
            <p>Ritual = ${data["results"][i]["ritual"]}</p>
            <p>Concentration = ${data["results"][i]["concentration"]}</p>
            </div>
            <hr>
            ${data["results"][i]["desc"]}
            <br>
            ${data["results"][i]["higher_level"]}
            </td>
            
            <td>
            <form action="/spell/link" method="post" class="container">
            <div>
            <input type="hidden" name="spell_name" value="${data['results'][i]['name']}">
            <input type="hidden" name="desc" value="${data['results'][i]['desc']}">
            <input type="hidden" name="higher_level" value="${data['results'][i]['higher_level']}">
            <input type="hidden" name="range" value="${data['results'][i]['range']}">
            <input type="hidden" name="components" value="${data['results'][i]['components']}">
            <input type="hidden" name="material" value="${data['results'][i]['material']}">
            <input type="hidden" name="ritual" value="${data['results'][i]['ritual']}">
            <input type="hidden" name="concentration" value="${data['results'][i]['concentration']}">
            <input type="hidden" name="casting_time" value="${data['results'][i]['casting_time']}">
            <input type="hidden" name="duration" value="${data['results'][i]['duration']}">
            <input type="hidden" name="level_int" value="${data['results'][i]['level_int']}">
            <input type="hidden" name="level" value="${data['results'][i]['level']}">
            <input type="hidden" name="school" value="${data['results'][i]['school']}">
            <input type="hidden" name="spellbook_id" value="${current_spellbook}">
            </div>
            <button type="submit" class="btn btn-dark mt-2">Add to Spellbook</button>
            </form>
            </td>
            </tr>
        `;
            }
        })
        .catch(function (err) {
            console.log("Error - There is a problem", err);
        });

    level_six_api =
        "https://api.open5e.com/spells/?level_int=6&limit=200" + school_filter;
    console.log(level_six_api);
    response_level_six = fetch(level_six_api)
        .then(function (response_level_six) {
            return response_level_six.json();
        })
        .then(function (data) {
            var list_spells_sixth_level =
                document.getElementById(`level_sixs`);
            list_spells_sixth_level.innerHTML = "";
            for (i = 0; i < data["results"].length; i++) {
                list_spells_sixth_level.innerHTML += `
            <tr data-bs-toggle="collapse" data-bs-target="#level6-desc-${i}" id="level6-${i}">
            <th>${data["results"][i]["name"]}</th>
            <td>${data["results"][i]["casting_time"]}</td>
            <td>${data["results"][i]["school"]}</td>
            <td>${data["results"][i]["range"]}</td>
            <td>${data["results"][i]["duration"]}</td>
            <td>${data["results"][i]["dnd_class"]}</td>
            <td></td>
            </tr>
            <tr class="collapse accordion-collapse" data-bs-parent=".table" id="level6-desc-${i}">
            <td colspan="6">
            <div class="d-flex gap-5">
            <p>Components = ${data["results"][i]["components"]}</p>
            <p>Ritual = ${data["results"][i]["ritual"]}</p>
            <p>Concentration = ${data["results"][i]["concentration"]}</p>
            </div>
            <hr>
            ${data["results"][i]["desc"]}
            <br>
            ${data["results"][i]["higher_level"]}
            </td>
            
            <td>
            <form action="/spell/link" method="post" class="container">
            <div>
            <input type="hidden" name="spell_name" value="${data['results'][i]['name']}">
            <input type="hidden" name="desc" value="${data['results'][i]['desc']}">
            <input type="hidden" name="higher_level" value="${data['results'][i]['higher_level']}">
            <input type="hidden" name="range" value="${data['results'][i]['range']}">
            <input type="hidden" name="components" value="${data['results'][i]['components']}">
            <input type="hidden" name="material" value="${data['results'][i]['material']}">
            <input type="hidden" name="ritual" value="${data['results'][i]['ritual']}">
            <input type="hidden" name="concentration" value="${data['results'][i]['concentration']}">
            <input type="hidden" name="casting_time" value="${data['results'][i]['casting_time']}">
            <input type="hidden" name="duration" value="${data['results'][i]['duration']}">
            <input type="hidden" name="level_int" value="${data['results'][i]['level_int']}">
            <input type="hidden" name="level" value="${data['results'][i]['level']}">
            <input type="hidden" name="school" value="${data['results'][i]['school']}">
            <input type="hidden" name="spellbook_id" value="${current_spellbook}">
            </div>
            <button type="submit" class="btn btn-dark mt-2">Add to Spellbook</button>
            </form>
            </td>
            </tr>
        `;
            }
        })
        .catch(function (err) {
            console.log("Error - There is a problem", err);
        });

    level_seven_api =
        "https://api.open5e.com/spells/?level_int=7&limit=200" + school_filter;
    console.log(level_seven_api);
    response_level_seven = fetch(level_seven_api)
        .then(function (response_level_seven) {
            return response_level_seven.json();
        })
        .then(function (data) {
            var list_spells_seventh_level =
                document.getElementById(`level_sevens`);
            list_spells_seventh_level.innerHTML = "";
            for (i = 0; i < data["results"].length; i++) {
                list_spells_seventh_level.innerHTML += `
            <tr data-bs-toggle="collapse" data-bs-target="#level7-desc-${i}" id="level7-${i}">
            <th>${data["results"][i]["name"]}</th>
            <td>${data["results"][i]["casting_time"]}</td>
            <td>${data["results"][i]["school"]}</td>
            <td>${data["results"][i]["range"]}</td>
            <td>${data["results"][i]["duration"]}</td>
            <td>${data["results"][i]["dnd_class"]}</td>
            <td></td>
            </tr>
            <tr class="collapse accordion-collapse" data-bs-parent=".table" id="level7-desc-${i}">
            <td colspan="6">
            <div class="d-flex gap-5">
            <p>Components = ${data["results"][i]["components"]}</p>
            <p>Ritual = ${data["results"][i]["ritual"]}</p>
            <p>Concentration = ${data["results"][i]["concentration"]}</p>
            </div>
            <hr>
            ${data["results"][i]["desc"]}
            <br>
            ${data["results"][i]["higher_level"]}
            </td>
            
            <td>
            <form action="/spell/link" method="post" class="container">
            <div>
            <input type="hidden" name="spell_name" value="${data['results'][i]['name']}">
            <input type="hidden" name="desc" value="${data['results'][i]['desc']}">
            <input type="hidden" name="higher_level" value="${data['results'][i]['higher_level']}">
            <input type="hidden" name="range" value="${data['results'][i]['range']}">
            <input type="hidden" name="components" value="${data['results'][i]['components']}">
            <input type="hidden" name="material" value="${data['results'][i]['material']}">
            <input type="hidden" name="ritual" value="${data['results'][i]['ritual']}">
            <input type="hidden" name="concentration" value="${data['results'][i]['concentration']}">
            <input type="hidden" name="casting_time" value="${data['results'][i]['casting_time']}">
            <input type="hidden" name="duration" value="${data['results'][i]['duration']}">
            <input type="hidden" name="level_int" value="${data['results'][i]['level_int']}">
            <input type="hidden" name="level" value="${data['results'][i]['level']}">
            <input type="hidden" name="school" value="${data['results'][i]['school']}">
            <input type="hidden" name="spellbook_id" value="${current_spellbook}">
            </div>
            <button type="submit" class="btn btn-dark mt-2">Add to Spellbook</button>
            </form>
            </td>
            </tr>
        `;
            }
        })
        .catch(function (err) {
            console.log("Error - There is a problem", err);
        });

    level_eight_api =
        "https://api.open5e.com/spells/?level_int=8&limit=200" + school_filter;
    console.log(level_eight_api);
    response_level_eight = fetch(level_eight_api)
        .then(function (response_level_eight) {
            return response_level_eight.json();
        })
        .then(function (data) {
            var list_spells_eighth_level =
                document.getElementById(`level_eights`);
            list_spells_eighth_level.innerHTML = "";
            for (i = 0; i < data["results"].length; i++) {
                list_spells_eighth_level.innerHTML += `
            <tr data-bs-toggle="collapse" data-bs-target="#level8-desc-${i}" id="level8-${i}">
            <th>${data["results"][i]["name"]}</th>
            <td>${data["results"][i]["casting_time"]}</td>
            <td>${data["results"][i]["school"]}</td>
            <td>${data["results"][i]["range"]}</td>
            <td>${data["results"][i]["duration"]}</td>
            <td>${data["results"][i]["dnd_class"]}</td>
            <td></td>
            </tr>
            <tr class="collapse accordion-collapse" data-bs-parent=".table" id="level8-desc-${i}">
            <td colspan="6">
            <div class="d-flex gap-5">
            <p>Components = ${data["results"][i]["components"]}</p>
            <p>Ritual = ${data["results"][i]["ritual"]}</p>
            <p>Concentration = ${data["results"][i]["concentration"]}</p>
            </div>
            <hr>
            ${data["results"][i]["desc"]}
            <br>
            ${data["results"][i]["higher_level"]}
            </td>
            
            <td>
            <form action="/spell/link" method="post" class="container">
            <div>
            <input type="hidden" name="spell_name" value="${data['results'][i]['name']}">
            <input type="hidden" name="desc" value="${data['results'][i]['desc']}">
            <input type="hidden" name="higher_level" value="${data['results'][i]['higher_level']}">
            <input type="hidden" name="range" value="${data['results'][i]['range']}">
            <input type="hidden" name="components" value="${data['results'][i]['components']}">
            <input type="hidden" name="material" value="${data['results'][i]['material']}">
            <input type="hidden" name="ritual" value="${data['results'][i]['ritual']}">
            <input type="hidden" name="concentration" value="${data['results'][i]['concentration']}">
            <input type="hidden" name="casting_time" value="${data['results'][i]['casting_time']}">
            <input type="hidden" name="duration" value="${data['results'][i]['duration']}">
            <input type="hidden" name="level_int" value="${data['results'][i]['level_int']}">
            <input type="hidden" name="level" value="${data['results'][i]['level']}">
            <input type="hidden" name="school" value="${data['results'][i]['school']}">
            <input type="hidden" name="spellbook_id" value="${current_spellbook}">
            </div>
            <button type="submit" class="btn btn-dark mt-2">Add to Spellbook</button>
            </form>
            </td>
            </tr>
        `;
            }
        })
        .catch(function (err) {
            console.log("Error - There is a problem", err);
        });

        level_nine_api =
        "https://api.open5e.com/spells/?level_int=9&limit=200" + school_filter;
    console.log(level_nine_api);
    response_level_nine = fetch(level_nine_api)
        .then(function (response_level_nine) {
            return response_level_nine.json();
        })
        .then(function (data) {
            var list_spells_ninth_level =
                document.getElementById(`level_nines`);
            list_spells_ninth_level.innerHTML = "";
            for (i = 0; i < data["results"].length; i++) {
                list_spells_ninth_level.innerHTML += `
            <tr data-bs-toggle="collapse" data-bs-target="#level9-desc-${i}" id="level9-${i}">
            <th>${data["results"][i]["name"]}</th>
            <td>${data["results"][i]["casting_time"]}</td>
            <td>${data["results"][i]["school"]}</td>
            <td>${data["results"][i]["range"]}</td>
            <td>${data["results"][i]["duration"]}</td>
            <td>${data["results"][i]["dnd_class"]}</td>
            <td></td>
            </tr>
            <tr class="collapse accordion-collapse" data-bs-parent=".table" id="level9-desc-${i}">
            <td colspan="6">
            <div class="d-flex gap-5">
            <p>Components = ${data["results"][i]["components"]}</p>
            <p>Ritual = ${data["results"][i]["ritual"]}</p>
            <p>Concentration = ${data["results"][i]["concentration"]}</p>
            </div>
            <hr>
            ${data["results"][i]["desc"]}
            <br>
            ${data["results"][i]["higher_level"]}
            </td>
            
            <td>
            <form action="/spell/link" method="post" class="container">
            <div>
            <input type="hidden" name="spell_name" value="${data['results'][i]['name']}">
            <input type="hidden" name="desc" value="${data['results'][i]['desc']}">
            <input type="hidden" name="higher_level" value="${data['results'][i]['higher_level']}">
            <input type="hidden" name="range" value="${data['results'][i]['range']}">
            <input type="hidden" name="components" value="${data['results'][i]['components']}">
            <input type="hidden" name="material" value="${data['results'][i]['material']}">
            <input type="hidden" name="ritual" value="${data['results'][i]['ritual']}">
            <input type="hidden" name="concentration" value="${data['results'][i]['concentration']}">
            <input type="hidden" name="casting_time" value="${data['results'][i]['casting_time']}">
            <input type="hidden" name="duration" value="${data['results'][i]['duration']}">
            <input type="hidden" name="level_int" value="${data['results'][i]['level_int']}">
            <input type="hidden" name="level" value="${data['results'][i]['level']}">
            <input type="hidden" name="school" value="${data['results'][i]['school']}">
            <input type="hidden" name="spellbook_id" value="${current_spellbook}">
            </div>
            <button type="submit" class="btn btn-dark mt-2">Add to Spellbook</button>
            </form>
            </td>
            </tr>
        `;
            }
        })
        .catch(function (err) {
            console.log("Error - There is a problem", err);
        });
}