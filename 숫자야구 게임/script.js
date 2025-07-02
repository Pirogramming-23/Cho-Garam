let answer = [];
let attempts = 9;
const maxAttempts = 9;

function init_game() {
    answer = generateUniqueNumbers();
    attempts = maxAttempts;

    document.getElementById("number1").value = "";
    document.getElementById("number2").value = "";
    document.getElementById("number3").value = "";

    document.getElementById("results").innerHTML = "";
    document.getElementById("game-result-img").src = "";
    document.getElementById("attempts").textContent = attempts;

    document.querySelector(".submit-button").disabled = false;

    console.log("정답:", answer); 
}

function generateUniqueNumbers() {
    const digits = [];
    while (digits.length < 3) {
        const rand = Math.floor(Math.random() * 10);
        if (!digits.includes(rand)) {
            digits.push(rand);
        }
    }
    return digits;
}

function check_numbers() {
    const input1 = document.getElementById("number1").value.trim();
    const input2 = document.getElementById("number2").value.trim();
    const input3 = document.getElementById("number3").value.trim();

    if (input1 === "" || input2 === "" || input3 === "") {
        alert("모든 칸을 입력해주세요.");
        clearInputs();
        return;
    }

    const guess = [parseInt(input1), parseInt(input2), parseInt(input3)];

    if (new Set(guess).size !== 3) {
        alert("중복되지 않는 숫자를 입력해주세요.");
        clearInputs();
        return;
    }

    let strike = 0;
    let ball = 0;

    for (let i = 0; i < 3; i++) {
        if (guess[i] === answer[i]) {
            strike++;
        } else if (answer.includes(guess[i])) {
            ball++;
        }
    }

    const resultContainer = document.getElementById("results");

    const line = document.createElement("div");
    line.className = "check-result";

    const numberDiv = document.createElement("div");
    numberDiv.className = "left";
    numberDiv.textContent = guess.join(" ");

    const resultDiv = document.createElement("div");
    resultDiv.className = "right";

    if (strike === 0 && ball === 0) {
        const outNum = document.createElement("span");
        outNum.textContent = "0";

        const outIcon = document.createElement("span");
        outIcon.className = "num-result out";
        outIcon.textContent = "O";

        resultDiv.appendChild(outNum);
        resultDiv.appendChild(outIcon);
    } else {
        if (strike > 0) {
            const sNum = document.createElement("span");
            sNum.textContent = strike;

            const s = document.createElement("span");
            s.className = "num-result strike";
            s.textContent = "S";

            resultDiv.appendChild(sNum);
            resultDiv.appendChild(s);
        }
        if (ball > 0) {
            const bNum = document.createElement("span");
            bNum.textContent = ball;

            const b = document.createElement("span");
            b.className = "num-result ball";
            b.textContent = "B";

            resultDiv.appendChild(bNum);
            resultDiv.appendChild(b);
        }
    }

    line.appendChild(numberDiv);
    line.appendChild(resultDiv);
    resultContainer.appendChild(line);

    attempts--;
    document.getElementById("attempts").textContent = attempts;

    clearInputs();

    if (strike === 3) {
        endGame(true);
    } else if (attempts === 0) {
        endGame(false);
    }
}

function clearInputs() {
    document.getElementById("number1").value = "";
    document.getElementById("number2").value = "";
    document.getElementById("number3").value = "";
    document.getElementById("number1").focus();
}

function endGame(isWin) {
    const img = document.getElementById("game-result-img");
    const btn = document.querySelector(".submit-button");

    if (isWin) {
        img.src = "success.png";
    } else {
        img.src = "fail.png";

        const resultContainer = document.getElementById("results");
        const answerLine = document.createElement("div");
        answerLine.textContent = `정답은: ${answer.join("")}`;
        answerLine.style.fontWeight = "bold";
        resultContainer.appendChild(answerLine);
    }

    btn.disabled = true;
}

document.addEventListener("DOMContentLoaded", init_game);
