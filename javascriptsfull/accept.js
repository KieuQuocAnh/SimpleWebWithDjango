//how to accept user
// 1. easy way = window prompt
//professional  way = Html text box 

// let username = window.prompt("Wthat's Your username?")
// console.log(username);
// let username;
// document.getElementById("mySubmit").onclick=function(){
//     username = document.getElementById("myText").value;
//     // console.log(username)
//     document.getElementById("myH1").textContent=`Hello ${username}`;

// }
{/* <h1 id="myH1">Whelcome</h1>
<label>Username: </label>
<input id="myText"><br><br>
<button id="mySubmit">submit</button> */}


// type conversion = change the datatype of a value to another(String ,numbers,booleans)// ncl gán giá trị , 




// let age = window.prompt ("How old are you?")

// age+=1;
// console.log(age, typeof age)

// let x ="pizza";
// let y ="pizza";
// let z ="pizza";
// x= Number(x);
// y=String(y);
// z=Boolean(z);
// console.log(typeof x,typeof y,typeof z);


//const

// const PI=3.14159;
// let radius;
// let circumference;


// radius = Number(radius);
// circumference = 2 * PI * radius;


// document.getElementById("mySubmit").onclick=function(){
//     radius=document.getElementById("myText").value;
//     circumference=2 * PI * radius;
//     document.getElementById("myH3").textContent=circumference;
// }


// <h1 id ="myH1"> Enter the radius of a circle: </h1>
// <input type="text" id="myText">
// <button id="mySubmit">submib</button>
// <h3 id="myH3">...</h3>


// const decreaseBtn=document.getElementById("decreaseBtn");
// const resetBtn=document.getElementById("resetBtn");
// const increaseBtn=document.getElementById("increaseBtn");

// const countLabel=document.getElementById("countLabel");
// let count = 0;
// increaseBtn.onclick=function()
// {
//     count++;
//     countLabel.textContent=count;
// }
// decreaseBtn.onclick=function(){
//     count--;
//     countLabel.textContent=count;
// }
// resetBtn.onclick=function(){
//     count=0;
//     countLabel.textContent=count;
//     }



//math=build-in object that provides a collection of properties and methods
// console.log(Math.PI)
// console.log(Math.E)

// let x= 4.2122;
// let y =2;
// let z;
// z= Math.round(x)
// z=Math.floor(x)
// z=Math.ceil(x)
// z=Math.trunc(x)
// Math.pow()

// console.log(z);



// Random Number Generator
// const min=50;
// const max=100;

// let randomNum_1=Math.random();
// let randomNum_2=Math.random()*6;
// let randomNum_3=Math.floor(Math.random()*6);
// let randomNum_4=Math.floor(Math.random()*100)+1;  
// let randomNum_5=Math.floor(Math.random()*max)+min;  
// let randomNum_6=Math.floor(Math.random()*(max-min)+min);  
// console.log(randomNum_1);
// console.log(randomNum_2);
// console.log(randomNum_3);
// console.log(randomNum_4);
// console.log(randomNum_5);
// console.log(randomNum_6);
// const myButton=document.getElementById("myButton");
// const myLabel1=document.getElementById("myLabel1");
// const myLabel2=document.getElementById("myLabel2");
// const myLabel3=document.getElementById("myLabel3");
// const min=1;
// const max=6;
// let randomNum1;
// let randomNum2;
// let randomNum3;
// myButton.onclick=function(){
//     randomNum1 = Math.floor(Math.random() * max) + min;
//     randomNum2 = Math.floor(Math.random() * max) + min;
//     randomNum3 = Math.floor(Math.random() * max) + min;
//     myLabel1.textContent=randomNum1;
//     myLabel2.textContent=randomNum2;
//     myLabel3.textContent=randomNum3;
// }


// if statements
// let age = 25;
// if(age>=18){
//     console.log("You are ole enough to enter this stie");
// }
// else{
//     console.log("You must be 18+ to enter this site");
// }


// const now = new Date();

// let time =now.getHours();
// console.log(time)

// if(time>=8 && time<=12){
//     console.log("Good morning");

//     }else if(time>=13 && time<=17){

//         console.log("Good afternoon");

//         }else if(time>=18 && time<=23){

//             console.log("Good evening");

//             }else{

//                 console.log("Good night");
//                 }


// const myText=document.getElementById("myText");
// const mySubmit=document.getElementById("mySubmit");
// const resultElement=document.getElementById("resultElement")
// let age;

// mySubmit.onclick=function(){

//     age = myText.value;// Thay 'Value' thành 'value'
//     age = Number(age);
//     console.log(age);
    

//     if(age >= 100) {
//         resultElement.textContent="You are TOO OLD to enter this site";
        
//     }
//     else if(age == 0) {
//         resultElement.textContent="You can't enter .You were just born";
        
//     }
//     else if(age >= 18){
//         resultElement.textContent="You are old enough to enter this site";

    
//     }else if(age < 0){
//         resultElement.textContent="Your age can't be below 0";
//     }else{
//         resultElement.textContent="You must be 18+ to enter this site";
//     }

