var incomeSlider = document.getElementById("income");
var incomeOutput = document.getElementById("incomeValue");
incomeOutput.innerHTML = incomeSlider.value;
incomeSlider.oninput = function () {
  incomeOutput.innerHTML = this.value;
};
const cities = {
  Belarus: {
    Minsk: [
      "Central District",
      "Savyetski District",
      "Pershamayski District",
      "Zavodski District",
      "Leninski District",
      "Partyzanski District",
    ],
    Brest: ["Brest District", "Kamianets District", "Luninets District"],
    Gomel: ["Gomel District", "Zhlobin District", "Mazyr District"],
    Mogilev: ["Mogilev District", "Bobruisk District", "Krichev District"],
    Vitebsk: ["Vitebsk District", "Orsha District", "Polotsk District"],
    Hrodna: ["Hrodna District", "Lida District", "Slonim District"],
  },
};
var experienceSlider = document.getElementById("experience");
var experienceOutput = document.getElementById("experienceValue");
experienceOutput.innerHTML = experienceSlider.value;
experienceSlider.oninput = function () {
  experienceOutput.innerHTML = this.value;
};

function showForm(event) {
  console.log(event.target.closest(".vacancy"));
  document.getElementById("myModal").style.display = "block";
}
allBtns = document.querySelectorAll(".send-cv");
allBtns.forEach((element) => {
  element.addEventListener("click", showForm);
});

regions = document.querySelectorAll(".region");

function checkRegion(event) {
  if (event.target.closest("li").textContent.trim() == "Вся Беларусь") {
    if (event.target.checked == true) {
      regions.forEach((element) => {
        element.checked = true;
      });
    } else if (event.target.checked == false) {
      regions.forEach((element) => {
        element.checked = false;
      });
    }
    if (event.target.checked == true) {
      result = true;
      regions.forEach((element) => {
        if (element.checked == false) {
          result = false;
        }
      });
    }
  }
  if (event.target.closest("li").textContent.trim() != "Вся Беларусь") {
    if (event.target.checked == false) {
      regions.forEach((element) => {
        if (element.closest("li").textContent.trim() == "Вся Беларусь") {
          console.log(element.closest("li").textContent.trim());
          element.checked = false;
        }
      });
    }
  }
  regions.forEach((element) => {
    if (element.closest("li").textContent.trim() == "Минск") {
      if (element.checked == true) {
        metro = document.querySelector(".metro").style.display = "block";
      } else {
        metro = document.querySelector(".metro").style.display = "none";
      }
    }
  });
}

regions.forEach((element) => {
  element.addEventListener("change", checkRegion);
});
