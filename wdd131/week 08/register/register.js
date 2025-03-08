import { participantTemplate, successTemplate } from "./template.mjs";

document.addEventListener("DOMContentLoaded", () => {
    let participantCount = 1;
    const addButton = document.getElementById("addParticipant");
    const form = document.getElementById("registrationForm");
    const summary = document.getElementById("summary");

    addButton.addEventListener("click", () => {
        participantCount++;
        const newParticipant = participantTemplate(participantCount);
        document.getElementById("participantList").insertAdjacentHTML("beforeend", newParticipant);
    });

    form.addEventListener("submit", (event) => {
        event.preventDefault();
        const totalFee = totalFees();
        const adultName = document.getElementById("adult_name").value;
        
        form.classList.add("hide");
        summary.classList.remove("hide");
        summary.innerHTML = successTemplate({ name: adultName, count: participantCount, total: totalFee });
    });

    function totalFees() {
        let feeElements = document.querySelectorAll("input[name^='fee']");
        feeElements = [...feeElements];
        return feeElements.reduce((sum, input) => sum + (parseFloat(input.value) || 0), 0);
    }
});