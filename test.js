// function fact(n) {
//     result = 1
//     for (var i; i = n ,i--;){
//         result *= i
        
//     }
//     return result
// }


// const facts = (n) => {
//     if (n >=1){
//         return n* fact(n-1)
//     }
//     else return 1 }

//     console.log(fact(5));

function fib(n) {
    let a = 1;
    let b = 1;
    for ( i = 3; i <= n ; i++) {
        let c = a + b;
        a = b;
        b = c;
        }
    return b;
}
console.log(fib(8))

