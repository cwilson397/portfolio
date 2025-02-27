import { participantTemplate, successTemplate } from "./Templates.js";

document.addEventListener("DOMContentLoaded", () => {
    let participantCount = 1;
    const addButton = document.getElementById("add");
    const form = document.querySelector("form");
    const summary = document.getElementById("summary");

    addButton.addEventListener("click", () => {
        participantCount++;
        const newParticipant = participantTemplate(participantCount);
        addButton.insertAdjacentHTML("beforebegin", newParticipant);
    });

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
});
f