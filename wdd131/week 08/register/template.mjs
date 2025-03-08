export function participantTemplate(count) {
  return `<section class="participant" id="participant${count}">
      <p>Participant ${count}</p>
      <label for="fname${count}">First Name<span>*</span></label>
      <input id="fname${count}" type="text" name="fname${count}" required>
      <label for="activity${count}">Activity #<span>*</span></label>
      <input id="activity${count}" type="text" name="activity${count}">
      <label for="fee${count}">Fee ($)<span>*</span></label>
      <input id="fee${count}" type="number" name="fee${count}">
      <label for="date${count}">Desired Date<span>*</span></label>
      <input id="date${count}" type="date" name="date${count}">
  </section>`;
}

export function successTemplate(info) {
  return `<p>Thank you, ${info.name}, for registering. You have registered ${info.count} participants and owe $${info.total} in fees.</p>`;
}
