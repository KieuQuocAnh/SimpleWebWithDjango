//array = a variable like structure that can hold more than 1 value
// let fruits =["apple","banana","orange","something"];
// // fruits[3]="cocount";
// fruits.pop();
// fruits.pop();
// fruits.push("something");
// fruits.unshift("mango");

// let numOFFurits= fruits.length;
// console.log(fruits[0]);
// console.log(fruits[1]);
// console.log(fruits[2]);
// console.log(fruits[3]);
// console.log(numOFFurits);
// for(let i = numOFFurits; i >=0 ; i --){
//     console.log(fruits[i]);
// }



// spread operator=. . .

// let username="Bro Code";
// let letters=[...username];
// let letters2=[...username].join("-");
// console.log(letters);
// console.log(letters2);

// reset parameters


// function openFridge(...foods){
//     console.log(...foods);
// }
// function getFood(...foods){
//     return foods;
// }

// const food1=`pizza`;
// const food2=`sushi`;
// const food3=`tacos`;
// const food4=`ramen`;
// const food5=`ice cream`;
// const foods= getFood(food1,food2,food3,food4,food5);
// console.log(foods);


// function sum(...numbers){
//     let result = 0;
//     for(let i = 0; i < numbers.length; i++){
//         result += numbers[i];
//         }
//         return result;
// }


// const total = sum(1,2,3,4,5);
// console.log("Your total is : ",total);

// function getAverage(...numbers){
//     let result = 0 ;
//     for(let number of numbers){
//         result += number;
         
//     }
//     return result / numbers.length;
// }
// const total2 = getAverage(75,100,85,90,50);
// console.log(total2);

// function combineStrings(...strings){
//     return strings.join(" ");
// }

// const fullName = combineStrings("Mr.","Spongebob","Squarepants","III");
// console.log(fullName);


//Call Back

// hello(goodbye);
// hello(leave);




// // function hello(){
// //     console.log("Hello");
// // }
// // function hello(){
// //     setTimeout(function (){
// //         console.log("Hello");
// //     },3000);
    
// // }
// function hello(callback){
//     console.log("Hello");
//     callback();
// }

// function leave(){
//     console.log("Leave!");
// }
// function goodbye(){
//     console.log("Goodbye");
// }


sum(displayPage,1,2);
function sum(callback,x,y){
    let result= x+y;
    callback(result)
}
function displayConsole(result){
    console.log(result);
}


function displayPage(result){
    document.getElementById("myH1").textContent = result;
}



