const front_text = document.getElementById("front_text")
const back_text = document.getElementById("back_text")

const prev_btn = document.getElementById("prev")
const next_btn = document.getElementById("next")
const shuffle_btn = document.getElementById("shuffle")

function update_card() {
  front_text.innerText = testables[index][0]
  back_text.innerText = testables[index][1]

  // console.log(String(index+1) + "/" + String(testables.length))
}

function shuffleArray(array) {
    for (let i = array.length - 1; i >= 1; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
}

// init 
let index = 0
if (testables.length === 0) {
  testables = [["no cards selected to display", "please select and submit topics from the sidebar on the left :D"]]
}
update_card()

// flip card on spacebar
const card_inner = document.getElementById("card_inner")
document.addEventListener("keydown", (event) => {
  if (event.key === " ") {
    event.preventDefault()
    card_inner.classList.toggle("flipped")
  }
})

// changing the word
// prev

function prev_card() {
  index -= 1
  if (index < 0) {
    index = testables.length - 1
  }
  update_card()
}

prev_btn.addEventListener("click", () => {
  prev_card()
})

document.addEventListener("keydown", (event) => {
  if (event.key === "ArrowLeft") {
    prev_card()
  }
});

// next

function next_card() {
  index += 1
  if (index >= testables.length) {
    index = 0
  }
  update_card()
}

next_btn.addEventListener("click", () => {
  next_card()
})

document.addEventListener("keydown", (event) => {
  if (event.key === "ArrowRight") {
    next_card()
  }
});


// shuffle
shuffle_btn.addEventListener("click", ()=> {
  testables = shuffleArray(testables)
  update_card()
})

// select all
const select_all_btn = document.getElementById("select_all")
let select = true;

function update_select_all_button_face() {
  const select_all_msg = "select all"
  const deselect_all_msg = "deselect all"
  
  if (select) {
    select_all_btn.textContent = select_all_msg
  } else {
    select_all_btn.textContent = deselect_all_msg
  }
}

document.querySelectorAll('.topic-checkbox').forEach(element => {
  element.addEventListener("change", () => {

    if (select) {
      select = false

    } else {
      let no_selected = 0
      document.querySelectorAll('.topic-checkbox').forEach(element => {
        if (element.checked === true) {no_selected += 1}
      });
      no_selected === 0 ? select = true : select = false
    }

    update_select_all_button_face()
  })
});

select_all_btn.addEventListener("click", () => {
  document.querySelectorAll('.topic-checkbox').forEach(element => {
    element.checked = select;
  });
  select = !select
  update_select_all_button_face()
})
