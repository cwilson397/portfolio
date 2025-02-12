// arrays.js

// Activity 1
const steps = ["one", "two", "three"];
function listTemplate(step) {
  return `
${step}
`;
}

const stepsHtml = steps.map(listTemplate);
document.querySelector("#myList").innerHTML = stepsHtml.join();

// Activity 2
const grades = ["A", "B", "A"];
function convertGradeToPoints(grade) {
  let points = 0;
  if  (grade === "A") {
    points = 4;
  } else if (grade === "B") {
    points = 3;
  }
  return points;
}

const gpaPoints = grades.map(convertGradeToPoints);

// Display GPA points in Activity 2
document.querySelector("#gpaPointsList").innerHTML = gpaPoints
  .map((point) => `<li>${point}</li>`)
  .join("");

// Activity 3
const pointsTotal = gpaPoints.reduce(function (total, item) {
  return total + item;
});
const gpa = pointsTotal / gpaPoints.length;

// Display GPA in Activity 3
document.querySelector("#gpaDisplay").textContent = `GPA: ${gpa.toFixed(2)}`;

// Activity 4
const words = ["watermelon", "peach", "apple", "tomato", "grape"];
const shortWords = words.filter(function (word) {
  return word.length < 6;
});

// Display short words in Activity 4
document.querySelector("#shortWordsList").innerHTML = shortWords
  .map((word) => `<li>${word}</li>`)
  .join("");

// Activity 5
const myArray = [12, 34, 21, 54];
const luckyNumber = 21;
let luckyIndex = myArray.indexOf(luckyNumber);

// Display lucky number index in Activity 5
document.querySelector("#luckyIndexDisplay").textContent = `Lucky Number Index: ${luckyIndex}`;