// }


// .Checked



// const myCheckBox=document.getElementById("myCheckBox");
// const visaBtn=document.getElementById("visaBtn");
// const masterCardBtn=document.getElementById("masterCardBtn");
// const payPalBtn=document.getElementById("payPalBtn");

// const mySubmit=document.getElementById("mySubmit");
// const subResult=document.getElementById("subResult");
// const paymentResult=document.getElementById("paymentResult");


// mySubmit.onclick=function() {

//     if(myCheckBox.checked){
//         subResult.textContent="You are subscribed!";


//     }
//     else{
//         subResult.textContent="You are NOT subscribed";
//     }
//     if(visaBtn.checked){
//         paymentResult.textContent="You are using VISA";
//     }else if(masterCardBtn.checked){
//         paymentResult.textContent="You are using MASTER CARD";
//     }else if (payPalBtn.checked) {
//         paymentResult.textContent="You are using PAY PAL";

//     }
//     else{
//         paymentResult.textContent="You are not using any payment method";
//         }

// }




//  ternary operation


// let age=12
// // age >= 18 ? "You're an adult " : " You're a minor";
// let message = age >= 18 ? "You're an adult " : " You're a minor";

// console.log(message)

// let time =9;
// let greeting = time <12 ? "Good morning " : "Good afternoon";
// console.log(greeting);

// let purchaseAmount = 125;
// let discount = purchaseAmount >= 100 ? 10 : 0;
// console.log(`Your total is ${purchaseAmount -purchaseAmount *( discount/100)}`)




// SWITCH


// time = new Date()
// let day = time.getDay();
// console.log (day);
// switch(day){
//     case 1:
//         console.log("Today is Monday");
//         break;
//     case 2:
//         console.log("Today is Tuesday");
//         break;
//     case 3:
//         console.log("Today is Wednesday");
//         break;
//     case 4:
//         console.log("Today is Thursday");
//         break;
//     case 5:
//         console.log("Today is Friday");
//         break;
//     case 6:
//         console.log("Today is Saturday");
//         break;
//     case 7:
//         console.log("Today is Sunday");
//         break;
//     default:
//         console.log(`${day} is not day `)  ; 

//}
// let testScore=25;
// let letterGrade;
// switch(true){
//     case testScore >=90:
//         letterGrade = "A";
//         break;
//     case testScore >=80:
//         letterGrade = "B";
//         break;
//     case testScore >=70:
//         letterGrade = "C";
//         break;
//     case testScore >=60:
//         letterGrade = "D";
//     break;   
//     default:
//         letterGrade = "F";
// } 
// console.log(letterGrade);



// let userName="Brocode";
// console.log(userName.charAt(2));
// console.log(userName.indexOf("o"));
// console.log(userName.lastIndexOf("o"));
// console.log(userName.length);

// userName1=userName.trim();




// console.log(userName1);





// let userName = "BroCode";
// let result = userName.startsWith(" ");
// let result1 = userName.includes(" ");


// console.log(result);
// if(result){
//     console.log("The string starts with ' '");
// }else{
//     console.log(userName);

// }





// string slicing \


// const fullName ="Bro code";

// let firstName=fullName.slice(0,3);
// let lastName=fullName.slice(4,10);
// console.log(firstName);
// console.log(lastName);


//METHOD CHAINING 

// let username = window.prompt("Enter Your Username ")



// username=username.trim().charAt(0).toUpperCase()+username.trim().slice()
// console.log(username)




// while loop


// let username="";
// while(username==="" || username === null){
//     username=window.prompt(`Enter you name: `)

// }
// console.log(`Hello ${username}`);


// let loggedIn= false;
// let username ;
// let password;
// do{
//     username=window.prompt("Enter your username");
//     password=window.prompt("Enter your password");
//     if(username ==="myUsername" && password === "myPassword"){
//         loggedIn=true;
//         console.log("You are logged in");

        
//     }
//     else{
//         console.log("Invalid username or password");
//         }
// }while(!loggedIn)





//for loop



// for(let i =1; i <=20; i ++){


//     if( i == 13){
//        break;
//     }
//     else{
//         console.log(i)
//     }
    
// }




//Number guessing game 


const minNum=1;
const maxNum=100;
const answer = Math.floor(Math.random()*(maxNum-minNum+1))+minNum;
let guess ;
let attempts = 0;
let running =true;
console.log(typeof(answer),answer);
while(running){
    guess = window.prompt(`Guess a number between ${minNum} and ${maxNum}`);
    guess = Number(guess);
    if(isNaN(guess)){
        window.alert("Please enter a vaild number");      
    }
    else if(guess < minNum || guess > maxNum){
        window.alert("Please enter a vaild number");
        }
    else{
        attempts ++;
        if (guess < answer){
            window.alert("TOO LOW! TRY AGAIN");
        }
        else if ( guess > answer){
            window.alert("TOO HIGH! TRY AGAIN");
        }
        else{
            window.alert(`CORRECT! the answer was ${answer}. It took you ${attempts} attempts congratulations`);
            running=false;
            }

    }
    
}