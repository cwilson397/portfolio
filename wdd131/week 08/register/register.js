document.addEventListener("DOMContentLoaded", () => {
    let participantCount = 1;
    const addButton = document.getElementById("add");
    const participantsFieldset = document.querySelector(".participants");
    const form = document.querySelector("form");
    const summary = document.getElementById("summary");
    const submitButton = document.getElementById("submitButton");

    addButton.addEventListener("click", () => {
        participantCount++;
        const newParticipant = participantTemplate(participantCount);
        addButton.insertAdjacentHTML("beforebegin", newParticipant);
    });

    function participantTemplate(count) {
        return `<section class="participant${count}">
            <p>Participant ${count}</p>
            <div class="item">
              <label for="fname${count}"> First Name<span>*</span></label>
              <input id="fname${count}" type="text" name="fname" required=""/>
            </div>
            <div class="item activities">
              <label for="activity${count}">Activity #<span>*</span></label>
              <input id="activity${count}" type="text" name="activity"/>
            </div>
            <div class="item">
              <label for="fee${count}">Fee ($)<span>*</span></label>
              <input id="fee${count}" type="number" name="fee"/>
            </div>
            <div class="item">
              <label for="date${count}">Desired Date <span>*</span></label>
              <input id="date${count}" type="date" name="date"/>
            </div>
            <div class="item">
              <p>Grade</p>
              <select>
                <option selected="" value="" disabled=""></option>
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
          </section>`;
    }

    form.addEventListener("submit", (event) => {
        event.preventDefault();
        const totalFee = totalFees();
        const adultName = document.getElementById("adult_name").value;

        form.style.display = "none";
        summary.innerHTML = successTemplate({ name: adultName, count: participantCount, total: totalFee });
    });

    function totalFees() {
        let feeElements = document.querySelectorAll("[id^=fee]");
        feeElements = [...feeElements];
        return feeElements.reduce((sum, input) => sum + (parseFloat(input.value) || 0), 0);
    }

    function successTemplate(info) {
        return `<p>Thank you, ${info.name}, for registering. You have registered ${info.count} participants and owe $${info.total} in fees.</p>`;
    }
});
