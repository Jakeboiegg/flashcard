console.log(testables)

const card_text = document.getElementById("card_text")

const prev_btn = document.getElementById("prev")
const next_btn = document.getElementById("next")

let index = 0

function update_card() {
  card_text.textContent = testables[index][0]
}

update_card()

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
