
/*fetch("characters.json")
*  .then(res => res.text())
*  .then(start);
*/

let classtables = JSON.parse('{"assassin": {"ability minimums": {"strength": 12, "dexterity": 12, "intelligence": 9}, "bonus xp minimums": {"strength": 15, "dexterity": 15, "intelligence": 15}}}')

let characterBeingCreated = new Object()

let choose_class = document.getElementById("choose-class")
console.log(choose_class)


function p(container, text) {
    let p = document.createElement("p")
    p.innerHTML = text
    container.appendChild(p)
}

function start() {
  for (const [klass, value] of Object.entries(classtables)) {
    p(choose_class, klass.capitalize())
    mins = value['ability minimums']
    text = klass + ". Min abilities: "
    for (const [ayy, lmao] of Object.entries(mins)) {
      text = text + ayy + ": " + lmao + ","
    }
    p(choose_class, text)

    mins = value['bonus xp minimums']
    text = klass + ". Min for bonus xp: "
    for (const [ayy, lmao] of Object.entries(mins)) {
      text = text + ayy + ": " + lmao + ","
    }
    p(choose_class, text)
  }
}

start()

// let b = document.getElementById("b-container");
// let q = document.createElement("p");
// q.innerHTML = propertiesToArray(classtables);
// b.appendChild(q);

function checkAbilityMinimums () {
  // todo this imp only considers min abilities going above or below a min requiremet for a klass
  // but what about "this value went up, klass K is as before, but klass Q is now available?"
  // and what about "class R avialable under permutation"? not that that's a hugel important use case
  // on input to ability score A of value N
  // for klass in classtables
  // if klass[ability minimums] contains A
  // updateDisplay(klass)
}

function checkBonusXPMinimums () {
  // similar to
}


// todo; consider that if you pick fighter, go thru the process, choose weapon profs, etc.
// then change and do thief
// then change back to fighter
// ideally, those same weapon profs you chose as fighter should still be selected
// this implies storing data about what choices you made while working to build char for K class
// even more ideally (don't have to support this), when u switch to thief, should choose as many profs for thief as possible which were ones chosen as fighter.


//    what I can send from server is the form with all subforms, such as picking class, sex, race, and so on.
//
//      to do validation, though, I'll want to probably send a fat JSON file with class_tables as in the python file of the same name
//      so I can do JS validation for things like "Oh they just swapped their 14 to a 15, Paladin is now unavailable but Monk is available" and so on
//      (with availability shown by adding/removing CSS classes)
//
//      I can even do things like "with ability scores as is, you can pick these 7 out of 10 classes;
//      and with the array you have, NO permutation will let you play the other 2 classes.
//      if you changed how you assigned your scores you could play THIS class; (this one is the key)"
//
//      in addition to "if you changed score assignment..."
//      I could also include racial changes.
//      "If you were an elf instead of a human you'd get the Mage bonus XP  without moving any scores (ie you'd go from 15 to 16)
//      If you permuted your scores like this AND  chose an elf you could get Fighter bonus XP..."
//      and so on.
//
//





function propertiesToArray(obj) {
  const isObject = val =>
    val && typeof val === 'object' && !Array.isArray(val);

  const addDelimiter = (a, b) =>
    a ? `${a}.${b}` : b;

  const paths = (obj = {}, head = '') => {
    return Object.entries(obj)
      .reduce((product, [key, value]) =>
        {
          let fullPath = addDelimiter(head, key)
          return isObject(value) ?
            product.concat(paths(value, fullPath))
          : product.concat(fullPath)
        }, []);
  }

  return paths(obj);
}
// https://d-toybox.com/studio/lib/input_event_viewer.html
// very helpful for input events
