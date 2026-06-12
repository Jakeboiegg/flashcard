console.log(testables)

const card = document.getElementById("card")
const card_text = document.getElementById("card_text")

const prev_btn = document.getElementById("prev")
const next_btn = document.getElementById("next")

function update_card() {
  card_text.textContent = testables[index][flipped]
}

// init 
let index = 0
let flipped = 0
update_card()

// changing the word
prev_btn.addEventListener("click", () => {
  index -= 1
  if (index < 0) {
    index = testables.length - 1
  }
  update_card()
})

next_btn.addEventListener("click", () => {
  index += 1
  if (index >= testables.length) {
    index = 0
  }
  update_card()
})

// flipping the cards
card.addEventListener("click", () => {
  flipped == 0 ? flipped = 1 : flipped = 0 
  update_card()
})
