let participantCount = 1;

//Function for participant template
function participantTemplate(count) {
  return `
    <section class="participant${count}">
      <p>Participant ${count}</p>
      <div class="item">
        <label for="fname${count}">First Name<span>*</span></label>
        <input id="fname${count}" type="text" name="fname${count}" required />
      </div>
      <div class="item activities">
        <label for="activity${count}">Activity #<span>*</span></label>
        <input id="activity${count}" type="text" name="activity${count}" />
      </div>
      <div class="item">
        <label for="fee${count}">Fee ($)<span>*</span></label>
        <input id="fee${count}" type="number" name="fee${count}" />
      </div>
      <div class="item">
        <label for="date${count}">Desired Date <span>*</span></label>
        <input id="date${count}" type="date" name="date${count}" />
      </div>
      <div class="item">
        <p>Grade</p>
        <select>
          <option selected value="" disabled selected></option>
          <option value="1">1st</option>
          <option value="2">2nd</option>
          <option value="3">3rd</option>
          <option value="4">4th</option>
          <option value="5">5th</option>
          <option value="6">6th</option>
          <option value="7">7th</option>
          <option value="8">8th</option>
          <option value="9">9th</option>
          <option value="10">10th</option>
          <option value="11">11th</option>
          <option value="12">12th</option>
        </select>
      </div>
    </section>
  `;
}


document.querySelector("#add").addEventListener("click", () => {
  participantCount++;
  const newSection = participantTemplate(participantCount);
  const addBtn = document.querySelector("#add");
  addBtn.insertAdjacentHTML("beforebegin", newSection);
  const fieldset = document.querySelector(".participants");
  fieldset.classList.add("multiple-participants");
});


function totalFees() {
  let feeElements = document.querySelectorAll("[id^=fee]");
  console.log(feeElements);
  feeElements = [...feeElements];
  return feeElements.reduce((sum, el) => sum + Number(el.value || 0), 0);
}


document.querySelector("form").addEventListener("submit", submitForm);

function submitForm(event) {
  event.preventDefault();

  const adultName = document.querySelector("#adult_name").value;
  const total = totalFees();

  document.querySelector("form").style.display = "none";

  document.querySelector("#summary").innerHTML = successTemplate({
    name: adultName,
    count: participantCount,
    fees: total,
  });
}

function successTemplate(info) {
  return `
    <h2>Thank You!</h2>
    <p>Thank you <strong>${info.name}</strong> for registering.</p>
    <p>You have registered <strong>${info.count}</strong> participant(s) 
        and owe <strong>$${info.fees}</strong> in Fees.</p>
  `;
}
