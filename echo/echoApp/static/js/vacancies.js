document.querySelectorAll(".send-cv").forEach((element) => {
  element.addEventListener("click", showForm);
});

const selectCountry = document.querySelector('#select-country')

async function fetchData() {
  const response = await fetch("http://127.0.0.1:8000/api/countries");

  countries = await response.json();

  console.log("Полученные данные:", countries);

  countries['clean_data'].forEach((element) => {
    selectCountry.insertAdjacentHTML("beforeend",
      `<option class="country" value="${Object.keys(element)}">${Object.keys(element)}</option>`
    )
  })
}
fetchData();

function checkCountry (event) {
    try {
      document.querySelector('#select-region').remove()
    } catch (i) {}
    districtClass = document.querySelector('.district').style.display = 'none'
    selectedCountry = event.target.options[event.target.selectedIndex]
    regionClass = document.querySelector('.region')
    regionClass.insertAdjacentHTML("beforeend",
        `
      <select name="region" id="select-region">
        <option value="-">-</option>
      </select>
    `)
    regionClass.style.display = 'block'
    countries['clean_data'][selectedCountry.index - 1][selectedCountry.value].forEach(element =>{
      document.querySelector('#select-region').insertAdjacentHTML("beforeend", `
            <option value="${Object.keys(element)}">${Object.keys(element)}</option>
        `)
    })
    document.querySelector('#select-region').addEventListener("change", changeRegion)
}

selectCountry.addEventListener("change", checkCountry)

function changeRegion (event) {
  try {
      document.querySelector('#select-district').remove()
    } catch (i) {}
    selectedRegion = event.target.options[event.target.selectedIndex]
    districtClass = document.querySelector('.district')
    districtClass.insertAdjacentHTML("beforeend",
        `
      <select name="district" id="select-district">
        <option value="-">-</option>
      </select>
    `)
    districtClass.style.display = 'block'
    // console.log(countries['clean_data'][selectedCountry.index - 1][selectedCountry.value][selectedRegion.index - 1][selectedRegion.value])
      countries['clean_data'][selectedCountry.index - 1][selectedCountry.value][selectedRegion.index - 1][selectedRegion.value].forEach(element =>{
      document.querySelector('#select-district').insertAdjacentHTML("beforeend", `
            <option value="${element}">${element}</option>
        `)
    })
}

document
  .querySelector("#employment")
  .addEventListener("change", checkEmployment);

function checkEmployment(event) {
  if (event.target.value == "part-time") {
    document.querySelector(".podrabotka").style.display = "block";
  } else {
    document.querySelector(".podrabotka").style.display = "none";
  }
}

function showForm(event) {
  document.getElementById("myModal").style.display = "block";
}
