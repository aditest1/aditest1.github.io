let qProgress = 0;
let questions = [];

// Fetch questions from the JSON file
async function getQuestions(chapter) {
  try {
    let response = await fetch(`c${chapter}.json`);
    
    if (!response.ok) {
      throw new Error(`Failed to fetch questions: ${response.statusText}`);
    }
    let data = await response.json();
    console.log(data)
    return data;
  } catch (error) {
    console.error("Error fetching questions:", error);
    return null;
  }
}

/**
 * Render the questions based on the selected filter.
 * @param {number} chapter
 * @param {string} filter
 */
async function render(chapter, filter) {
  let json = await getQuestions(chapter);
  if (!json || !json.questions) {
    alert("No questions found for the selected chapter.");
    return;
  }

  // Filter questions based on the selected type
  questions = json.questions.filter(q => q.type.includes(filter));
  if (questions.length === 0) {
    alert("No questions found for the selected type.");
    return;
  }

  let type = questions[0].type;
  let question = questions[0].question;
  let options = questions[0].options;
  let answers = questions[0].answer;
  renderQuestion(type, question, options, answers);
}

async function render_next(chapter) {
  qProgress += 1;
  if (qProgress >= questions.length) {
    alert("Congratulations! You have completed the chapter!");
    window.location.href = `index.html`;
    return;
  }

  document.getElementById("questionbox").remove();
  let type = questions[qProgress].type;
  let question = questions[qProgress].question;
  let options = questions[qProgress].options;
  let answers = questions[qProgress].answer;
  renderQuestion(type, question, options, answers);
}

function renderQuestion(type, question, options, answers) {
  switch (type) {
    case "mcq":
      renderMCQ(question, options, answers);
      break;
    case "scq":
      renderSCQ(question, options, answers);
      break;
    case "assertion":
      renderAssertionR(question, options, answers);
      break;
    default:
      console.error("Unknown question type:", type);
      alert("Unknown question type. Please check the data.");
  }
}

function renderMCQ(question, options, answers) {
  let mcq = document.createElement("div");
  mcq.id = "questionbox";
  mcq.innerHTML = `
    <p>${question}</p>
    <div class="flex flex-col gap-2">
      ${options.map(option => `
        <div class="flex gap-2">
          <input type="radio" name="options" value="${option}">
          <label>${option}</label>
        </div>
      `).join("")}
    </div>
    <button onclick="check_answer()" class="bg-blue-500 hover:bg-blue-700 font-bold py-2 px-5 rounded">Submit</button>
  `;
  document.getElementById('questionContainer').appendChild(mcq);
}


const containsAll = (arr1, arr2) => arr2.every(arr2Item => arr1.includes(arr2Item));
const sameMembers = (arr1, arr2) => containsAll(arr1, arr2) && containsAll(arr2, arr1);
function check_answer() {
  let correctAnswers = questions[qProgress].answer; // Assuming qProgress is correctly managed elsewhere
  let options = document.getElementsByName("options");
  let userAnswers = [];
  
  // Collect selected answers
  for (let option of options) {
    if (option.checked) {
      userAnswers.push(option.value);
    }
  }
  
  // Convert correctAnswers to an array if it's not already
  if (!Array.isArray(correctAnswers)) {
    correctAnswers = [correctAnswers];
  }
  
  // Check if userAnswers match correctAnswers
  if (arraysEqual(userAnswers, correctAnswers)) {
    alert("Correct!");
  } else {
    alert("Incorrect! The correct answer(s) is/are: " + correctAnswers.join(", "));
  }
  
  render_next(1); // Assuming render_next is defined elsewhere
}

// Function to compare arrays for equality
function arraysEqual(arr1, arr2) {
  if (arr1.length !== arr2.length) return false;
  for (let i = 0; i < arr1.length; i++) {
    if (arr1[i] !== arr2[i]) return false;
  }
  return true;
}
function renderSCQ(question, options, answers) {
  let scq = document.createElement("div");
  scq.id = "questionbox";
  scq.innerHTML = `
    <p>${question}</p>
    <div class="flex flex-col gap-2">
      ${options.map(option => `<div class="flex gap-2"><input type="radio" name="options" value="${option}"><label>${option}</label></div>`).join("")}
    </div>
    <button onclick="check_answer()" class="bg-blue-500 hover:bg-blue-700 font-bold py-2 px-5 rounded">Submit</button>
  `;
  document.getElementById('questionContainer').appendChild(scq);
}

function renderAssertionR(question, options, answers) {
  let assertionr = document.createElement("div");
  assertionr.id = "questionbox";
  assertionr.innerHTML = `
    <p>${question}</p>
    <div class="flex flex-col gap-2">
      ${options.map(option => `
        <div class="flex gap-2">
          <input type="radio" name="options" value="${option}">
          <label>${option}</label>
        </div>
      `).join("")}
    </div>
    <button onclick="check_answer()" class="bg-blue-500 hover:bg-blue-700 font-bold py-2 px-5 rounded">Submit</button>
  `;
  document.getElementById('questionContainer').appendChild(assertionr);
}

