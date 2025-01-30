
// start Random password Generator
function generatePassword(length, includeLowercase, includeUppercase, includeNumbers, includeSymbols) {
    const lowercaseChars = "abcdefghijklmnopqrstuvwxyz";
    const uppercaseChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const numberChars = "0123456789";
    const symbolChars = "!@#$%^&*()_+-=";
    let allowedChars = "";
    let password = "";

    if (includeLowercase) allowedChars += lowercaseChars;
    if (includeUppercase) allowedChars += uppercaseChars;
    if (includeNumbers) allowedChars += numberChars;
    if (includeSymbols) allowedChars += symbolChars;

    if (length <= 0) {
        return "(Password length must be at least 1)";
    }
    if (allowedChars.length === 0) {
        return "(At least one set of characters needs to be selected)";
    }

    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * allowedChars.length);
        password += allowedChars[randomIndex];
    }
    return password;
}

document.addEventListener("DOMContentLoaded", function () {
    const generateButton = document.getElementById("generatePasswordButton");
    const passwordDisplay = document.getElementById("generatedPassword");
    const copyButton = document.getElementById("copyPasswordButton");

    // Xử lý khi nhấn nút "Simple Password"
    generateButton.addEventListener("click", function () {
        const length = 18; // Độ dài mật khẩu mong muốn
        const includeLowercase = true;
        const includeUppercase = true;
        const includeNumbers = true;
        const includeSymbols = true;

        const password = generatePassword(length, includeLowercase, includeUppercase, includeNumbers, includeSymbols);
        passwordDisplay.textContent = password; // Hiển thị mật khẩu
    });

    // Xử lý khi nhấn nút "Copy"
    copyButton.addEventListener("click", function () {
        const password = passwordDisplay.textContent;
        if (password) {
            navigator.clipboard.writeText(password).then(function () {
                alert("Password copied to clipboard!");
            }).catch(function (err) {
                console.error("Could not copy password: ", err);
            });
        } else {
            alert("No password to copy!");
        }
    });
});
//  End Random password Generator


// Show/hide password onClick of button using Javascript only

// https://stackoverflow.com/questions/31224651/show-hide-password-onclick-of-button-using-javascript-only


