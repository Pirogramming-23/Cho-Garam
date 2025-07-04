let startTime = 0;
let elapsedTime = 0;
let timerInterval;
let isRunning = false;

const timeDisplay = document.getElementById("time");
const recordList = document.getElementById("recordList");

document.getElementById("start").addEventListener("click", () => {
    if (isRunning) return;
    isRunning = true;
    startTime = Date.now() - elapsedTime;
    timerInterval = setInterval(() => {
    elapsedTime = Date.now() - startTime;
    updateTimeDisplay(elapsedTime);
    }, 50);
});

document.getElementById("stop").addEventListener("click", () => {
  if (!isRunning) return;
  isRunning = false;
  clearInterval(timerInterval);
  addRecord(timeDisplay.textContent);
});

document.getElementById("reset").addEventListener("click", () => {
  clearInterval(timerInterval);
  startTime = 0;
  elapsedTime = 0;
  isRunning = false;
  updateTimeDisplay(0);
});

document.getElementById("checkAll").addEventListener("change", function () {
  const checkboxes = recordList.querySelectorAll("input[type='checkbox']");
  checkboxes.forEach(cb => cb.checked = this.checked);
});

document.getElementById("deleteSelected").addEventListener("click", () => {
  const checkedItems = recordList.querySelectorAll("input[type='checkbox']:checked");
  checkedItems.forEach(cb => cb.parentElement.remove());
});

function updateTimeDisplay(ms) {
  const totalSeconds = Math.floor(ms / 1000);
  const centiseconds = Math.floor((ms % 1000) / 10); // 1/100초 단위
  const formattedSeconds = String(totalSeconds).padStart(2, '0');
  const formattedCentis = String(centiseconds).padStart(2, '0');
  timeDisplay.textContent = `${formattedSeconds}:${formattedCentis}`;
}

function addRecord(time) {
  const li = document.createElement("li");
  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";
  li.appendChild(checkbox);
  li.appendChild(document.createTextNode(time));
  recordList.appendChild(li);
}
