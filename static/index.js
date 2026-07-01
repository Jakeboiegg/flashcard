const front_text = document.getElementById("front_text")
const back_text = document.getElementById("back_text")

const prev_btn = document.getElementById("prev")
const next_btn = document.getElementById("next")
const shuffle_btn = document.getElementById("shuffle")

function update_card() {
  front_text.innerText = testables[index][0]
  back_text.innerText = testables[index][1]
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
let flipped = 0
update_card()

console.log(testables)

// changing the word
// prev
prev_btn.addEventListener("click", () => {
  index -= 1
  if (index < 0) {
    index = testables.length - 1
  }
  update_card()
})

// next
next_btn.addEventListener("click", () => {
  index += 1
  if (index >= testables.length) {
    index = 0
  }
  update_card()
})

// shuffle
shuffle_btn.addEventListener("click", ()=> {
  testables = shuffleArray(testables)
  console.log(testables)
  update_card()
})

