document.querySelectorAll(".logout-btn")[0].addEventListener("click", logOut);
document
  .querySelectorAll(".my-resumes")[0]
  .addEventListener("click", mySummaries);
document
  .querySelectorAll(".my-business-btn")[0]
  .addEventListener("click", myBusiness);

const dateInput = document.getElementById("date-input");
arr = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "Backspace"];

dateInput.addEventListener("keydown", validateInput);

let profileCountry = document.querySelector(".profile-country");
let selectCountry = document.querySelector("#select-country");

selectCountry.addEventListener("change", chageCountry);

countries.forEach((element) => {
  selectCountry.insertAdjacentHTML(
    "beforeend",
    `<option value="${Object.keys(element)}">${Object.keys(element)}</option>`
  );
});

function loadImage(event) {
  var output = document.getElementById("preview");

  output.src = URL.createObjectURL(event.target.files[0]);
  output.onload = function () {
    URL.revokeObjectURL(output.src);
  };
}

async function fetchData() {
  const response = await fetch("http://127.0.0.1:8000/api/countries");

  countries = await response.json();

  console.log("Полученные данные:", data);
}

function inputProcessing(event, inputChar) {
  event.preventDefault();
  let inputValue = event.target.value + inputChar;
  const inputlength = inputValue.length;
  if (inputChar == "Backspace") {
    if (inputlength == 12) {
      inputValue = inputValue.substring(0, dateInput.value.length - 2);
    } else if (inputlength == 15) {
      inputValue = inputValue.substring(0, dateInput.value.length - 2);
    } else {
      inputValue = inputValue.substring(0, dateInput.value.length - 1);
    }
    dateInput.value = inputValue;
  }
  if (inputlength <= 10 && inputChar != "Backspace") {
    if (inputlength == 2) {
      inputValue += ".";
    } else if (inputlength == 5) {
      inputValue += ".";
    }
    dateInput.value = inputValue;
  }
}

function validateInput(event) {
  event.preventDefault();
  const inputChar = event.key;
  if (arr.includes(inputChar) == true) {
    inputProcessing(event, inputChar);
  }
}

function chageCountry(event) {
  try {
    document.querySelector("#select-region").remove();
  } catch {}
  selectElement = event.target.options[event.target.selectedIndex];
  profileCountry.insertAdjacentHTML(
    "beforeend",
    `<select name="region" id="select-region">
          <option value="none">-</option>
        </select>
      `
  );

  countries[selectElement.index - 1][selectElement.value].forEach((element) => {
    document
      .querySelector("#select-region")
      .insertAdjacentHTML(
        "beforeend",
        `<option value="${Object.keys(element)}">${Object.keys(
          element
        )}</option>`
      );
  });
  document
    .querySelector("#select-region")
    .addEventListener("change", changeRegion);
}

function changeRegion(event) {
  console.log(selectElement.value);
}

function logOut() {
  var confirmLogout = confirm("Are you sure you want to log out?");
  if (confirmLogout) {
    window.location.href = "/logout";
  }
}

function mySummaries() {
  window.location.href = "/my_summaries";
}

function myBusiness() {
  window.location.href = "/my_company";
}

fetchData();
