
function generatePassword(length , includeLowercase, includeUppercase,includeNumbers,includeSymbols){
    const lowercaseChars="abcdefghijklmnopqrstuvwxyz";
    const uppercaseChars="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const symbolChars="!@#$%^&*()_+-=";
    const numberChars="0123456789";

    let allowedChars = "";
    let password = "";
    allowedChars += includeLowercase ? lowercaseChars : "";
    allowedChars += includeLowercase ? uppercaseChars : "";
    allowedChars += includeNumbers ? symbolChars : "";
    allowedChars += includeNumbers ? numberChars : "";
    
    if(length <=0 ){
        return `(password length must be at least 1)`;

    }
    if(allowedChars.length === 0){
        return `(At least 1 set of character needs to be selected)`;

    }
    for(let i = 0; i <= length ; i++){
        const randomIndex = Math.floor(Math.random() *allowedChars.length);
        password += allowedChars[randomIndex];
    }
    console.log(allowedChars);
    return password;
}

const passwordLenght=18;
const includeLowercase=true;
const includeUppercase=true;
const includeNumbers= true;
const includeSymbols= true;
const password=generatePassword(passwordLenght,
                                includeLowercase,
                                includeUppercase,
                                includeNumbers,
                                includeSymbols);
console.log(`Generated password: ${password}`);





